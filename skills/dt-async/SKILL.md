---
name: dt-async
description: >-
  Use the dt-async Python library (import `dynatrace`) to call the Dynatrace REST
  API asynchronously. Trigger WHENEVER the user works with `DynatraceAsync`,
  imports from `dynatrace` (`from dynatrace import DynatraceAsync,
  DynatraceOAuthCredentials, DynatraceAccessToken`), or builds async Python code
  that talks to a Dynatrace tenant — querying monitored entities, metrics,
  problems, logs, SLOs, settings 2.0, running DQL/Grail queries, managing
  tokens/ActiveGates, or Account/IAM and Platform APIs. Also trigger on async
  pagination over `dt.<service>.list(...)`, OAuth vs API-token auth for
  Dynatrace, choosing the tenant base URL (.apps/.live/api.dynatrace.com), or
  wiring a Dynatrace client into a FastAPI/Celery service. Covers client setup,
  auth, services, pagination, error handling, and integration patterns.
---

# dt-async — async Dynatrace REST API client

`dt-async` is an async Python client for the [Dynatrace REST API], built on
**httpx** + **authlib**. It's a fork of Dynatrace's official client focused on
ergonomic async use and typed result objects. Install as `dt-async`, import as
`dynatrace`.

```bash
pip install dt-async
```

```python
from dynatrace import DynatraceAsync, DynatraceOAuthCredentials, DynatraceAccessToken
```

[Dynatrace REST API]: https://www.dynatrace.com/support/help/dynatrace-api

## Mental model

1. **Create a client** — `DynatraceAsync(base_url, credentials, ...)`. It's an
   async context manager; use `async with` (or call `await dt.aclose()`).
2. **Credentials decide which APIs you get** — OAuth and API-token unlock
   *different* service sets (see below). This is the #1 source of confusion.
3. **Call `await dt.<service>.<method>(...)`** — every method is a coroutine.
4. **Iterate list results with `async for`** (or `await ....to_list()`); paging
   is automatic.
5. **Results are typed objects** with snake_case attributes; `.json()` returns
   the raw dict.

```python
import asyncio
from dynatrace import DynatraceAsync, DynatraceOAuthCredentials

async def main():
    async with DynatraceAsync(
        base_url="https://abc12345.apps.dynatrace.com",
        credentials=DynatraceOAuthCredentials(
            client_id="dt0s02...",
            client_secret="dt0s02...",
            account_uuid="your-account-uuid",
            scope="storage:entities:read storage:metrics:read",
        ),
    ) as dt:
        async for entity in await dt.entities.list('type("HOST")',
                                                    fields="properties.memoryTotal"):
            print(entity.entity_id, entity.display_name, entity.properties)

asyncio.run(main())
```

## Authentication — pick the right credentials

