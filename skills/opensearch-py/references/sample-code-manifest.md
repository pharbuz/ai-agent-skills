# Sample Code Manifest

Local copy of `https://github.com/opensearch-project/opensearch-py/tree/main/samples` generated on 2026-07-27.
`samples/poetry.lock` is intentionally omitted because it is dependency lock metadata, not a code sample.

## How To Use

- Prefer reading the specific sample file under `assets/samples/` instead of browsing GitHub.
- Use samples as implementation patterns, but still adapt credentials, hosts, certificate paths, index names, cleanup, and error handling to the target project.
- Do not copy test credentials or `verify_certs=False` into production code.

## Categories
- `advanced_index_actions/`: index open/close, aliases, settings, mapping, analyzer, refresh, flush, force merge, split/shrink/clone, rollover, and delete index workflows.
- `aws/`: Amazon OpenSearch Service and Serverless SigV4 request signing patterns.
- `bulk/`: bulk API request body formats and `helpers.bulk` usage.
- `document_lifecycle/`: create, update, get, search, delete document lifecycle.
- `hello/`: minimal synchronous and asynchronous clients, Unicode documents.
- `index_template/`: component templates, index templates, aliases, and matching index creation.
- `json/`: JSON serializer-oriented hello examples.
- `knn/`: k-NN vector search basics, boolean filters, and efficient filters.
- `logging/`: log collection sample indexing structured logs.
- `search/`: search_after pagination sync and async.
- `security/`: security plugin role and user management examples.
- `snapshot/`: snapshot repository and snapshot workflow with Docker context.

## Files
- `assets/samples/README.md` (641 bytes)
- `assets/samples/advanced_index_actions/advanced_index_actions_sample.py` (3392 bytes)
- `assets/samples/aws/README.md` (578 bytes)
- `assets/samples/aws/search_requests.py` (2501 bytes)
- `assets/samples/aws/search_urllib3_async.py` (2693 bytes)
- `assets/samples/aws/search_urllib3_sync.py` (2494 bytes)
- `assets/samples/bulk/bulk_array.py` (1797 bytes)
- `assets/samples/bulk/bulk_helpers.py` (3043 bytes)
- `assets/samples/bulk/bulk_ld.py` (1817 bytes)
- `assets/samples/document_lifecycle/document_lifecycle_sample.py` (3052 bytes)
- `assets/samples/hello/hello.py` (2037 bytes)
- `assets/samples/hello/hello_async.py` (2747 bytes)
- `assets/samples/hello/unicode.py` (1689 bytes)
- `assets/samples/hello/unicode_async.py` (2000 bytes)
- `assets/samples/index_template/index_template_sample.py` (5121 bytes)
- `assets/samples/json/json_hello.py` (1840 bytes)
- `assets/samples/json/json_hello_async.py` (2378 bytes)
- `assets/samples/knn/knn_async_basics.py` (2511 bytes)
- `assets/samples/knn/knn_basics.py` (2187 bytes)
- `assets/samples/knn/knn_boolean_filter.py` (2541 bytes)
- `assets/samples/knn/knn_efficient_filter.py` (4902 bytes)
- `assets/samples/logging/log_collection_sample.py` (4323 bytes)
- `assets/samples/poetry.toml` (27 bytes)
- `assets/samples/pyproject.toml` (1046 bytes)
- `assets/samples/search/search_after_async.py` (3162 bytes)
- `assets/samples/search/search_after_sync.py` (3039 bytes)
- `assets/samples/security/roles.py` (1486 bytes)
- `assets/samples/security/users.py` (1242 bytes)
- `assets/samples/snapshot/Dockerfile` (297 bytes)
- `assets/samples/snapshot/README.md` (217 bytes)
- `assets/samples/snapshot/snapshot_sample.py` (1925 bytes)
