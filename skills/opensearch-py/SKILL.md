---
name: opensearch-py
description: >-
  Build, debug, test, or migrate Python code using the official OpenSearch
  client package `opensearch-py` (import `opensearchpy`). Trigger WHENEVER the
  user installs or imports `opensearch-py`/`opensearchpy`; uses `OpenSearch`,
  `AsyncOpenSearch`, `RequestsHttpConnection`, `AIOHttpConnection`,
  `AWSV4SignerAuth`, `helpers.bulk`, `streaming_bulk`, `parallel_bulk`, `scan`,
  `reindex`, `Search`, `Document`, `Index`, `Q`, `A`, `UpdateByQuery`, CAT,
  cluster, indices, ingest, nodes, security, snapshot, tasks, features,
  alerting, index-management, ML Commons plugin clients, serializers,
  transports, connection pools, sniffing, TLS/auth, SigV4, DSL mappings, search
  queries, index templates, aliases, bulk indexing, scroll/scan, or fixes
  OpenSearch Python client connection errors, auth failures, SSL verification,
  async-extra import problems, helper retry behavior, DSL serialization, mapping
  setup, endpoint parameter names, getting-started workflows, and version/API
  compatibility issues.
---

# opensearch-py

Use this skill for Python code that talks to OpenSearch through the official
`opensearch-py` package. Import path is `opensearchpy`, not `opensearch_py`.

Do not browse live documentation while using this skill. The API reference and
examples are bundled under `references/`; load only the relevant local file.

## Default Workflow

1. Inspect installed version, extras, and current imports before editing.
2. Choose the API layer:
   - Low-level client: `OpenSearch` for REST endpoint calls.
   - Async client: `AsyncOpenSearch` only when `opensearch-py[async]` or
     `aiohttp` support is installed.
   - Helpers: `bulk`, `streaming_bulk`, `parallel_bulk`, `scan`, `reindex` for
     large document workflows.
   - DSL helpers: `Search`, `Document`, `Index`, `Q`, `A`, fields, mappings, and
     update-by-query for query construction and model-style documents.
   - Namespace/plugin clients: use attributes on `client` (`client.indices`,
     `client.cluster`, `client.security`, etc.) instead of instantiating
     namespace clients directly.
3. Configure hosts/auth/TLS explicitly. For production TLS, keep
   `use_ssl=True` and `verify_certs=True`; provide CA/client certificates or
   AWS SigV4 auth when required.
4. Preserve endpoint parameter names from the local reference. Many generated
   methods are keyword-only and use `body=`, `index=`, `id=`, `params=`, and
   `headers=`.
5. Handle `opensearchpy.exceptions.OpenSearchException` subclasses deliberately:
   `NotFoundError`, `RequestError`, `AuthenticationException`,
   `AuthorizationException`, `ConnectionError`, `ConnectionTimeout`,
   `TransportError`, `SSLError`, and `SerializationError`.
6. Add tests with mocked clients or a disposable OpenSearch container when code
   changes query shape, bulk actions, index creation, retries, or exception
   handling.

## Version And Extras Checks

```bash
python -m pip show opensearch-py
python - <<'PY'
import opensearchpy
print(getattr(opensearchpy, "__version__", "unknown"))
print("AsyncOpenSearch:", hasattr(opensearchpy, "AsyncOpenSearch"))
PY
```

Install async support when the project needs `AsyncOpenSearch` or
`AIOHttpConnection`:

```bash
python -m pip install "opensearch-py[async]"
```

## Minimal Sync Client

```python
from opensearchpy import OpenSearch


client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=False,  # local dev only; use CA verification in production
    ssl_show_warn=False,
)

info = client.info()
client.indices.create(index="orders", body={"settings": {"index": {"number_of_shards": 1}}})
client.index(index="orders", id="1", body={"status": "paid", "total": 42})
result = client.search(index="orders", body={"query": {"term": {"status": "paid"}}})
```

## Minimal Async Client

```python
import asyncio
from opensearchpy import AsyncOpenSearch


async def main() -> None:
    client = AsyncOpenSearch(hosts=[{"host": "localhost", "port": 9200}])
    try:
        response = await client.search(index="orders", body={"query": {"match_all": {}}})
        print(response["hits"]["total"])
    finally:
        await client.close()


asyncio.run(main())
```

## Decision Rules

- Prefer `OpenSearch(...)` plus namespace attributes for endpoint calls:
  `client.indices.create(...)`, `client.cluster.health(...)`,
  `client.security.authinfo(...)`, `client.snapshot.create(...)`.
- Prefer `helpers.streaming_bulk` for large imports where per-item success/error
  handling matters; use `helpers.bulk` for simpler all-at-once summary behavior.
- Use `helpers.scan` for scroll-style full reads. Do not implement scroll loops
  manually unless the project needs custom control.
- Use DSL helpers when query composition benefits from Python objects; use raw
  dict request bodies when preserving exact JSON is clearer.
- Use `AWSV4SignerAuth` with `RequestsHttpConnection` for Amazon OpenSearch
  Service and OpenSearch Serverless SigV4 auth.
- Do not set `verify_certs=False` outside local development/test fixtures.
- Do not silently ignore `RequestError` from index creation or mapping updates;
  inspect whether the index already exists, the mapping is incompatible, or the
  request body is invalid.
- Do not instantiate `CatClient`, `IndicesClient`, `SecurityClient`, plugin
  clients, or other namespace clients directly unless testing internals; access
  them through the parent client.

## References

- Read [references/examples.md](references/examples.md) for complete local code
  patterns: sync, async, TLS, AWS SigV4, bulk, scan, DSL, documents, and tests.
- Read [references/sample-code-manifest.md](references/sample-code-manifest.md)
  when the task benefits from official sample code; then read the matching file
  under `assets/samples/` locally instead of browsing GitHub.
- Read [references/python-low-level-guide.md](references/python-low-level-guide.md)
  for the official getting-started flow: setup, connecting to OpenSearch,
  Amazon OpenSearch Service, Amazon OpenSearch Serverless, creating indexes,
  indexing, bulk operations, searching, deleting documents/indexes, and the
  bundled sample program.
- Read [references/api-reference-index.md](references/api-reference-index.md)
  first when you need to locate a class or method.
- Read [references/clients-core.md](references/clients-core.md) for
  `OpenSearch`, `AsyncOpenSearch`, core document/search/bulk methods, and HTTP
  namespace calls.
- Read [references/clients-namespaces.md](references/clients-namespaces.md) for
  CAT, cluster, dangling indices, ingest, indices, nodes, remote, security,
  snapshot, tasks, and features clients.
- Read [references/connections-transport.md](references/connections-transport.md)
  for connection classes, TLS, serializers, connection pools, metrics,
  transports, sniffing, retries, and exceptions.
- Read [references/helpers-dsl.md](references/helpers-dsl.md) for helper
  functions and DSL classes: `Search`, `Document`, `Index`, `Mapping`, `Query`,
  `Agg`, fields, analysis, functions, faceted search, wrappers, and
  update-by-query.
- Read [references/plugins.md](references/plugins.md) for Alerting, Index
  Management, and ML Commons plugin clients.