Two credential types, and **they expose different services** (the client raises a
helpful `AttributeError` if you reach for one that your credentials don't allow):

| | `DynatraceOAuthCredentials` | `DynatraceAccessToken` |
|---|---|---|
| Header | OAuth2 bearer (auto-refreshed) | `Authorization: Api-Token <token>` |
| Fields | `client_id`, `client_secret`, `account_uuid`, `scope`, `sso_base_url` | `token` |
| Unlocks | **Platform** (`dt.platform.*` — DQL/Grail, Davis, AppEngine) and **Account** (`dt.account.*` — IAM, subscriptions) | **Environment V1** + **Config V1** (`dt.dashboards`, `dt.plugins`, `dt.timeseries`, `dt.management_zones`, …) |
| Both expose | Environment **V2**: `entities`, `metrics`, `problems`, `logs`, `settings`, `slos`, `security_problems`, `events_v2`, `tokens`, `credentials`, `activegates`, … | ← same |

```python
# OAuth 2.0 (client credentials) — for Platform/Account/V2
DynatraceOAuthCredentials(client_id="...", client_secret="...",
                          account_uuid="...", scope="...")

# API token — for Environment V1 / Config V1 / V2
DynatraceAccessToken(token="dt0c01...")
```

**Base URL** depends on what you call:

| Target | base_url |
|--------|----------|
| Platform APIs (Grail/DQL, AppEngine) & gen-3 environment | `https://<envId>.apps.dynatrace.com` |
| Classic environment APIs (V1/V2 on SaaS) | `https://<envId>.live.dynatrace.com` |
| Account Management API | `https://api.dynatrace.com` |

The `scope` string must list every permission the called APIs need (space-
separated). Full auth detail, scopes, refresh behaviour, and the exact
restricted-service lists → [`references/authentication.md`](references/authentication.md).

## Calling services

Pattern: `result = await dt.<service>.<method>(...)`. Single-object methods return
a typed object; `list()`-style methods return an async-iterable `PaginatedList`.

```python
# Single entity
host = await dt.entities.get("HOST-1234567890ABCDEF", fields="properties")
print(host.display_name, host.properties)

# Metrics — query data points, or list metric descriptors
async for series in await dt.metrics.query("builtin:host.cpu.idle", resolution="Inf"):
    print(series)
async for descriptor in await dt.metrics.list("builtin:host.*"):
    print(descriptor)

# Problems / logs / SLOs follow the same shape
async for problem in await dt.problems.list():
    print(problem)

# DQL / Grail (OAuth only)
resp = await dt.platform.grail_query_execution.execute(
    "fetch logs | filter status == 'ERROR' | limit 100"
)
# long-running queries return a request token to poll:
# resp = await dt.platform.grail_query_execution.poll(resp.request_token)
```

The full `dt.<service>` catalogue (every API → accessor, grouped by V2 / V1 /
Config V1 / Platform / Account, with credential-type availability) →
[`references/services.md`](references/services.md).

## Pagination

`list()`-style methods return a `PaginatedList` (or `HeaderPaginatedList`) that
pages automatically via `nextPageKey`. It is **async-only**:

```python
# Stream page by page (preferred — low memory)
async for item in await dt.problems.list():
    ...

# Materialize everything into a list
problems = await (await dt.problems.list()).to_list()
len_hint = len(await dt.problems.list())   # totalCount when the API reports it
```

A plain `for` over a `PaginatedList` raises `TypeError` ("use 'async for' or
await to_list()"). Don't forget the **double await** when materializing:
`await (await dt.x.list()).to_list()`.

## Errors, retries, rate limits

- **Any HTTP status ≥ 400 raises** a plain `Exception` whose message includes the
  URL and response body. Catch `Exception` around calls (the library does not
  define a custom exception type).
- **Retries**: pass `retries=N, retry_delay_ms=ms` to retry on
  `{400,401,403,404,413,429,500,502,503,504}`.
- **HTTP 429**: pass `too_many_requests_strategy=TOO_MANY_REQUESTS_WAIT`
  (`from dynatrace import TOO_MANY_REQUESTS_WAIT`) to sleep for the `Retry-After`
  value and retry until it clears.
- **Timeouts**: `timeout=<seconds>`. OAuth token fetch timeout: `token_timeout`.

```python
from dynatrace import DynatraceAsync, DynatraceAccessToken, TOO_MANY_REQUESTS_WAIT

dt = DynatraceAsync(
    base_url="https://abc12345.live.dynatrace.com",
    credentials=DynatraceAccessToken(token="dt0c01..."),
    retries=5, retry_delay_ms=1000,
    too_many_requests_strategy=TOO_MANY_REQUESTS_WAIT,
    timeout=30,
)
```

## Client options

| Option | Purpose |
|--------|---------|
| `base_url` (required) | Tenant URL; trailing slashes are trimmed |
| `credentials` (required) | `DynatraceOAuthCredentials` or `DynatraceAccessToken` |
| `retries`, `retry_delay_ms` | Retry count + delay on the status forcelist |
| `too_many_requests_strategy` | `TOO_MANY_REQUESTS_WAIT` to honor `Retry-After` on 429 |
| `timeout`, `token_timeout` | HTTP timeout / OAuth token-fetch timeout (default 30) |
| `proxies` | `{"https": "http://proxy:8080"}` |
| `headers` | Extra default headers merged into every request |
| `verify_ssl` | **Defaults to `False`** — set `True` to verify TLS in production |
| `log` | A `logging.Logger`; `print_bodies=True` prints request bodies |

## Using dt-async in an async app (FastAPI / Celery)

Two patterns that compose well (generalized — adapt names to your project):

```python
# 1) A factory that builds a configured client from your stored credentials
def build_dt_client(env_id: str, creds, *, logger=None) -> DynatraceAsync:
    return DynatraceAsync(
        base_url=f"https://{env_id}.apps.dynatrace.com",
        credentials=DynatraceOAuthCredentials(
            client_id=creds.client_id, client_secret=creds.client_secret,
            account_uuid=creds.account_uuid,
            scope=creds.scope or "account-uac-read account-env-read",
        ),
        log=logger,
    )

# 2) A service class that takes the client by injection and wraps operations
class EntityStatusService:
    def __init__(self, dt: DynatraceAsync) -> None:
        self._dt = dt

    async def list_hosts(self) -> list:
        return await (await self._dt.entities.list('type("HOST")')).to_list()
```

Lifecycle: prefer `async with DynatraceAsync(...) as dt:` for scripts and
request-scoped use so the httpx client is closed. For a long-lived client, call
`await dt.aclose()` on shutdown. More (DI, Celery tasks, testing/mocking) →
[`references/integration.md`](references/integration.md).

## Common pitfalls

- **Wrong credential type for the API.** `dt.platform.*` / `dt.account.*` need
  OAuth; `dt.dashboards`, `dt.plugins`, `dt.timeseries`, `dt.management_zones`
  (Config/V1) need an API token. The `AttributeError` message tells you which.
- **Forgetting the double `await`** on `list()` + `to_list()`.
- **Sync `for`** over a paginated result → `TypeError`; use `async for`.
- **`verify_ssl` defaults to `False`** — turn it on for production.
- **Scope too narrow** → 403. Widen the OAuth `scope` to cover every called API.
- **Not closing the client** — leaks httpx connections; use `async with` / `aclose()`.

## Reference files

- `references/authentication.md` — OAuth vs token, scopes, base URLs, refresh, restricted-service lists
- `references/services.md` — full `dt.<service>` catalogue by API group + availability
- `references/usage-patterns.md` — pagination, result objects, errors, DQL/Grail, settings 2.0, recipes
- `references/integration.md` — client lifecycle, factory + injected-service patterns, Celery, testing
