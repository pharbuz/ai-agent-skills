# Clients Core

> Local snapshot generated from OpenSearch Python Client API Reference on 2026-07-27. Use this file instead of browsing the live documentation during skill execution.


## Source: `api-ref/client.html`

## Clients

- OpenSearch Client

### Clients within Opensearch

OpenSearch Client includes several clients:

- Http Client
- Compact and aligned text (CAT) Client
- Cluster Client
- Dangling Indices Client
- Ingest Client
- Indices Client
- Nodes Client
- Remote Client
- Security Client
- Snapshot Client
- Tasks Client
- Features Client


## Source: `api-ref/clients/opensearch_client.html`

## OpenSearch Client

### `class opensearchpy.OpenSearch(hosts=None, transport_class=<class 'opensearchpy.transport.Transport'>, **kwargs)`

Bases: Client

OpenSearch client. Provides a straightforward mapping from Python to OpenSearch REST endpoints.

The instance has attributes cat, cluster, indices, ingest, nodes, snapshot and tasks that provide access to instances of CatClient, ClusterClient, IndicesClient, IngestClient, NodesClient, SnapshotClient and TasksClient respectively. This is the preferred (and only supported) way to get access to those classes and their methods.

You can specify your own connection class which should be used by providing the connection_class parameter:

```python
# create connection to localhost using the ThriftConnection
client = OpenSearch(connection_class=ThriftConnection)
```

If you want to turn on sniffing you have several options (described in Transport):

```python
# create connection that will automatically inspect the cluster to get
# the list of active nodes. Start with nodes running on
# 'opensearchnode1' and 'opensearchnode2'
client = OpenSearch(
    ['opensearchnode1', 'opensearchnode2'],
    # sniff before doing anything
    sniff_on_start=True,
    # refresh nodes after a node fails to respond
    sniff_on_connection_fail=True,
    # and also every 60 seconds
    sniffer_timeout=60
)
```

Different hosts can have different parameters, use a dictionary per node to specify those:

```python
# connect to localhost directly and another node using SSL on port 443
# and an url_prefix. Note that ``port`` needs to be an int.
client = OpenSearch([
    {'host': 'localhost'},
    {'host': 'othernode', 'port': 443, 'url_prefix': 'opensearch', 'use_ssl': True},
])
```

If using SSL, there are several parameters that control how we deal with certificates (see AIOHttpConnection for detailed description of the options):

```python
client = OpenSearch(
    ['localhost:443', 'other_host:443'],
    # turn on SSL
    use_ssl=True,
    # make sure we verify SSL certificates
    verify_certs=True,
    # provide a path to CA certs on disk
    ca_certs='/path/to/CA_certs'
)
```

If using SSL, but don’t verify the certs, a warning message is showed optionally (see AIOHttpConnection for detailed description of the options):

```python
client = OpenSearch(
    ['localhost:443', 'other_host:443'],
    # turn on SSL
    use_ssl=True,
    # no verify SSL certificates
    verify_certs=False,
    # don't verify the hostname in the certificate
    ssl_assert_hostname=False,
    # don't show warnings about ssl certs verification
    ssl_show_warn=False
)
```

SSL client authentication is supported (see AIOHttpConnection for detailed description of the options):

```python
client = OpenSearch(
    ['localhost:443', 'other_host:443'],
    # turn on SSL
    use_ssl=True,
    # make sure we verify SSL certificates
    verify_certs=True,
    # provide a path to CA certs on disk
    ca_certs='/path/to/CA_certs',
    # PEM formatted SSL client certificate
    client_cert='/path/to/clientcert.pem',
    # PEM formatted SSL client key
    client_key='/path/to/clientkey.pem'
)
```

Alternatively you can use RFC-1738 formatted URLs, as long as they are not in conflict with other options:

```python
client = OpenSearch(
    [
        'http://user:secret@localhost:9200/',
        'https://user:secret@other_host:443/production'
    ],
    verify_certs=True
)
```

By default, JSONSerializer is used to encode all outgoing requests. However, you can implement your own custom serializer:

```python
from opensearchpy.serializer import JSONSerializer

class SetEncoder(JSONSerializer):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, Something):
            return 'CustomSomethingRepresentation'
        return JSONSerializer.default(self, obj)

client = OpenSearch(serializer=SetEncoder())
```

### `Parameters:`

-
hosts (Any) – list of nodes, or a single node, we should connect to. Node should be a dictionary ({“host”: “localhost”, “port”: 9200}), the entire dictionary will be passed to the Connection class as kwargs, or a string in the format of host[:port] which will be translated to a dictionary automatically. If no value is given the Connection class defaults will be used.

-
transport_class (Type[Transport]) – Transport subclass to use.

-
kwargs (Any) – any additional arguments will be passed on to the Transport class and, subsequently, to the Connection instances.

-
hosts

-
transport_class

-
kwargs

### `__repr__()`

Return repr(self).

### `Return type:`

Any

### `bulk(*, body, index=None, params=None, headers=None)`

Allows to perform multiple index/update/delete operations in a single request.

### `Parameters:`

-
body (Any) – The operation definition and data (action-data pairs), separated by newlines

-
index (Any) – Name of the data stream, index, or index alias to perform bulk actions on.

-
_source – true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude from the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
require_alias – If true, the request’s actions must target an index alias. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period each action waits for the following operations: automatic index creation, dynamic mapping updates, waiting for active shards.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `bulk_stream(*, body, index=None, params=None, headers=None)`

Allows to perform multiple index/update/delete operations using request response streaming.

### `Parameters:`

-
body (Any) – The operation definition and data (action-data pairs), separated by newlines

-
index (Any) – Name of the data stream, index, or index alias to perform bulk actions on.

-
_source – true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude from the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
batch_interval – Specifies for how long bulk operations should be accumulated into a batch before sending the batch to data nodes.

-
batch_size – Specifies how many bulk operations should be accumulated into a batch before sending the batch to data nodes.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
require_alias – If true, the request’s actions must target an index alias. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period each action waits for the following operations: automatic index creation, dynamic mapping updates, waiting for active shards.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `clear_scroll(*, body=None, scroll_id=None, params=None, headers=None)`

Explicitly clears the search context for a scroll.

### `Parameters:`

-
body (Any) – A comma-separated list of scroll IDs to clear if none was specified using the scroll_id parameter

-
scroll_id (Any) – A comma-separated list of scroll IDs to clear. To clear all scroll IDs, use _all.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
scroll_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `close()`

Closes the Transport and all internal connections

### `Return type:`

None

### `count(*, body=None, index=None, params=None, headers=None)`

Returns number of documents matching a query.

### `Parameters:`

-
body (Any) – Query to restrict the results specified with the Query DSL (optional)

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. This parameter can only be used when the q query string parameter is specified. Default is false.

-
analyzer – Analyzer to use for the query string. This parameter can only be used when the q query string parameter is specified.

-
default_operator – The default operator for query string query: AND or OR. This parameter can only be used when the q query string parameter is specified. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string. This parameter can only be used when the q query string parameter is specified.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Specifies the type of index that wildcard expressions can match. Supports comma-separated values. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_throttled – If true, concrete, expanded or aliased indexes are ignored when frozen.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
min_score – Sets the minimum _score value that documents must have to be included in the result.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
terminate_after – Maximum number of documents to collect for each shard. If a query reaches this limit, OpenSearch terminates the query early. OpenSearch collects documents before sorting.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create(*, index, id, body, params=None, headers=None)`

Creates a new document in the index. Returns a 409 response when a document with a same ID already exists in the index.

### `Parameters:`

-
index (Any) – Name of the data stream or index to target. If the target doesn’t exist and matches the name or wildcard (*) pattern of an index template with a data_stream definition, this request creates the data stream. If the target doesn’t exist and doesn’t match a data stream template, this request creates the index.

-
id (Any) – The unique identifier for the document.

-
body (Any) – The document

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period the request waits for the following operations: automatic index creation, dynamic mapping updates, waiting for active shards.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
index

-
id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_pit(*, index, params=None, headers=None)`

Creates point in time context.

### `Parameters:`

-
index (Any) – A comma-separated list of indexes; use _all or empty string to perform the operation on all indexes.

-
allow_partial_pit_creation – Allow if point in time can be created with partial failures.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Whether to expand wildcard expression to concrete indexes that are open, closed or both. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
keep_alive – Specify the keep alive for point in time.

-
preference – Specify the node or shard the operation should be performed on. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
routing – A comma-separated list of specific routing values.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete(*, index, id, params=None, headers=None)`

Removes a document from the index.

### `Parameters:`

-
index (Any) – Name of the target index.

-
id (Any) – The unique identifier for the document.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
if_primary_term – Only perform the operation if the document has this primary term.

-
if_seq_no – Only perform the operation if the document has this sequence number.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for active shards.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_all_pits(*, params=None, headers=None)`

