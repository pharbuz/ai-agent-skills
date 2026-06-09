# Integrating dt-async into async applications

Patterns for using the client in real services (FastAPI, Celery, long-running
workers). Names are illustrative — adapt to your architecture.

## Client lifecycle

`DynatraceAsync` wraps a single httpx `AsyncClient`. Close it to release
connections.

- **Scripts / request-scoped**: use the async context manager.
  ```python
  async with DynatraceAsync(base_url=..., credentials=...) as dt:
      ...
  ```
- **Long-lived (app-scoped)**: build once, reuse across requests, close on
  shutdown with `await dt.aclose()`.

The OAuth client refreshes its token automatically, so a long-lived OAuth client
keeps working across token expiries — no manual refresh needed.

## Factory pattern: build a configured client from stored credentials

Centralize base-URL and scope decisions in one place so callers don't repeat
them.

```python
import logging
from dynatrace import DynatraceAsync, DynatraceOAuthCredentials, DynatraceAccessToken

def build_oauth_client(env_id: str, creds, *, logger: logging.Logger | None = None,
                       classic: bool = False) -> DynatraceAsync:
    host = "live" if classic else "apps"
    return DynatraceAsync(
        base_url=f"https://{env_id}.{host}.dynatrace.com",
        credentials=DynatraceOAuthCredentials(
            client_id=creds.client_id,
            client_secret=creds.client_secret,
            account_uuid=creds.account_uuid,
            scope=creds.scope or "account-uac-read account-env-read",
        ),
        log=logger,
        verify_ssl=True,
    )

def build_account_client(creds, *, logger=None) -> DynatraceAsync:
    # Account API lives on api.dynatrace.com
    return DynatraceAsync(
        base_url="https://api.dynatrace.com",
        credentials=DynatraceOAuthCredentials(
            client_id=creds.client_id, client_secret=creds.client_secret,
            account_uuid=creds.account_uuid, scope=creds.scope,
        ),
        log=logger, verify_ssl=True,
    )

def build_token_client(env_id: str, token: str, *, logger=None) -> DynatraceAsync:
    # Config V1 / Environment V1 need an API token
    return DynatraceAsync(
        base_url=f"https://{env_id}.live.dynatrace.com",
        credentials=DynatraceAccessToken(token=token),
        log=logger, verify_ssl=True,
    )
```

> Config-V1 APIs need a token while Platform/Account need OAuth, so a workflow
> spanning both should build **two clients** from these factories.

## Injected-service pattern

Wrap Dynatrace operations in a service that receives the client by constructor
injection. This keeps domain logic testable and hides the raw API shape.

```python
from dynatrace import DynatraceAsync

class EntityService:
    def __init__(self, dt: DynatraceAsync) -> None:
        self._dt = dt

    async def list_hosts(self, selector: str = 'type("HOST")') -> list:
        return await (await self._dt.entities.list(selector)).to_list()

    async def host(self, entity_id: str):
        return await self._dt.entities.get(entity_id, fields="properties,tags")
```

## FastAPI

Provide the client (or a service wrapping it) as a dependency. Build per request
for request-scoped credentials, or reuse an app-scoped client.

```python
from fastapi import Depends, FastAPI

app = FastAPI()

async def get_dt() -> DynatraceAsync:
    dt = build_oauth_client(env_id, load_creds())
    try:
        yield dt                     # request-scoped: closed after the response
    finally:
        await dt.aclose()

@app.get("/hosts")
async def hosts(dt: DynatraceAsync = Depends(get_dt)):
    return [h.json() for h in await (await dt.entities.list('type("HOST")')).to_list()]
```

For an app-scoped client, create it in a lifespan handler and `aclose()` it on
shutdown; inject the shared instance instead of building per request.

## Celery / background workers

Celery tasks are sync entry points; run the async client with `asyncio.run`
(or your worker's event-loop helper), and build the client inside the task from
the task's arguments.

```python
import asyncio

@shared_task
def sync_problems(env_id: str) -> int:
    async def _run() -> int:
        async with build_oauth_client(env_id, load_creds()) as dt:
            problems = await (await dt.problems.list()).to_list()
            return len(problems)
    return asyncio.run(_run())
```

Keep the client inside the task coroutine so it's created and closed within the
same event loop. Don't share one `DynatraceAsync` instance across event loops.

## Testing & mocking

The client talks HTTP via httpx, so the cleanest tests stub at the HTTP layer
with **respx** (httpx mock) — no monkeypatching of the library internals:

```python
import httpx, respx, pytest
from dynatrace import DynatraceAsync, DynatraceAccessToken

@pytest.mark.asyncio
@respx.mock
async def test_list_hosts():
    respx.get(url__regex=r".*/api/v2/entities").mock(
        return_value=httpx.Response(200, json={"entities": [
            {"entityId": "HOST-1", "displayName": "h1"}], "totalCount": 1})
    )
    async with DynatraceAsync(
        base_url="https://t.live.dynatrace.com",
        credentials=DynatraceAccessToken(token="dt0c01.x"),
    ) as dt:
        hosts = await (await dt.entities.list('type("HOST")')).to_list()
    assert hosts[0].display_name == "h1"
```

Alternatively, inject a fake service object in place of the real one at the
boundary (the injected-service pattern makes this trivial). For OAuth clients in
tests, prefer an API-token client or mock the SSO token endpoint too.
