# opensearch-py Examples

Local examples for common `opensearch-py` tasks. Use these patterns alongside
the API snapshot files in this directory.

## Sync Client With TLS

```python
from opensearchpy import OpenSearch


client = OpenSearch(
    hosts=[{"host": "search.example.com", "port": 9200}],
    http_auth=("admin", "secret"),
    use_ssl=True,
    verify_certs=True,
    ca_certs="/etc/ssl/certs/ca-bundle.crt",
    timeout=30,
    max_retries=3,
    retry_on_timeout=True,
)
```

## Local Development Client

```python
from opensearchpy import OpenSearch


client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=False,
    ssl_show_warn=False,
)
```

## Amazon OpenSearch Service SigV4

```python
import boto3
from opensearchpy import AWSV4SignerAuth, OpenSearch, RequestsHttpConnection


region = "us-east-1"
host = "search-domain.us-east-1.es.amazonaws.com"
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region)

client = OpenSearch(
    hosts=[{"host": host, "port": 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
    pool_maxsize=20,
)
```

## Create Index And Search

```python
from opensearchpy import OpenSearch
from opensearchpy.exceptions import NotFoundError, RequestError


client = OpenSearch(hosts=[{"host": "localhost", "port": 9200}])

mapping = {
    "settings": {"index": {"number_of_shards": 1, "number_of_replicas": 0}},
    "mappings": {
        "properties": {
            "customer_id": {"type": "keyword"},
            "status": {"type": "keyword"},
            "total": {"type": "double"},
            "created_at": {"type": "date"},
        }
    },
}

try:
    client.indices.create(index="orders", body=mapping)
except RequestError as exc:
    if getattr(exc, "error", "") != "resource_already_exists_exception":
        raise

client.index(index="orders", id="order-1", body={"customer_id": "c1", "status": "paid", "total": 42.5})
client.indices.refresh(index="orders")

response = client.search(
    index="orders",
    body={
        "query": {"bool": {"filter": [{"term": {"status": "paid"}}]}},
        "sort": [{"created_at": {"order": "desc"}}],
    },
)
hits = [hit["_source"] for hit in response["hits"]["hits"]]
```

## Bulk Indexing

```python
from opensearchpy import OpenSearch, helpers


client = OpenSearch(hosts=[{"host": "localhost", "port": 9200}])

actions = (
    {
        "_op_type": "index",
        "_index": "orders",
        "_id": row["id"],
        "_source": row,
    }
    for row in rows
)

success_count, errors = helpers.bulk(
    client,
    actions,
    chunk_size=500,
    request_timeout=60,
    raise_on_error=False,
)
```

## Streaming Bulk With Per-Item Handling

```python
from opensearchpy import OpenSearch, helpers


client = OpenSearch(hosts=[{"host": "localhost", "port": 9200}])

for ok, item in helpers.streaming_bulk(client, actions, chunk_size=500, max_retries=3):
    if not ok:
        logger.warning("bulk item failed: %s", item)
```

## Scan All Matching Documents

```python
from opensearchpy import OpenSearch, helpers


client = OpenSearch(hosts=[{"host": "localhost", "port": 9200}])

for hit in helpers.scan(
    client,
    index="orders",
    query={"query": {"range": {"created_at": {"gte": "now-7d"}}}},
    size=1000,
    preserve_order=False,
):
    process(hit["_id"], hit["_source"])
```

## Async Client

Requires `opensearch-py[async]`.

```python
import asyncio
from opensearchpy import AsyncOpenSearch


async def run() -> None:
    client = AsyncOpenSearch(hosts=[{"host": "localhost", "port": 9200}])
    try:
        await client.index(index="orders", id="1", body={"status": "paid"})
        response = await client.search(index="orders", body={"query": {"match_all": {}}})
        print(response["hits"]["total"])
    finally:
        await client.close()


asyncio.run(run())
```

## DSL Search

```python
from opensearchpy import OpenSearch, Q, Search


client = OpenSearch(hosts=[{"host": "localhost", "port": 9200}])

search = (
    Search(using=client, index="orders")
    .query(Q("term", status="paid"))
    .filter("range", total={"gte": 10})
    .sort("-created_at")
    [:25]
)

response = search.execute()
for hit in response:
    print(hit.meta.id, hit.status, hit.total)
```

## Document And Index DSL

```python
from opensearchpy import Date, Document, Keyword, OpenSearch, Text


class Order(Document):
    customer_id = Keyword()
    status = Keyword()
    description = Text()
    created_at = Date()

    class Index:
        name = "orders"


client = OpenSearch(hosts=[{"host": "localhost", "port": 9200}])
Order.init(using=client)

order = Order(meta={"id": "order-1"}, customer_id="c1", status="paid")
order.save(using=client)
```

## Unit Testing Query Code

```python
from unittest.mock import Mock


def find_paid_orders(client):
    return client.search(index="orders", body={"query": {"term": {"status": "paid"}}})


def test_find_paid_orders_builds_expected_query():
    client = Mock()
    client.search.return_value = {"hits": {"hits": []}}

    find_paid_orders(client)

    client.search.assert_called_once_with(
        index="orders",
        body={"query": {"term": {"status": "paid"}}},
    )
```