Deletes all active point in time searches.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_by_query(*, index, body, params=None, headers=None)`

Deletes documents matching the provided query.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams or indexes, omit this parameter or use * or _all.

-
body (Any) – The search definition using the Query DSL

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – List of fields to exclude from the returned _source field.

-
_source_includes – List of fields to extract and return from the _source field.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. Default is false.

-
analyzer – Analyzer to use for the query string.

-
conflicts – What to do if delete by query hits version conflicts: abort or proceed. Valid choices are abort, proceed.

-
default_operator – The default operator for query string query: AND or OR. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
from – Starting offset. Default is 0.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
max_docs – Maximum number of documents to process. Defaults to all documents.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
refresh – If true, OpenSearch refreshes all shards involved in the delete by query after the request completes. Valid choices are false, true, wait_for.

-
request_cache – If true, the request cache is used for this request. Defaults to the index-level setting.

-
requests_per_second – The throttle for this request in sub- requests per second. Default is 0.

-
routing – A custom value used to route operations to a specific shard.

-
scroll – Period to retain the search context for scrolling.

-
scroll_size – Size of the scroll request that powers the operation. Default is 100.

-
search_timeout – Explicit timeout for each search request. Defaults to no timeout.

-
search_type – The type of the search operation. Available options: query_then_fetch, dfs_query_then_fetch. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
size – Deprecated, use max_docs instead.

-
slices – The number of slices this task should be divided into.

-
sort – A comma-separated list of <field>:<direction> pairs.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stats – Specific tag of the request for logging and statistical purposes.

-
terminate_after – Maximum number of documents to collect for each shard. If a query reaches this limit, OpenSearch terminates the query early. OpenSearch collects documents before sorting. Use with caution. OpenSearch applies this parameter to each shard handling the request. When possible, let OpenSearch perform early termination automatically. Avoid specifying this parameter for requests that target data streams with backing indexes across multiple data tiers.

-
timeout – Period each deletion request waits for active shards.

-
version – If true, returns the document version as part of a hit.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – If true, the request blocks until the operation is complete. Default is True.

-
index

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_by_query_rethrottle(*, task_id, params=None, headers=None)`

Changes the number of requests per second for a particular Delete By Query operation.

### `Parameters:`

-
task_id (Any) – The ID for the task.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
requests_per_second – The throttle for this request in sub- requests per second.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
task_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_pit(*, body=None, params=None, headers=None)`

Deletes one or more point in time searches based on the IDs passed.

### `Parameters:`

-
body (Any) – The point-in-time ids to be deleted

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_script(*, id, params=None, headers=None)`

Deletes a script.

### `Parameters:`

-
id (Any) – Identifier for the stored script or search template.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `exists(*, index, id, params=None, headers=None)`

Returns information about whether a document exists in an index.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases. Supports wildcards (*).

-
id (Any) – Identifier of the document.

-
_source – true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude in the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time.

-
refresh – If true, OpenSearch refreshes all shards involved in the delete by query after the request completes. Valid choices are false, true, wait_for.

-
routing – Target the specified primary shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stored_fields – List of stored fields to return as part of a hit. If no fields are specified, no stored fields are included in the response. If this field is specified, the _source parameter defaults to false.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `exists_source(*, index, id, params=None, headers=None)`

Returns information about whether a document source exists in an index.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases. Supports wildcards (*).

-
id (Any) – Identifier of the document.

-
_source – true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude in the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time.

-
refresh – If true, OpenSearch refreshes all shards involved in the delete by query after the request completes. Valid choices are false, true, wait_for.

-
routing – Target the specified primary shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `explain(*, index, id, body=None, params=None, headers=None)`

Returns information about why a specific document matches (or doesn’t match) a query.

### `Parameters:`

-
index (Any) – Index names used to limit the request. Only a single index name can be provided to this parameter.

-
id (Any) – Defines the document ID.

-
body (Any) – The query definition using the Query DSL

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude from the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. Default is false.

-
analyzer – Analyzer to use for the query string. This parameter can only be used when the q query string parameter is specified.

-
default_operator – The default operator for query string query: AND or OR. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string. Default is _all.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stored_fields – A comma-separated list of stored fields to return in the response.

-
index

-
id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `field_caps(*, body=None, index=None, params=None, headers=None)`

Returns the information about the capabilities of fields among multiple indexes.

### `Parameters:`

-
body (Any) – An index filter specified with the Query DSL

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – The type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma-separated values, such as open,hidden. Valid choices are all, closed, hidden, none, open.

-
fields – A comma-separated list of fields to retrieve capabilities for. Wildcard (*) expressions are supported.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If true, missing or closed indexes are not included in the response.

-
include_unmapped – If true, unmapped fields are included in the response. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get(*, index, id, params=None, headers=None)`

Returns a document.

### `Parameters:`

-
index (Any) – The name of the index containing the document.

-
id (Any) – The unique identifier of the document.

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude in the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search. If false, do nothing with refreshes. Valid choices are false, true, wait_for.

-
routing – Target the specified primary shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stored_fields – List of stored fields to return as part of a hit. If no fields are specified, no stored fields are included in the response. If this field is specified, the _source parameter defaults to false.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: internal, external, external_gte. Valid choices are external, external_gte, internal.

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_all_pits(*, params=None, headers=None)`

Lists all active point in time searches.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_script(*, id, params=None, headers=None)`

Returns a script.

### `Parameters:`

-
id (Any) – Identifier for the stored script or search template.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Specify timeout for connection to master

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_script_context(*, params=None, headers=None)`

Returns all script contexts.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_script_languages(*, params=None, headers=None)`

Returns available script types, languages and contexts.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_source(*, index, id, params=None, headers=None)`

Returns the source of a document.

### `Parameters:`

-
index (Any) – The name of the index containing the document.

-
id (Any) – The unique identifier of the document.

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude in the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – Boolean) If true, the request is real time as opposed to near real time.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search. If false, do nothing with refreshes. Valid choices are false, true, wait_for.

-
routing – Target the specified primary shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type. One of internal, external, external_gte. Valid choices are external, external_gte, internal.

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `index(*, index, body, id=None, params=None, headers=None)`

Creates or updates a document in an index.

### `Parameters:`

-
index (Any) – Name of the data stream or index to target.

-
body (Any) – The document

-
id (Any) – The unique identifier for the document.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
if_primary_term – Only perform the operation if the document has this primary term.

-
if_seq_no – Only perform the operation if the document has this sequence number.

-
op_type – Set to create to only index the document if it does not already exist (put if absent). If a document with the specified _id already exists, the indexing operation will fail. Same as using the <index>/_create endpoint. Valid values: index, create. If document id is specified, it defaults to index. Otherwise, it defaults to create.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
require_alias – If true, the destination must be an index alias. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period the request waits for the following operations: automatic index creation, dynamic mapping updates, waiting for active shards.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
index

-
body

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `info(*, params=None, headers=None)`

Returns basic information about the cluster.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `mget(*, body, index=None, params=None, headers=None)`

Allows to get multiple documents in one request.

### `Parameters:`

