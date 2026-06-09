# Usage patterns

All examples assume an open client `dt` (see [SKILL.md](../SKILL.md)).

## Pagination

`list()`-style methods return a `PaginatedList[T]` (JSON-body paging via
`nextPageKey`) or `HeaderPaginatedList[T]` (paging via the `next-page-key`
header). Both are **async-iterables** that fetch subsequent pages on demand.

```python
# Stream (low memory) — pages are fetched as you iterate
async for problem in await dt.problems.list():
    print(problem.title)

# Materialize all pages — note the DOUBLE await
problems = await (await dt.problems.list()).to_list()

# len() reports the API's totalCount when available (else items seen so far)
page = await dt.entities.list('type("HOST")')
print(len(page))
```

- A plain `for` raises `TypeError("... use 'async for' or await to_list()")`.
- The first page is fetched eagerly when the list is created (`.initialize()`),
  so an auth/permission error surfaces immediately, not mid-iteration.

## Result objects

Every result is a `DynatraceObject` subclass: camelCase JSON fields become
snake_case attributes, and `.json()` returns the original raw dict.

```python
host = await dt.entities.get("HOST-1234567890ABCDEF", fields="properties,tags")
host.entity_id        # "HOST-1234567890ABCDEF"
host.display_name     # str
host.properties       # dict
host.tags             # list[METag]
host.json()           # raw API dict
```

Some objects expose their own action methods, e.g. a plugin endpoint can delete
itself:

```python
async for plugin in await dt.plugins.list():
    async for endpoint in plugin.endpoints:
        if "test" in endpoint.name:
            await endpoint.delete(plugin.id)
```

## Errors, retries, rate limits

- **Status ≥ 400 raises a plain `Exception`** with the URL and response body in
  the message — there is no custom exception class, so catch `Exception`.
- **Retries** (`retries`, `retry_delay_ms`) cover the forcelist
  `{400,401,403,404,413,429,500,502,503,504}` and httpx transport errors.
- **429** with `too_many_requests_strategy=TOO_MANY_REQUESTS_WAIT` sleeps for the
  `Retry-After` header (default 5s) and retries until it clears.

```python
from dynatrace import TOO_MANY_REQUESTS_WAIT
try:
    slos = await (await dt.slos.list()).to_list()
except Exception as exc:           # includes 4xx/5xx with the response body
    logger.error("Dynatrace call failed: %s", exc)
    raise
```

## Metrics

```python
# Query data points (PaginatedList of series collections)
async for series in await dt.metrics.query(
    "builtin:host.cpu.idle", resolution="Inf",
):
    for data in series.data:
        for ts, value in zip(data.timestamps, data.values):
            print(data.dimensions, ts, value)

# List metric descriptors matching a selector
async for descriptor in await dt.metrics.list("builtin:host.*"):
    print(descriptor)
```

## DQL / Grail

OAuth only, under `dt.platform.grail_query_execution`. Short queries return rows
directly; long-running ones return a request token to poll.

```python
resp = await dt.platform.grail_query_execution.execute(
    "fetch logs | filter loglevel == 'ERROR' | summarize count(), by:{dt.entity.host}",
    default_timeframe_start="now-2h",
    default_timeframe_end="now",
    max_result_records=1000,
)

# If the query is still running, poll with the returned request token:
# while resp.state == "RUNNING":
#     resp = await dt.platform.grail_query_execution.poll(resp.request_token)
# rows = resp.result.records

# Cancel a running query:
# await dt.platform.grail_query_execution.cancel(resp.request_token)
```

`execute(...)` accepts the full Grail body as keyword args
(`default_sampling_ratio`, `default_scan_limit_gbytes`, `fetch_timeout_seconds`,
`filter_segments`, `max_result_bytes`, `timezone`, `enrich`, …).

## Settings 2.0

```python
from dynatrace.environment_v2.settings import SettingsObjectCreate

obj = SettingsObjectCreate(
    schema_id="builtin:anomaly-detection.metric-events",
    value={...},               # schema-specific payload
    scope="environment",
)
await dt.settings.create_object(validate_only=False, body=obj)
# Tip: pass validate_only=True first to dry-run the payload against the schema.
```

## Tokens & credential vault

```python
from dynatrace.environment_v2.tokens_api import SCOPE_METRICS_READ, SCOPE_METRICS_INGEST
new_token = await dt.tokens.create("metrics_token",
                                   scopes=[SCOPE_METRICS_READ, SCOPE_METRICS_INGEST])
print(new_token.token)

from dynatrace.environment_v2.credential_vault import PublicCertificateCredentials
cred = PublicCertificateCredentials(
    name="my_cred", scopes=["EXTENSION"], description="...",
    owner_access_only=False, certificate=pem_text, password="",
    certificate_format="PEM",
)
created = await dt.credentials.post(cred)
print(created.id)
```

## Timeframes

Methods that take a timeframe accept `datetime` objects or Dynatrace relative
strings (`"now-3d"`, `"now-2h"`). `datetime` values are converted for you.

```python
from datetime import datetime, timedelta
async for token in await dt.tokens.list(fields="+lastUsedDate,+scopes"):
    if token.last_used_date and token.last_used_date < datetime.now() - timedelta(days=90):
        ...  # stale token
```