-
body (Any) – Document identifiers; can be either docs (containing full document information) or ids (when index is provided in the URL.

-
index (Any) – The name of the index to retrieve documents from when ids are specified, or when a document in the docs array does not specify an index.

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude from the response. You can also use this parameter to exclude fields from the subset specified in _source_includes query parameter.

-
_source_includes – A comma-separated list of source fields to include in the response. If this parameter is specified, only these source fields are returned. You can exclude fields from this subset using the _source_excludes query parameter. If the _source parameter is false, this parameter is ignored.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time.

-
refresh – If true, the request refreshes relevant shards before retrieving documents. Valid choices are false, true, wait_for.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stored_fields – If true, retrieves the document fields stored in the index rather than the document _source.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `msearch(*, body, index=None, params=None, headers=None)`

Allows to execute several search operations in one request.

### `Parameters:`

-
body (Any) – The request definitions (metadata-search request definition pairs), separated by newlines

-
index (Any) – A comma-separated list of data streams, indexes, and index aliases to search.

-
ccs_minimize_roundtrips – If true, network round-trips between the coordinating node and remote clusters are minimized for cross-cluster search requests. Default is True.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
max_concurrent_searches – Maximum number of concurrent searches the multi search API can execute.

-
max_concurrent_shard_requests – Maximum number of concurrent shard requests that each sub-search request executes per node. Default is 5.

-
pre_filter_shard_size – Defines a threshold that enforces a pre-filter roundtrip to prefilter search shards based on query rewriting if the number of shards the search request expands to exceeds the threshold. This filter roundtrip can limit the number of shards significantly if for instance a shard can not match any documents based on its rewrite method i.e., if date filters are mandatory to match but the shard bounds and the query are disjoint.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
rest_total_hits_as_int – If true, hits.total are returned as an integer in the response. Defaults to false, which returns an object. Default is false.

-
search_type – Indicates whether global term and document frequencies should be used when scoring returned documents. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
typed_keys – Specifies whether aggregation and suggester names should be prefixed by their respective types in the response.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `msearch_template(*, body, index=None, params=None, headers=None)`

Allows to execute several search template operations in one request.

### `Parameters:`

-
body (Any) – The request definitions (metadata-search request definition pairs), separated by newlines

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams and indexes, omit this parameter or use *.

-
ccs_minimize_roundtrips – If true, network round-trips are minimized for cross-cluster search requests. Default is True.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
max_concurrent_searches – Maximum number of concurrent searches the API can run.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
rest_total_hits_as_int – If true, the response returns hits.total as an integer. If false, it returns hits.total as an object. Default is false.

-
search_type – The type of the search operation. Available options: query_then_fetch, dfs_query_then_fetch. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
typed_keys – If true, the response prefixes aggregation and suggester names with their respective types.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `mtermvectors(*, body=None, index=None, params=None, headers=None)`

Returns multiple termvectors in one request.

### `Parameters:`

-
body (Any) – Define ids, documents, parameters or a list of parameters per document here. You must at least provide a list of document ids. See documentation.

-
index (Any) – The name of the index that contains the document.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
field_statistics – If true, the response includes the document count, sum of document frequencies, and sum of total term frequencies. Default is True.

-
fields – A comma-separated list or a wildcard expression specifying the fields to include in the statistics. Used as the default list unless a specific field list is provided in the completion_fields or fielddata_fields parameters.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ids – A comma-separated list of documents IDs. You must provide either the docs field in the request body or specify ids as a query parameter or in the request body.

-
offsets – If true, the response includes term offsets. Default is True.

-
payloads – If true, the response includes term payloads. Default is True.

-
positions – If true, the response includes term positions. Default is True.

-
preference – Specifies the node or shard on which the operation should be performed. See [preference query parameter]({{site.url}}{{site.baseurl}}/api-reference/search- apis/search/#the-preference-query-parameter) for a list of available options. By default the requests are routed randomly to available shard copies (primary or replica), with no guarantee of consistency across repeated queries.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time. Default is True.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
term_statistics – If true, the response includes term frequency and document frequency. Default is false.

-
version – If true, returns the document version as part of a hit.

-
version_type – The specific version type. Valid choices are external, external_gte, internal.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `ping(*, params=None, headers=None)`

Returns whether the cluster is running.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_script(*, id, body, context=None, params=None, headers=None)`

Creates or updates a script.

### `Parameters:`

-
id (Any) – Identifier for the stored script or search template. Must be unique within the cluster.

-
body (Any) – The document

-
context (Any) – Context in which the script or search template should run. To prevent errors, the API immediately compiles the script or template in this context.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
id

-
body

-
context

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `rank_eval(*, body, index=None, params=None, headers=None)`

Allows to evaluate the quality of ranked search results over a set of typical search queries.

### `Parameters:`

-
body (Any) – The ranking evaluation search definition, including search requests, document ratings and ranking metric definition.

-
index (Any) – A comma-separated list of data streams, indexes, and index aliases used to limit the request. Wildcard (*) expressions are supported. To target all data streams and indexes in a cluster, omit this parameter or use _all or *.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Whether to expand wildcard expression to concrete indexes that are open, closed or both. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If true, missing or closed indexes are not included in the response.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
search_type – Search operation type Valid choices are dfs_query_then_fetch, query_then_fetch.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `reindex(*, body, params=None, headers=None)`

Allows to copy documents from one index to another, optionally filtering the source documents by a query, changing the destination index settings, or fetching the documents from a remote cluster.

### `Parameters:`

-
body (Any) – The search definition using the Query DSL and the prototype for the index request.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
max_docs – Maximum number of documents to process. By default, all documents.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, the request refreshes affected shards to make this operation visible to search. Valid choices are false, true, wait_for.

-
requests_per_second – The throttle for this request in sub- requests per second. Defaults to no throttle. Default is 0.

-
scroll – Specifies how long a consistent view of the index should be maintained for scrolled search.

-
slices – The number of slices this task should be divided into. Defaults to 1 slice, meaning the task isn’t sliced into subtasks.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period each indexing waits for automatic index creation, dynamic mapping updates, and waiting for active shards.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – If true, the request blocks until the operation is complete. Default is True.

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `reindex_rethrottle(*, task_id, params=None, headers=None)`

Changes the number of requests per second for a particular reindex operation.

### `Parameters:`

-
task_id (Any) – Identifier for the task.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
requests_per_second – The throttle for this request in sub- requests per second.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
task_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `render_search_template(*, body=None, id=None, params=None, headers=None)`

Allows to use the Mustache language to pre-render a search definition.

### `Parameters:`

-
body (Any) – The search definition template and its parameters.

-
id (Any) – ID of the search template to render. If no source is specified, this or the id request body parameter is required.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `scripts_painless_execute(*, body=None, params=None, headers=None)`

Allows an arbitrary script to be executed and a result to be returned.

### `Parameters:`

-
body (Any) – The script to execute

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `scroll(*, body=None, scroll_id=None, params=None, headers=None)`

Allows to retrieve a large numbers of results from a single search request.

### `Parameters:`

-
scroll_id (Any) – The scroll ID for scrolled search

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
rest_total_hits_as_int – If true, the API response’s hit.total property is returned as an integer. If false, the API response’s hit.total property is returned as an object. Default is false.

-
scroll – Period to retain the search context for scrolling.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body (Any)

-
scroll_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search(*, body=None, index=None, params=None, headers=None)`

Returns results matching a query.

### `Parameters:`

-
body (Any) – The search definition using the Query DSL

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams and indexes, omit this parameter or use * or _all.

-
_source – Indicates which source fields are returned for matching documents. These fields are returned in the hits._source property of the search response. Valid values are: true to return the entire document source; false to not return the document source; <string> to return the source fields that are specified as a comma- separated list (supports wildcard (*) patterns).

-
_source_excludes – A comma-separated list of source fields to exclude from the response. You can also use this parameter to exclude fields from the subset specified in _source_includes query parameter. If the _source parameter is false, this parameter is ignored.

-
_source_includes – A comma-separated list of source fields to include in the response. If this parameter is specified, only these source fields are returned. You can exclude fields from this subset using the _source_excludes query parameter. If the _source parameter is false, this parameter is ignored.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
allow_partial_search_results – If true, returns partial results if there are shard request timeouts or shard failures. If false, returns an error with no partial results. Default is True.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. This parameter can only be used when the q query string parameter is specified. Default is false.

-
analyzer – Analyzer to use for the query string. This parameter can only be used when the q query string parameter is specified.

-
batched_reduce_size – The number of shard results that should be reduced at once on the coordinating node. This value should be used as a protection mechanism to reduce the memory overhead per search request if the potential number of shards in the request can be large. Default is 512.

-
cancel_after_time_interval – The time after which the search request will be canceled. Request-level parameter takes precedence over cancel_after_time_interval cluster setting.

-
ccs_minimize_roundtrips – If true, network round-trips between the coordinating node and the remote clusters are minimized when executing cross-cluster search (CCS) requests. Default is True.

-
default_operator – The default operator for query string query: AND or OR. This parameter can only be used when the q query string parameter is specified. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string. This parameter can only be used when the q query string parameter is specified.

-
docvalue_fields – A comma-separated list of fields to return as the docvalue representation for each hit.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid choices are all, closed, hidden, none, open.

-
explain – If true, returns detailed information about score computation as part of a hit.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
from – Starting document offset. Needs to be non-negative. By default, you cannot page through more than 10,000 hits using the from and size parameters. To page through more hits, use the search_after parameter. Default is 0.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_throttled – If true, concrete, expanded or aliased indexes will be ignored when frozen.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
include_named_queries_score – Indicates whether hit.matched_queries should be rendered as a map that includes the name of the matched query associated with its score (true) or as an array containing the name of the matched queries (false) Default is false.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored. This parameter can only be used when the q query string parameter is specified.

-
max_concurrent_shard_requests – Defines the number of concurrent shard requests per node this search executes concurrently. This value should be used to limit the impact of the search on the cluster in order to limit the number of concurrent shard requests. Default is 5.

-
phase_took – Indicates whether to return phase-level took time values in the response. Default is false.

-
pre_filter_shard_size – Defines a threshold that enforces a pre-filter roundtrip to prefilter search shards based on query rewriting if the number of shards the search request expands to exceeds the threshold. This filter roundtrip can limit the number of shards significantly if for instance a shard can not match any documents based on its rewrite method (if date filters are mandatory to match but the shard bounds and the query are disjoint). When unspecified, the pre- filter phase is executed if any of these conditions is met: the request targets more than 128 shards; the request targets one or more read-only index; the primary sort of the query targets an indexed field.

-
preference – Nodes and shards used for the search. By default, OpenSearch selects from eligible nodes and shards using adaptive replica selection, accounting for allocation awareness. Valid values are: _only_local to run the search only on shards on the local node; _local to, if possible, run the search on shards on the local node, or if not, select shards using the default method; _only_nodes:<node-id>,<node-id> to run the search on only the specified nodes IDs, where, if suitable shards exist on more than one selected node, use shards on those nodes using the default method, or if none of the specified nodes are available, select shards from any available node using the default method; _prefer_nodes:<node-id>,<node- id> to if possible, run the search on the specified nodes IDs, or if not, select shards using the default method; _shards:<shard>,<shard> to run the search only on the specified shards; <custom-string> (any string that does not start with _) to route searches with the same <custom-string> to the same shards in the same order. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax using query parameter search. Query parameter searches do not support the full OpenSearch Query DSL but are handy for testing.

-
request_cache – If true, the caching of search results is enabled for requests where size is 0. Defaults to index level settings.

-
rest_total_hits_as_int – Indicates whether hits.total should be rendered as an integer or an object in the rest search response. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
scroll – Period to retain the search context for scrolling. See Scroll search results. By default, this value cannot exceed 1d (24 hours). You can change this limit using the search.max_keep_alive cluster-level setting.

-
search_pipeline – Customizable sequence of processing stages applied to search queries.

-
search_type – How distributed term frequencies are calculated for relevance scoring. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
seq_no_primary_term – If true, returns sequence number and primary term of the last modification of each hit.

-
size – Defines the number of hits to return. By default, you cannot page through more than 10,000 hits using the from and size parameters. To page through more hits, use the search_after parameter. Default is 10.

-
sort – A comma-separated list of <field>:<direction> pairs.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stats – Specific tag of the request for logging and statistical purposes.

-
stored_fields – A comma-separated list of stored fields to return as part of a hit. If no fields are specified, no stored fields are included in the response. If this field is specified, the _source parameter defaults to false. You can pass _source: true to return both source fields and stored fields in the search response.

-
suggest_field – Specifies which field to use for suggestions.

-
suggest_mode – Specifies the suggest mode. This parameter can only be used when the suggest_field and suggest_text query string parameters are specified. Valid choices are always, missing, popular.

-
suggest_size – Number of suggestions to return. This parameter can only be used when the suggest_field and suggest_text query string parameters are specified.

-
suggest_text – The source text for which the suggestions should be returned. This parameter can only be used when the suggest_field and suggest_text query string parameters are specified.

-
terminate_after – Maximum number of documents to collect for each shard. If a query reaches this limit, OpenSearch terminates the query early. OpenSearch collects documents before sorting. Use with caution. OpenSearch applies this parameter to each shard handling the request. When possible, let OpenSearch perform early termination automatically. Avoid specifying this parameter for requests that target data streams with backing indexes across multiple data tiers. If set to 0 (default), the query does not terminate early.

-
timeout – Specifies the period of time to wait for a response from each shard. If no response is received before the timeout expires, the request fails and returns an error.

-
track_scores – If true, calculate and return document scores, even if the scores are not used for sorting.

-
track_total_hits – Number of hits matching the query to count accurately. If true, the exact number of hits is returned at the cost of some performance. If false, the response does not include the total number of hits matching the query.

-
typed_keys – If true, aggregation and suggester names are be prefixed by their respective types in the response.

-
verbose_pipeline – Enables or disables verbose mode for the search pipeline. When verbose mode is enabled, detailed information about each processor in the search pipeline is included in the search response. This includes the processor name, execution status, input, output, and time taken for processing. This parameter is primarily intended for debugging purposes, allowing users to track how data flows and transforms through the search pipeline.

-
version – If true, returns document version as part of a hit.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search_shards(*, body=None, index=None, params=None, headers=None)`

Returns information about the indexes and shards that a search request would be executed against.

### `Parameters:`

-
index (Any) – Returns the indexes and shards that a search request would be executed against.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
local – If true, the request retrieves information from the local node only. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body (Any)

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search_template(*, body, index=None, params=None, headers=None)`

Allows to use the Mustache language to pre-render a search definition.

### `Parameters:`

-
body (Any) – The search definition template and its parameters.

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*).

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
ccs_minimize_roundtrips – If true, network round-trips are minimized for cross-cluster search requests. Default is True.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
explain – If true, the response includes additional details about score computation as part of a hit.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_throttled – If true, specified concrete, expanded, or aliased indexes are not included in the response when throttled.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
phase_took – Indicates whether to return phase-level took time values in the response. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
profile – If true, the query execution is profiled.

-
rest_total_hits_as_int – If true, hits.total are rendered as an integer in the response. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
scroll – Specifies how long a consistent view of the index should be maintained for scrolled search.

-
search_pipeline – Customizable sequence of processing stages applied to search queries.

-
search_type – The type of the search operation. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
typed_keys – If true, the response prefixes aggregation and suggester names with their respective types.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `termvectors(*, index, body=None, id=None, params=None, headers=None)`

Returns information and statistics about terms in the fields of a particular document.

### `Parameters:`

-
index (Any) – The name of the index containing the document.

-
body (Any) – Define parameters and or supply a document to get termvectors for. See documentation.

-
id (Any) – The unique identifier of the document.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
field_statistics – If true, the response includes the document count, sum of document frequencies, and sum of total term frequencies. Default is True.

-
fields – A comma-separated list or a wildcard expression specifying the fields to include in the statistics. Used as the default list unless a specific field list is provided in the completion_fields or fielddata_fields parameters.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
offsets – If true, the response includes term offsets. Default is True.

-
payloads – If true, the response includes term payloads. Default is True.

-
positions – If true, the response includes term positions. Default is True.

-
preference – Specifies the node or shard on which the operation should be performed. See [preference query parameter]({{site.url}}{{site.baseurl}}/api-reference/search- apis/search/#the-preference-query-parameter) for a list of available options. By default the requests are routed randomly to available shard copies (primary or replica), with no guarantee of consistency across repeated queries.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time. Default is True.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
term_statistics – If true, the response includes term frequency and document frequency. Default is false.

-
version – If true, returns the document version as part of a hit.

-
version_type – The specific version type. Valid choices are external, external_gte, internal.

-
index

-
body

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update(*, index, id, body, params=None, headers=None)`

Updates a document with a script or partial document.

### `Parameters:`

-
index (Any) – The name of the index

-
id (Any) – Document ID

-
body (Any) – The request definition requires either script or partial doc

-
_source – Set to false to disable source retrieval. You can also specify a comma-separated list of the fields you want to retrieve.

-
_source_excludes – Specify the source fields you want to exclude.

-
_source_includes – Specify the source fields you want to retrieve.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
if_primary_term – Only perform the operation if the document has this primary term.

-
if_seq_no – Only perform the operation if the document has this sequence number.

-
lang – The script language. Default is painless.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If ‘true’, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid choices are false, true, wait_for.

-
require_alias – If true, the destination must be an index alias. Default is false.

-
retry_on_conflict – Specify how many times should the operation be retried when a conflict occurs. Default is 0.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for dynamic mapping updates and active shards. This guarantees OpenSearch waits for at least the timeout before failing. The actual wait time could be longer, particularly when multiple waits occur.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operations. Set to ‘all’ or any positive integer up to the total number of shards in the index (number_of_replicas+1). Defaults to 1 meaning the primary shard.

-
index

-
id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_by_query(*, index, body=None, params=None, headers=None)`

Performs an update on every document in the index without changing the source, for example to pick up a mapping change.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams or indexes, omit this parameter or use * or _all.

-
body (Any) – The search definition using the Query DSL

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – List of fields to exclude from the returned _source field.

-
_source_includes – List of fields to extract and return from the _source field.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. Default is false.

-
analyzer – Analyzer to use for the query string.

-
conflicts – What to do if update by query hits version conflicts: abort or proceed. Valid choices are abort, proceed.

-
default_operator – The default operator for query string query: AND or OR. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
from – Starting offset. Default is 0.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
max_docs – Maximum number of documents to process. Defaults to all documents.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
refresh – If true, OpenSearch refreshes affected shards to make the operation visible to search. Valid choices are false, true, wait_for.

-
request_cache – If true, the request cache is used for this request.

-
requests_per_second – The throttle for this request in sub- requests per second. Default is 0.

-
routing – A custom value used to route operations to a specific shard.

-
scroll – Period to retain the search context for scrolling.

-
scroll_size – Size of the scroll request that powers the operation. Default is 100.

-
search_timeout – Explicit timeout for each search request.

-
search_type – The type of the search operation. Available options: query_then_fetch, dfs_query_then_fetch. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
size – Deprecated, use max_docs instead.

-
slices – The number of slices this task should be divided into.

-
sort – A comma-separated list of <field>:<direction> pairs.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stats – Specific tag of the request for logging and statistical purposes.

-
terminate_after – Maximum number of documents to collect for each shard. If a query reaches this limit, OpenSearch terminates the query early. OpenSearch collects documents before sorting. Use with caution. OpenSearch applies this parameter to each shard handling the request. When possible, let OpenSearch perform early termination automatically. Avoid specifying this parameter for requests that target data streams with backing indexes across multiple data tiers.

-
timeout – Period each update request waits for the following operations: dynamic mapping updates, waiting for active shards.

-
version – If true, returns the document version as part of a hit.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – If true, the request blocks until the operation is complete. Default is True.

-
index

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_by_query_rethrottle(*, task_id, params=None, headers=None)`

Changes the number of requests per second for a particular Update By Query operation.

### `Parameters:`

-
task_id (Any) – The ID for the task.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
requests_per_second – The throttle for this request in sub- requests per second.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
task_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `class opensearchpy.AsyncOpenSearch(hosts=None, transport_class=<class 'opensearchpy._async.transport.AsyncTransport'>, **kwargs)`

Bases: Client

OpenSearch client. Provides a straightforward mapping from Python to OpenSearch REST endpoints.

The instance has attributes cat, cluster, indices, ingest, nodes, snapshot and tasks that provide access to instances of CatClient, ClusterClient, IndicesClient, IngestClient, NodesClient, SnapshotClient and TasksClient respectively. This is the preferred (and only supported) way to get access to those classes and their methods.

You can specify your own connection class which should be used by providing the connection_class parameter:

```python
# create connection to localhost using the ThriftConnection
client = OpenSearch(connection_class=ThriftConnection)
```

If you want to turn on sniffing you have several options (described in Transport):

```python
# create connection that will automatically inspect the cluster to get
# the list of active nodes. Start with nodes running on
# 'opensearchnode1' and 'opensearchnode2'
client = OpenSearch(
    ['opensearchnode1', 'opensearchnode2'],
    # sniff before doing anything
    sniff_on_start=True,
    # refresh nodes after a node fails to respond
    sniff_on_connection_fail=True,
    # and also every 60 seconds
    sniffer_timeout=60
)
```

Different hosts can have different parameters, use a dictionary per node to specify those:

```python
# connect to localhost directly and another node using SSL on port 443
# and an url_prefix. Note that ``port`` needs to be an int.
client = OpenSearch([
    {'host': 'localhost'},
    {'host': 'othernode', 'port': 443, 'url_prefix': 'opensearch', 'use_ssl': True},
])
```

If using SSL, there are several parameters that control how we deal with certificates (see AIOHttpConnection for detailed description of the options):

```python
client = OpenSearch(
    ['localhost:443', 'other_host:443'],
    # turn on SSL
    use_ssl=True,
    # make sure we verify SSL certificates
    verify_certs=True,
    # provide a path to CA certs on disk
    ca_certs='/path/to/CA_certs'
)
```

If using SSL, but don’t verify the certs, a warning message is showed optionally (see AIOHttpConnection for detailed description of the options):

```python
client = OpenSearch(
    ['localhost:443', 'other_host:443'],
    # turn on SSL
    use_ssl=True,
    # no verify SSL certificates
    verify_certs=False,
    # don't verify the hostname in the certificate
    ssl_assert_hostname=False,
    # don't show warnings about ssl certs verification
    ssl_show_warn=False
)
```

SSL client authentication is supported (see AIOHttpConnection for detailed description of the options):

```python
client = OpenSearch(
    ['localhost:443', 'other_host:443'],
    # turn on SSL
    use_ssl=True,
    # make sure we verify SSL certificates
    verify_certs=True,
    # provide a path to CA certs on disk
    ca_certs='/path/to/CA_certs',
    # PEM formatted SSL client certificate
    client_cert='/path/to/clientcert.pem',
    # PEM formatted SSL client key
    client_key='/path/to/clientkey.pem'
)
```

Alternatively you can use RFC-1738 formatted URLs, as long as they are not in conflict with other options:

```python
client = OpenSearch(
    [
        'http://user:secret@localhost:9200/',
        'https://user:secret@other_host:443/production'
    ],
    verify_certs=True
)
```

By default, JSONSerializer is used to encode all outgoing requests. However, you can implement your own custom serializer:

```python
from opensearchpy.serializer import JSONSerializer

class SetEncoder(JSONSerializer):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, Something):
            return 'CustomSomethingRepresentation'
        return JSONSerializer.default(self, obj)

client = OpenSearch(serializer=SetEncoder())
```

### `Parameters:`

-
hosts (Any) – list of nodes, or a single node, we should connect to. Node should be a dictionary ({“host”: “localhost”, “port”: 9200}), the entire dictionary will be passed to the Connection class as kwargs, or a string in the format of host[:port] which will be translated to a dictionary automatically. If no value is given the Connection class defaults will be used.

-
transport_class (Type[AsyncTransport]) – Transport subclass to use.

-
kwargs (Any) – any additional arguments will be passed on to the Transport class and, subsequently, to the Connection instances.

-
hosts

-
transport_class

-
kwargs

### `__repr__()`

Return repr(self).

### `Return type:`

Any

### `bulk(*, body, index=None, params=None, headers=None)`

Allows to perform multiple index/update/delete operations in a single request.

### `Parameters:`

-
body (Any) – The operation definition and data (action-data pairs), separated by newlines

-
index (Any) – Name of the data stream, index, or index alias to perform bulk actions on.

-
_source – true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude from the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
require_alias – If true, the request’s actions must target an index alias. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period each action waits for the following operations: automatic index creation, dynamic mapping updates, waiting for active shards.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `bulk_stream(*, body, index=None, params=None, headers=None)`

Allows to perform multiple index/update/delete operations using request response streaming.

### `Parameters:`

-
body (Any) – The operation definition and data (action-data pairs), separated by newlines

-
index (Any) – Name of the data stream, index, or index alias to perform bulk actions on.

-
_source – true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude from the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
batch_interval – Specifies for how long bulk operations should be accumulated into a batch before sending the batch to data nodes.

-
batch_size – Specifies how many bulk operations should be accumulated into a batch before sending the batch to data nodes.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
require_alias – If true, the request’s actions must target an index alias. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period each action waits for the following operations: automatic index creation, dynamic mapping updates, waiting for active shards.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `clear_scroll(*, body=None, scroll_id=None, params=None, headers=None)`

Explicitly clears the search context for a scroll.

### `Parameters:`

-
body (Any) – A comma-separated list of scroll IDs to clear if none was specified using the scroll_id parameter

-
scroll_id (Any) – A comma-separated list of scroll IDs to clear. To clear all scroll IDs, use _all.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
scroll_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `asyncclose()`

Closes the Transport and all internal connections

### `Return type:`

None

### `count(*, body=None, index=None, params=None, headers=None)`

Returns number of documents matching a query.

### `Parameters:`

-
body (Any) – Query to restrict the results specified with the Query DSL (optional)

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. This parameter can only be used when the q query string parameter is specified. Default is false.

-
analyzer – Analyzer to use for the query string. This parameter can only be used when the q query string parameter is specified.

-
default_operator – The default operator for query string query: AND or OR. This parameter can only be used when the q query string parameter is specified. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string. This parameter can only be used when the q query string parameter is specified.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Specifies the type of index that wildcard expressions can match. Supports comma-separated values. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_throttled – If true, concrete, expanded or aliased indexes are ignored when frozen.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
min_score – Sets the minimum _score value that documents must have to be included in the result.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
terminate_after – Maximum number of documents to collect for each shard. If a query reaches this limit, OpenSearch terminates the query early. OpenSearch collects documents before sorting.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create(*, index, id, body, params=None, headers=None)`

Creates a new document in the index. Returns a 409 response when a document with a same ID already exists in the index.

### `Parameters:`

-
index (Any) – Name of the data stream or index to target. If the target doesn’t exist and matches the name or wildcard (*) pattern of an index template with a data_stream definition, this request creates the data stream. If the target doesn’t exist and doesn’t match a data stream template, this request creates the index.

-
id (Any) – The unique identifier for the document.

-
body (Any) – The document

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period the request waits for the following operations: automatic index creation, dynamic mapping updates, waiting for active shards.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
index

-
id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_pit(*, index, params=None, headers=None)`

Creates point in time context.

### `Parameters:`

-
index (Any) – A comma-separated list of indexes; use _all or empty string to perform the operation on all indexes.

-
allow_partial_pit_creation – Allow if point in time can be created with partial failures.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Whether to expand wildcard expression to concrete indexes that are open, closed or both. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
keep_alive – Specify the keep alive for point in time.

-
preference – Specify the node or shard the operation should be performed on. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
routing – A comma-separated list of specific routing values.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete(*, index, id, params=None, headers=None)`

Removes a document from the index.

### `Parameters:`

-
index (Any) – Name of the target index.

-
id (Any) – The unique identifier for the document.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
if_primary_term – Only perform the operation if the document has this primary term.

-
if_seq_no – Only perform the operation if the document has this sequence number.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for active shards.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_all_pits(*, params=None, headers=None)`

Deletes all active point in time searches.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_by_query(*, index, body, params=None, headers=None)`

Deletes documents matching the provided query.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams or indexes, omit this parameter or use * or _all.

-
body (Any) – The search definition using the Query DSL

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – List of fields to exclude from the returned _source field.

-
_source_includes – List of fields to extract and return from the _source field.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. Default is false.

-
analyzer – Analyzer to use for the query string.

-
conflicts – What to do if delete by query hits version conflicts: abort or proceed. Valid choices are abort, proceed.

-
default_operator – The default operator for query string query: AND or OR. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
from – Starting offset. Default is 0.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
max_docs – Maximum number of documents to process. Defaults to all documents.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
refresh – If true, OpenSearch refreshes all shards involved in the delete by query after the request completes. Valid choices are false, true, wait_for.

-
request_cache – If true, the request cache is used for this request. Defaults to the index-level setting.

-
requests_per_second – The throttle for this request in sub- requests per second. Default is 0.

-
routing – A custom value used to route operations to a specific shard.

-
scroll – Period to retain the search context for scrolling.

-
scroll_size – Size of the scroll request that powers the operation. Default is 100.

-
search_timeout – Explicit timeout for each search request. Defaults to no timeout.

-
search_type – The type of the search operation. Available options: query_then_fetch, dfs_query_then_fetch. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
size – Deprecated, use max_docs instead.

-
slices – The number of slices this task should be divided into.

-
sort – A comma-separated list of <field>:<direction> pairs.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stats – Specific tag of the request for logging and statistical purposes.

-
terminate_after – Maximum number of documents to collect for each shard. If a query reaches this limit, OpenSearch terminates the query early. OpenSearch collects documents before sorting. Use with caution. OpenSearch applies this parameter to each shard handling the request. When possible, let OpenSearch perform early termination automatically. Avoid specifying this parameter for requests that target data streams with backing indexes across multiple data tiers.

-
timeout – Period each deletion request waits for active shards.

-
version – If true, returns the document version as part of a hit.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – If true, the request blocks until the operation is complete. Default is True.

-
index

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_by_query_rethrottle(*, task_id, params=None, headers=None)`

Changes the number of requests per second for a particular Delete By Query operation.

### `Parameters:`

-
task_id (Any) – The ID for the task.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
requests_per_second – The throttle for this request in sub- requests per second.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
task_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_pit(*, body=None, params=None, headers=None)`

Deletes one or more point in time searches based on the IDs passed.

### `Parameters:`

-
body (Any) – The point-in-time ids to be deleted

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_script(*, id, params=None, headers=None)`

Deletes a script.

### `Parameters:`

-
id (Any) – Identifier for the stored script or search template.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `exists(*, index, id, params=None, headers=None)`

Returns information about whether a document exists in an index.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases. Supports wildcards (*).

-
id (Any) – Identifier of the document.

-
_source – true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude in the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time.

-
refresh – If true, OpenSearch refreshes all shards involved in the delete by query after the request completes. Valid choices are false, true, wait_for.

-
routing – Target the specified primary shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stored_fields – List of stored fields to return as part of a hit. If no fields are specified, no stored fields are included in the response. If this field is specified, the _source parameter defaults to false.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `exists_source(*, index, id, params=None, headers=None)`

Returns information about whether a document source exists in an index.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases. Supports wildcards (*).

-
id (Any) – Identifier of the document.

-
_source – true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude in the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time.

-
refresh – If true, OpenSearch refreshes all shards involved in the delete by query after the request completes. Valid choices are false, true, wait_for.

-
routing – Target the specified primary shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `explain(*, index, id, body=None, params=None, headers=None)`

Returns information about why a specific document matches (or doesn’t match) a query.

### `Parameters:`

-
index (Any) – Index names used to limit the request. Only a single index name can be provided to this parameter.

-
id (Any) – Defines the document ID.

-
body (Any) – The query definition using the Query DSL

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude from the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. Default is false.

-
analyzer – Analyzer to use for the query string. This parameter can only be used when the q query string parameter is specified.

-
default_operator – The default operator for query string query: AND or OR. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string. Default is _all.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stored_fields – A comma-separated list of stored fields to return in the response.

-
index

-
id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `field_caps(*, body=None, index=None, params=None, headers=None)`

Returns the information about the capabilities of fields among multiple indexes.

### `Parameters:`

-
body (Any) – An index filter specified with the Query DSL

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – The type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma-separated values, such as open,hidden. Valid choices are all, closed, hidden, none, open.

-
fields – A comma-separated list of fields to retrieve capabilities for. Wildcard (*) expressions are supported.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If true, missing or closed indexes are not included in the response.

-
include_unmapped – If true, unmapped fields are included in the response. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get(*, index, id, params=None, headers=None)`

Returns a document.

### `Parameters:`

-
index (Any) – The name of the index containing the document.

-
id (Any) – The unique identifier of the document.

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude in the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search. If false, do nothing with refreshes. Valid choices are false, true, wait_for.

-
routing – Target the specified primary shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stored_fields – List of stored fields to return as part of a hit. If no fields are specified, no stored fields are included in the response. If this field is specified, the _source parameter defaults to false.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: internal, external, external_gte. Valid choices are external, external_gte, internal.

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_all_pits(*, params=None, headers=None)`

Lists all active point in time searches.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_script(*, id, params=None, headers=None)`

Returns a script.

### `Parameters:`

-
id (Any) – Identifier for the stored script or search template.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Specify timeout for connection to master

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_script_context(*, params=None, headers=None)`

Returns all script contexts.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_script_languages(*, params=None, headers=None)`

Returns available script types, languages and contexts.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_source(*, index, id, params=None, headers=None)`

Returns the source of a document.

### `Parameters:`

-
index (Any) – The name of the index containing the document.

-
id (Any) – The unique identifier of the document.

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude in the response.

-
_source_includes – A comma-separated list of source fields to include in the response.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – Boolean) If true, the request is real time as opposed to near real time.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search. If false, do nothing with refreshes. Valid choices are false, true, wait_for.

-
routing – Target the specified primary shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type. One of internal, external, external_gte. Valid choices are external, external_gte, internal.

-
index

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `index(*, index, body, id=None, params=None, headers=None)`

Creates or updates a document in an index.

### `Parameters:`

-
index (Any) – Name of the data stream or index to target.

-
body (Any) – The document

-
id (Any) – The unique identifier for the document.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
if_primary_term – Only perform the operation if the document has this primary term.

-
if_seq_no – Only perform the operation if the document has this sequence number.

-
op_type – Set to create to only index the document if it does not already exist (put if absent). If a document with the specified _id already exists, the indexing operation will fail. Same as using the <index>/_create endpoint. Valid values: index, create. If document id is specified, it defaults to index. Otherwise, it defaults to create.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid values: true, false, wait_for.

-
require_alias – If true, the destination must be an index alias. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period the request waits for the following operations: automatic index creation, dynamic mapping updates, waiting for active shards.

-
version – Explicit version number for concurrency control. The specified version must match the current version of the document for the request to succeed.

-
version_type – The specific version type: external, external_gte. Valid choices are external, external_gte, internal.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
index

-
body

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `info(*, params=None, headers=None)`

Returns basic information about the cluster.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `mget(*, body, index=None, params=None, headers=None)`

Allows to get multiple documents in one request.

### `Parameters:`

-
body (Any) – Document identifiers; can be either docs (containing full document information) or ids (when index is provided in the URL.

-
index (Any) – The name of the index to retrieve documents from when ids are specified, or when a document in the docs array does not specify an index.

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – A comma-separated list of source fields to exclude from the response. You can also use this parameter to exclude fields from the subset specified in _source_includes query parameter.

-
_source_includes – A comma-separated list of source fields to include in the response. If this parameter is specified, only these source fields are returned. You can exclude fields from this subset using the _source_excludes query parameter. If the _source parameter is false, this parameter is ignored.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time.

-
refresh – If true, the request refreshes relevant shards before retrieving documents. Valid choices are false, true, wait_for.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stored_fields – If true, retrieves the document fields stored in the index rather than the document _source.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `msearch(*, body, index=None, params=None, headers=None)`

Allows to execute several search operations in one request.

### `Parameters:`

-
body (Any) – The request definitions (metadata-search request definition pairs), separated by newlines

-
index (Any) – A comma-separated list of data streams, indexes, and index aliases to search.

-
ccs_minimize_roundtrips – If true, network round-trips between the coordinating node and remote clusters are minimized for cross-cluster search requests. Default is True.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
max_concurrent_searches – Maximum number of concurrent searches the multi search API can execute.

-
max_concurrent_shard_requests – Maximum number of concurrent shard requests that each sub-search request executes per node. Default is 5.

-
pre_filter_shard_size – Defines a threshold that enforces a pre-filter roundtrip to prefilter search shards based on query rewriting if the number of shards the search request expands to exceeds the threshold. This filter roundtrip can limit the number of shards significantly if for instance a shard can not match any documents based on its rewrite method i.e., if date filters are mandatory to match but the shard bounds and the query are disjoint.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
rest_total_hits_as_int – If true, hits.total are returned as an integer in the response. Defaults to false, which returns an object. Default is false.

-
search_type – Indicates whether global term and document frequencies should be used when scoring returned documents. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
typed_keys – Specifies whether aggregation and suggester names should be prefixed by their respective types in the response.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `msearch_template(*, body, index=None, params=None, headers=None)`

Allows to execute several search template operations in one request.

### `Parameters:`

-
body (Any) – The request definitions (metadata-search request definition pairs), separated by newlines

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams and indexes, omit this parameter or use *.

-
ccs_minimize_roundtrips – If true, network round-trips are minimized for cross-cluster search requests. Default is True.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
max_concurrent_searches – Maximum number of concurrent searches the API can run.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
rest_total_hits_as_int – If true, the response returns hits.total as an integer. If false, it returns hits.total as an object. Default is false.

-
search_type – The type of the search operation. Available options: query_then_fetch, dfs_query_then_fetch. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
typed_keys – If true, the response prefixes aggregation and suggester names with their respective types.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `mtermvectors(*, body=None, index=None, params=None, headers=None)`

Returns multiple termvectors in one request.

### `Parameters:`

-
body (Any) – Define ids, documents, parameters or a list of parameters per document here. You must at least provide a list of document ids. See documentation.

-
index (Any) – The name of the index that contains the document.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
field_statistics – If true, the response includes the document count, sum of document frequencies, and sum of total term frequencies. Default is True.

-
fields – A comma-separated list or a wildcard expression specifying the fields to include in the statistics. Used as the default list unless a specific field list is provided in the completion_fields or fielddata_fields parameters.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ids – A comma-separated list of documents IDs. You must provide either the docs field in the request body or specify ids as a query parameter or in the request body.

-
offsets – If true, the response includes term offsets. Default is True.

-
payloads – If true, the response includes term payloads. Default is True.

-
positions – If true, the response includes term positions. Default is True.

-
preference – Specifies the node or shard on which the operation should be performed. See [preference query parameter]({{site.url}}{{site.baseurl}}/api-reference/search- apis/search/#the-preference-query-parameter) for a list of available options. By default the requests are routed randomly to available shard copies (primary or replica), with no guarantee of consistency across repeated queries.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time. Default is True.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
term_statistics – If true, the response includes term frequency and document frequency. Default is false.

-
version – If true, returns the document version as part of a hit.

-
version_type – The specific version type. Valid choices are external, external_gte, internal.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `ping(*, params=None, headers=None)`

Returns whether the cluster is running.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_script(*, id, body, context=None, params=None, headers=None)`

Creates or updates a script.

### `Parameters:`

-
id (Any) – Identifier for the stored script or search template. Must be unique within the cluster.

-
body (Any) – The document

-
context (Any) – Context in which the script or search template should run. To prevent errors, the API immediately compiles the script or template in this context.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
id

-
body

-
context

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `rank_eval(*, body, index=None, params=None, headers=None)`

Allows to evaluate the quality of ranked search results over a set of typical search queries.

### `Parameters:`

-
body (Any) – The ranking evaluation search definition, including search requests, document ratings and ranking metric definition.

-
index (Any) – A comma-separated list of data streams, indexes, and index aliases used to limit the request. Wildcard (*) expressions are supported. To target all data streams and indexes in a cluster, omit this parameter or use _all or *.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Whether to expand wildcard expression to concrete indexes that are open, closed or both. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If true, missing or closed indexes are not included in the response.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
search_type – Search operation type Valid choices are dfs_query_then_fetch, query_then_fetch.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `reindex(*, body, params=None, headers=None)`

Allows to copy documents from one index to another, optionally filtering the source documents by a query, changing the destination index settings, or fetching the documents from a remote cluster.

### `Parameters:`

-
body (Any) – The search definition using the Query DSL and the prototype for the index request.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
max_docs – Maximum number of documents to process. By default, all documents.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If true, the request refreshes affected shards to make this operation visible to search. Valid choices are false, true, wait_for.

-
requests_per_second – The throttle for this request in sub- requests per second. Defaults to no throttle. Default is 0.

-
scroll – Specifies how long a consistent view of the index should be maintained for scrolled search.

-
slices – The number of slices this task should be divided into. Defaults to 1 slice, meaning the task isn’t sliced into subtasks.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period each indexing waits for automatic index creation, dynamic mapping updates, and waiting for active shards.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – If true, the request blocks until the operation is complete. Default is True.

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `reindex_rethrottle(*, task_id, params=None, headers=None)`

Changes the number of requests per second for a particular reindex operation.

### `Parameters:`

-
task_id (Any) – Identifier for the task.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
requests_per_second – The throttle for this request in sub- requests per second.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
task_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `render_search_template(*, body=None, id=None, params=None, headers=None)`

Allows to use the Mustache language to pre-render a search definition.

### `Parameters:`

-
body (Any) – The search definition template and its parameters.

-
id (Any) – ID of the search template to render. If no source is specified, this or the id request body parameter is required.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `scripts_painless_execute(*, body=None, params=None, headers=None)`

Allows an arbitrary script to be executed and a result to be returned.

### `Parameters:`

-
body (Any) – The script to execute

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `scroll(*, body=None, scroll_id=None, params=None, headers=None)`

Allows to retrieve a large numbers of results from a single search request.

### `Parameters:`

-
scroll_id (Any) – The scroll ID for scrolled search

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
rest_total_hits_as_int – If true, the API response’s hit.total property is returned as an integer. If false, the API response’s hit.total property is returned as an object. Default is false.

-
scroll – Period to retain the search context for scrolling.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body (Any)

-
scroll_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search(*, body=None, index=None, params=None, headers=None)`

Returns results matching a query.

### `Parameters:`

-
body (Any) – The search definition using the Query DSL

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams and indexes, omit this parameter or use * or _all.

-
_source – Indicates which source fields are returned for matching documents. These fields are returned in the hits._source property of the search response. Valid values are: true to return the entire document source; false to not return the document source; <string> to return the source fields that are specified as a comma- separated list (supports wildcard (*) patterns).

-
_source_excludes – A comma-separated list of source fields to exclude from the response. You can also use this parameter to exclude fields from the subset specified in _source_includes query parameter. If the _source parameter is false, this parameter is ignored.

-
_source_includes – A comma-separated list of source fields to include in the response. If this parameter is specified, only these source fields are returned. You can exclude fields from this subset using the _source_excludes query parameter. If the _source parameter is false, this parameter is ignored.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
allow_partial_search_results – If true, returns partial results if there are shard request timeouts or shard failures. If false, returns an error with no partial results. Default is True.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. This parameter can only be used when the q query string parameter is specified. Default is false.

-
analyzer – Analyzer to use for the query string. This parameter can only be used when the q query string parameter is specified.

-
batched_reduce_size – The number of shard results that should be reduced at once on the coordinating node. This value should be used as a protection mechanism to reduce the memory overhead per search request if the potential number of shards in the request can be large. Default is 512.

-
cancel_after_time_interval – The time after which the search request will be canceled. Request-level parameter takes precedence over cancel_after_time_interval cluster setting.

-
ccs_minimize_roundtrips – If true, network round-trips between the coordinating node and the remote clusters are minimized when executing cross-cluster search (CCS) requests. Default is True.

-
default_operator – The default operator for query string query: AND or OR. This parameter can only be used when the q query string parameter is specified. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string. This parameter can only be used when the q query string parameter is specified.

-
docvalue_fields – A comma-separated list of fields to return as the docvalue representation for each hit.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid choices are all, closed, hidden, none, open.

-
explain – If true, returns detailed information about score computation as part of a hit.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
from – Starting document offset. Needs to be non-negative. By default, you cannot page through more than 10,000 hits using the from and size parameters. To page through more hits, use the search_after parameter. Default is 0.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_throttled – If true, concrete, expanded or aliased indexes will be ignored when frozen.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
include_named_queries_score – Indicates whether hit.matched_queries should be rendered as a map that includes the name of the matched query associated with its score (true) or as an array containing the name of the matched queries (false) Default is false.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored. This parameter can only be used when the q query string parameter is specified.

-
max_concurrent_shard_requests – Defines the number of concurrent shard requests per node this search executes concurrently. This value should be used to limit the impact of the search on the cluster in order to limit the number of concurrent shard requests. Default is 5.

-
phase_took – Indicates whether to return phase-level took time values in the response. Default is false.

-
pre_filter_shard_size – Defines a threshold that enforces a pre-filter roundtrip to prefilter search shards based on query rewriting if the number of shards the search request expands to exceeds the threshold. This filter roundtrip can limit the number of shards significantly if for instance a shard can not match any documents based on its rewrite method (if date filters are mandatory to match but the shard bounds and the query are disjoint). When unspecified, the pre- filter phase is executed if any of these conditions is met: the request targets more than 128 shards; the request targets one or more read-only index; the primary sort of the query targets an indexed field.

-
preference – Nodes and shards used for the search. By default, OpenSearch selects from eligible nodes and shards using adaptive replica selection, accounting for allocation awareness. Valid values are: _only_local to run the search only on shards on the local node; _local to, if possible, run the search on shards on the local node, or if not, select shards using the default method; _only_nodes:<node-id>,<node-id> to run the search on only the specified nodes IDs, where, if suitable shards exist on more than one selected node, use shards on those nodes using the default method, or if none of the specified nodes are available, select shards from any available node using the default method; _prefer_nodes:<node-id>,<node- id> to if possible, run the search on the specified nodes IDs, or if not, select shards using the default method; _shards:<shard>,<shard> to run the search only on the specified shards; <custom-string> (any string that does not start with _) to route searches with the same <custom-string> to the same shards in the same order. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax using query parameter search. Query parameter searches do not support the full OpenSearch Query DSL but are handy for testing.

-
request_cache – If true, the caching of search results is enabled for requests where size is 0. Defaults to index level settings.

-
rest_total_hits_as_int – Indicates whether hits.total should be rendered as an integer or an object in the rest search response. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
scroll – Period to retain the search context for scrolling. See Scroll search results. By default, this value cannot exceed 1d (24 hours). You can change this limit using the search.max_keep_alive cluster-level setting.

-
search_pipeline – Customizable sequence of processing stages applied to search queries.

-
search_type – How distributed term frequencies are calculated for relevance scoring. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
seq_no_primary_term – If true, returns sequence number and primary term of the last modification of each hit.

-
size – Defines the number of hits to return. By default, you cannot page through more than 10,000 hits using the from and size parameters. To page through more hits, use the search_after parameter. Default is 10.

-
sort – A comma-separated list of <field>:<direction> pairs.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stats – Specific tag of the request for logging and statistical purposes.

-
stored_fields – A comma-separated list of stored fields to return as part of a hit. If no fields are specified, no stored fields are included in the response. If this field is specified, the _source parameter defaults to false. You can pass _source: true to return both source fields and stored fields in the search response.

-
suggest_field – Specifies which field to use for suggestions.

-
suggest_mode – Specifies the suggest mode. This parameter can only be used when the suggest_field and suggest_text query string parameters are specified. Valid choices are always, missing, popular.

-
suggest_size – Number of suggestions to return. This parameter can only be used when the suggest_field and suggest_text query string parameters are specified.

-
suggest_text – The source text for which the suggestions should be returned. This parameter can only be used when the suggest_field and suggest_text query string parameters are specified.

-
terminate_after – Maximum number of documents to collect for each shard. If a query reaches this limit, OpenSearch terminates the query early. OpenSearch collects documents before sorting. Use with caution. OpenSearch applies this parameter to each shard handling the request. When possible, let OpenSearch perform early termination automatically. Avoid specifying this parameter for requests that target data streams with backing indexes across multiple data tiers. If set to 0 (default), the query does not terminate early.

-
timeout – Specifies the period of time to wait for a response from each shard. If no response is received before the timeout expires, the request fails and returns an error.

-
track_scores – If true, calculate and return document scores, even if the scores are not used for sorting.

-
track_total_hits – Number of hits matching the query to count accurately. If true, the exact number of hits is returned at the cost of some performance. If false, the response does not include the total number of hits matching the query.

-
typed_keys – If true, aggregation and suggester names are be prefixed by their respective types in the response.

-
verbose_pipeline – Enables or disables verbose mode for the search pipeline. When verbose mode is enabled, detailed information about each processor in the search pipeline is included in the search response. This includes the processor name, execution status, input, output, and time taken for processing. This parameter is primarily intended for debugging purposes, allowing users to track how data flows and transforms through the search pipeline.

-
version – If true, returns document version as part of a hit.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search_shards(*, body=None, index=None, params=None, headers=None)`

Returns information about the indexes and shards that a search request would be executed against.

### `Parameters:`

-
index (Any) – Returns the indexes and shards that a search request would be executed against.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
local – If true, the request retrieves information from the local node only. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
body (Any)

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search_template(*, body, index=None, params=None, headers=None)`

Allows to use the Mustache language to pre-render a search definition.

### `Parameters:`

-
body (Any) – The search definition template and its parameters.

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*).

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
ccs_minimize_roundtrips – If true, network round-trips are minimized for cross-cluster search requests. Default is True.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
explain – If true, the response includes additional details about score computation as part of a hit.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_throttled – If true, specified concrete, expanded, or aliased indexes are not included in the response when throttled.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
phase_took – Indicates whether to return phase-level took time values in the response. Default is false.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
profile – If true, the query execution is profiled.

-
rest_total_hits_as_int – If true, hits.total are rendered as an integer in the response. Default is false.

-
routing – A custom value used to route operations to a specific shard.

-
scroll – Specifies how long a consistent view of the index should be maintained for scrolled search.

-
search_pipeline – Customizable sequence of processing stages applied to search queries.

-
search_type – The type of the search operation. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
typed_keys – If true, the response prefixes aggregation and suggester names with their respective types.

-
body

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `termvectors(*, index, body=None, id=None, params=None, headers=None)`

Returns information and statistics about terms in the fields of a particular document.

### `Parameters:`

-
index (Any) – The name of the index containing the document.

-
body (Any) – Define parameters and or supply a document to get termvectors for. See documentation.

-
id (Any) – The unique identifier of the document.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
field_statistics – If true, the response includes the document count, sum of document frequencies, and sum of total term frequencies. Default is True.

-
fields – A comma-separated list or a wildcard expression specifying the fields to include in the statistics. Used as the default list unless a specific field list is provided in the completion_fields or fielddata_fields parameters.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
offsets – If true, the response includes term offsets. Default is True.

-
payloads – If true, the response includes term payloads. Default is True.

-
positions – If true, the response includes term positions. Default is True.

-
preference – Specifies the node or shard on which the operation should be performed. See [preference query parameter]({{site.url}}{{site.baseurl}}/api-reference/search- apis/search/#the-preference-query-parameter) for a list of available options. By default the requests are routed randomly to available shard copies (primary or replica), with no guarantee of consistency across repeated queries.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
realtime – If true, the request is real time as opposed to near real time. Default is True.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
term_statistics – If true, the response includes term frequency and document frequency. Default is false.

-
version – If true, returns the document version as part of a hit.

-
version_type – The specific version type. Valid choices are external, external_gte, internal.

-
index

-
body

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update(*, index, id, body, params=None, headers=None)`

Updates a document with a script or partial document.

### `Parameters:`

-
index (Any) – The name of the index

-
id (Any) – Document ID

-
body (Any) – The request definition requires either script or partial doc

-
_source – Set to false to disable source retrieval. You can also specify a comma-separated list of the fields you want to retrieve.

-
_source_excludes – Specify the source fields you want to exclude.

-
_source_includes – Specify the source fields you want to retrieve.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
if_primary_term – Only perform the operation if the document has this primary term.

-
if_seq_no – Only perform the operation if the document has this sequence number.

-
lang – The script language. Default is painless.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
refresh – If ‘true’, OpenSearch refreshes the affected shards to make this operation visible to search, if wait_for then wait for a refresh to make this operation visible to search, if false do nothing with refreshes. Valid choices are false, true, wait_for.

-
require_alias – If true, the destination must be an index alias. Default is false.

-
retry_on_conflict – Specify how many times should the operation be retried when a conflict occurs. Default is 0.

-
routing – A custom value used to route operations to a specific shard.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for dynamic mapping updates and active shards. This guarantees OpenSearch waits for at least the timeout before failing. The actual wait time could be longer, particularly when multiple waits occur.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operations. Set to ‘all’ or any positive integer up to the total number of shards in the index (number_of_replicas+1). Defaults to 1 meaning the primary shard.

-
index

-
id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_by_query(*, index, body=None, params=None, headers=None)`

Performs an update on every document in the index without changing the source, for example to pick up a mapping change.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams or indexes, omit this parameter or use * or _all.

-
body (Any) – The search definition using the Query DSL

-
_source – Set to true or false to return the _source field or not, or a list of fields to return.

-
_source_excludes – List of fields to exclude from the returned _source field.

-
_source_includes – List of fields to extract and return from the _source field.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. Default is false.

-
analyzer – Analyzer to use for the query string.

-
conflicts – What to do if update by query hits version conflicts: abort or proceed. Valid choices are abort, proceed.

-
default_operator – The default operator for query string query: AND or OR. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
from – Starting offset. Default is 0.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
max_docs – Maximum number of documents to process. Defaults to all documents.

-
pipeline – ID of the pipeline to use to preprocess incoming documents. If the index has a default ingest pipeline specified, then setting the value to _none disables the default ingest pipeline for this request. If a final pipeline is configured it will always run, regardless of the value of this parameter.

-
preference – Specifies the node or shard the operation should be performed on. Random by default. Default is random.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
refresh – If true, OpenSearch refreshes affected shards to make the operation visible to search. Valid choices are false, true, wait_for.

-
request_cache – If true, the request cache is used for this request.

-
requests_per_second – The throttle for this request in sub- requests per second. Default is 0.

-
routing – A custom value used to route operations to a specific shard.

-
scroll – Period to retain the search context for scrolling.

-
scroll_size – Size of the scroll request that powers the operation. Default is 100.

-
search_timeout – Explicit timeout for each search request.

-
search_type – The type of the search operation. Available options: query_then_fetch, dfs_query_then_fetch. Valid choices are dfs_query_then_fetch, query_then_fetch.

-
size – Deprecated, use max_docs instead.

-
slices – The number of slices this task should be divided into.

-
sort – A comma-separated list of <field>:<direction> pairs.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
stats – Specific tag of the request for logging and statistical purposes.

-
terminate_after – Maximum number of documents to collect for each shard. If a query reaches this limit, OpenSearch terminates the query early. OpenSearch collects documents before sorting. Use with caution. OpenSearch applies this parameter to each shard handling the request. When possible, let OpenSearch perform early termination automatically. Avoid specifying this parameter for requests that target data streams with backing indexes across multiple data tiers.

-
timeout – Period each update request waits for the following operations: dynamic mapping updates, waiting for active shards.

-
version – If true, returns the document version as part of a hit.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – If true, the request blocks until the operation is complete. Default is True.

-
index

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_by_query_rethrottle(*, task_id, params=None, headers=None)`

Changes the number of requests per second for a particular Update By Query operation.

### `Parameters:`

-
task_id (Any) – The ID for the task.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
requests_per_second – The throttle for this request in sub- requests per second.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
task_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any


## Source: `api-ref/clients/http_client.html`

## Http Client

### `class opensearchpy.client.http.HttpClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Client)

### `delete(url, headers=None, params=None, body=None)`

Perform a DELETE request and return the data.

### `Parameters:`

-
url (str) – absolute url (without host) to target

-
headers (Mapping[str, Any] | None) – dictionary of headers, will be handed over to the underlying Connection class

-
params (Mapping[str, Any] | None) – dictionary of query parameters, will be handed over to the underlying Connection class for serialization

-
body (Any | None) – body of the request, will be serialized using serializer and passed to the connection

-
url

-
headers

-
params

-
body

### `Return type:`

Any

### `get(url, headers=None, params=None, body=None)`

Perform a GET request and return the data.

### `Parameters:`

-
url (str) – absolute url (without host) to target

-
headers (Mapping[str, Any] | None) – dictionary of headers, will be handed over to the underlying Connection class

-
params (Mapping[str, Any] | None) – dictionary of query parameters, will be handed over to the underlying Connection class for serialization

-
body (Any | None) – body of the request, will be serialized using serializer and passed to the connection

-
url

-
headers

-
params

-
body

### `Return type:`

Any

### `head(url, headers=None, params=None, body=None)`

Perform a HEAD request and return the data.

### `Parameters:`

-
url (str) – absolute url (without host) to target

-
headers (Mapping[str, Any] | None) – dictionary of headers, will be handed over to the underlying Connection class

-
params (Mapping[str, Any] | None) – dictionary of query parameters, will be handed over to the underlying Connection class for serialization

-
body (Any | None) – body of the request, will be serialized using serializer and passed to the connection

-
url

-
headers

-
params

-
body

### `Return type:`

Any

### `post(url, headers=None, params=None, body=None)`

Perform a POST request and return the data.

### `Parameters:`

-
url (str) – absolute url (without host) to target

-
headers (Mapping[str, Any] | None) – dictionary of headers, will be handed over to the underlying Connection class

-
params (Mapping[str, Any] | None) – dictionary of query parameters, will be handed over to the underlying Connection class for serialization

-
body (Any | None) – body of the request, will be serialized using serializer and passed to the connection

-
url

-
headers

-
params

-
body

### `Return type:`

Any

### `put(url, headers=None, params=None, body=None)`

Perform a PUT request and return the data.

### `Parameters:`

-
url (str) – absolute url (without host) to target

-
headers (Mapping[str, Any] | None) – dictionary of headers, will be handed over to the underlying Connection class

-
params (Mapping[str, Any] | None) – dictionary of query parameters, will be handed over to the underlying Connection class for serialization

-
body (Any | None) – body of the request, will be serialized using serializer and passed to the connection

-
url

-
headers

-
params

-
body

### `Return type:`

Any
