# Clients Namespaces

> Local snapshot generated from OpenSearch Python Client API Reference on 2026-07-27. Use this file instead of browsing the live documentation during skill execution.


## Source: `api-ref/clients/cat_client.html`

## Compact and aligned text (CAT) Client

### `class opensearchpy.client.cat.CatClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `aliases(*, name=None, params=None, headers=None)`

Shows information about aliases currently configured to indexes, including filter and routing information.

### `Parameters:`

-
name (Any) – A comma-separated list of aliases to retrieve. Supports wildcards (*). To retrieve all aliases, omit this parameter or use * or _all.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Specifies the type of index that wildcard expressions can match. Supports comma-separated values. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Whether to return information from the local node only instead of from the cluster manager node. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `all_pit_segments(*, params=None, headers=None)`

Lists all active CAT point-in-time segments.

### `Parameters:`

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `allocation(*, node_id=None, params=None, headers=None)`

Provides a snapshot of how many shards are allocated to each data node and how much disk space they are using.

### `Parameters:`

-
node_id (Any) – A comma-separated list of node IDs or names used to limit the returned information.

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
cluster_manager_timeout – A timeout for connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the HTTP Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from cluster-manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A timeout for connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
node_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `cluster_manager(*, params=None, headers=None)`

Returns information about the cluster-manager node.

### `Parameters:`

-
cluster_manager_timeout – A timeout for connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the HTTP Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A timeout for connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `count(*, index=None, params=None, headers=None)`

Provides quick access to the document count of the entire cluster or of an individual index.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `fielddata(*, fields=None, params=None, headers=None)`

Shows how much heap memory is currently being used by field data on every data node in the cluster.

### `Parameters:`

-
fields (Any) – A comma-separated list of fields used to limit the amount of returned information.

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
fields

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `health(*, params=None, headers=None)`

Returns a concise representation of the cluster health.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – The unit used to display time values. Valid choices are nanos, micros, ms, s, m, h, d.

-
ts – When true, returns HH:MM:SS and Unix epoch timestamps. Default is True.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `help(*, params=None, headers=None)`

Returns help for the Cat APIs.

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

### `indices(*, index=None, params=None, headers=None)`

Lists information related to indexes, that is, how much disk space they are using, how many shards they have, their health status, and so on.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Specifies the type of index that wildcard expressions can match. Supports comma-separated values. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
health – Limits indexes based on their health status. Supported values are green, yellow, and red. Valid choices are green, yellow, red.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
include_unloaded_segments – Whether to include information from segments not loaded into memory. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
pri – When true, returns information only from the primary shards. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – Specifies the time units. Valid choices are nanos, micros, ms, s, m, h, d.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `master(*, params=None, headers=None)`

Returns information about the cluster-manager node.

### `Parameters:`

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `nodeattrs(*, params=None, headers=None)`

Returns information about custom node attributes.

### `Parameters:`

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `nodes(*, params=None, headers=None)`

Returns basic statistics about the performance of cluster nodes.

### `Parameters:`

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
full_id – When true, returns the full node ID. When false, returns the shortened node ID.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – This parameter does not cause this API to act locally.): Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – Specifies the time units, for example, 5d or 7h. For more information, see [Supported units](https://opensearch.org/docs/latest/api-reference/units/). Valid choices are nanos, micros, ms, s, m, h, d.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `pending_tasks(*, params=None, headers=None)`

Returns a concise representation of the cluster’s pending tasks.

### `Parameters:`

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – Specifies the time units, for example, 5d or 7h. For more information, see [Supported units](https://opensearch.org/docs/latest/api-reference/units/). Valid choices are nanos, micros, ms, s, m, h, d.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `pit_segments(*, body=None, params=None, headers=None)`

Lists one or several CAT point-in-time segments.

### `Parameters:`

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `plugins(*, params=None, headers=None)`

Returns information about the names, components, and versions of the installed plugins.

### `Parameters:`

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `recovery(*, index=None, params=None, headers=None)`

Returns all completed and ongoing index and shard recoveries.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
active_only – If true, the response only includes ongoing shard recoveries. Default is false.

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
detailed – When true, includes detailed information about shard recoveries. Default is false.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – Specifies the time units, for example, 5d or 7h. For more information, see [Supported units](https://opensearch.org/docs/latest/api-reference/units/). Valid choices are nanos, micros, ms, s, m, h, d.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `repositories(*, params=None, headers=None)`

Returns information about all snapshot repositories for a cluster.

### `Parameters:`

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `segment_replication(*, index=None, params=None, headers=None)`

Returns information about active and last-completed segment replication events on each replica shard, including related shard-level metrics. These metrics provide information about how far behind the primary shard the replicas are lagging.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
active_only – When true, the response only includes ongoing segment replication events. Default is false.

-
allow_no_indices – Whether to ignore the index if a wildcard index expression resolves to no concrete indexes. This includes the _all string or when no indexes have been specified.

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
completed_only – When true, the response only includes the last-completed segment replication events. Default is false.

-
detailed – When true, the response includes additional metrics for each stage of a segment replication event. Default is false.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Specifies the type of index that wildcard expressions can match. Supports comma-separated values. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_throttled – Whether specified concrete, expanded, or aliased indexes should be ignored when throttled.

-
ignore_unavailable – Whether the specified concrete indexes should be ignored when missing or closed.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
shards – A comma-separated list of shards to display.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – Specifies the time units, for example, 5d or 7h. For more information, see [Supported units](https://opensearch.org/docs/latest/api-reference/units/). Valid choices are nanos, micros, ms, s, m, h, d.

-
timeout – The operation timeout.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `segments(*, index=None, params=None, headers=None)`

Provides low-level information about the segments in the shards of an index.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `shards(*, index=None, params=None, headers=None)`

Lists the states of all primary and replica shards and how they are distributed.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
bytes – The units used to display byte values. Valid choices are b, kb, k, mb, m, gb, g, tb, t, pb, p.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – Specifies the time units, for example, 5d or 7h. For more information, see [Supported units](https://opensearch.org/docs/latest/api-reference/units/). Valid choices are nanos, micros, ms, s, m, h, d.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `snapshots(*, repository=None, params=None, headers=None)`

Lists all of the snapshots stored in a specific repository.

### `Parameters:`

-
repository (Any) – A comma-separated list of snapshot repositories used to limit the request. Accepts wildcard expressions. _all returns all repositories. If any repository fails during the request, OpenSearch returns an error.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – When true, the response does not include information from unavailable snapshots. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – Specifies the time units, for example, 5d or 7h. For more information, see [Supported units](https://opensearch.org/docs/latest/api-reference/units/). Valid choices are nanos, micros, ms, s, m, h, d.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
repository

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `tasks(*, params=None, headers=None)`

Lists the progress of all tasks currently running on the cluster.

### `Parameters:`

-
actions – The task action names used to limit the response.

-
detailed – If true, the response includes detailed information about shard recoveries. Default is false.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
nodes – A comma-separated list of node IDs or names used to limit the returned information. Use _local to return information from the node to which you’re connecting, specify a specific node from which to get information, or keep the parameter empty to get information from all nodes.

-
parent_task_id – The parent task identifier, which is used to limit the response.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
time – Specifies the time units, for example, 5d or 7h. For more information, see [Supported units](https://opensearch.org/docs/latest/api-reference/units/). Valid choices are nanos, micros, ms, s, m, h, d.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `templates(*, name=None, params=None, headers=None)`

Lists the names, patterns, order numbers, and version numbers of index templates.

### `Parameters:`

-
name (Any) – The name of the template to return. Accepts wildcard expressions. If omitted, all templates are returned.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `thread_pool(*, thread_pool_patterns=None, params=None, headers=None)`

Returns cluster-wide thread pool statistics per node. By default the active, queued, and rejected statistics are returned for all thread pools.

### `Parameters:`

-
thread_pool_patterns (Any) – A comma-separated list of thread pool names used to limit the request. Accepts wildcard expressions.

-
cluster_manager_timeout – A timeout for connection to the cluster manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
format – A short version of the Accept header, such as json or yaml.

-
h – A comma-separated list of column names to display.

-
help – Returns help information. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Returns local information but does not retrieve the state from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): The amount of time allowed to establish a connection to the cluster manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
s – A comma-separated list of column names or column aliases to sort by.

-
size – The multiplier in which to display values.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
v – Enables verbose mode, which displays column headers. Default is false.

-
thread_pool_patterns

-
params (Any)

-
headers (Any)

### `Return type:`

Any


## Source: `api-ref/clients/cluster_client.html`

## Cluster Client

### `class opensearchpy.client.cluster.ClusterClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `allocation_explain(*, body=None, params=None, headers=None)`

Explains how shards are allocated in the current cluster and provides an explanation for why unassigned shards can’t be allocated to a node.

### `Parameters:`

-
body (Any) – The index, shard, and primary flag for which to generate an explanation. Leave this empty to generate an explanation for the first unassigned shard.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
include_disk_info – When true, returns information about disk usage and shard sizes. Default is false.

-
include_yes_decisions – When true, returns any YES decisions in the allocation explanation. YES decisions indicate when a particular shard allocation attempt was successful for the given node. Default is false.

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

### `delete_component_template(*, name, params=None, headers=None)`

Deletes a component template.

### `Parameters:`

-
name (Any) – The name of the component template to delete. Supports wildcard (*) expressions.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_decommission_awareness(*, params=None, headers=None)`

Recommissions a decommissioned zone.

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

### `delete_voting_config_exclusions(*, params=None, headers=None)`

Clears any cluster voting configuration exclusions.

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
wait_for_removal – Specifies whether to wait for all excluded nodes to be removed from the cluster before clearing the voting configuration exclusions list. When true, all excluded nodes are removed from the cluster before this API takes any action. When false, the voting configuration exclusions list is cleared even if some excluded nodes are still in the cluster. Default is True.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_weighted_routing(*, body=None, params=None, headers=None)`

Delete weighted shard routing weights.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `exists_component_template(*, name, params=None, headers=None)`

Returns information about whether a particular component template exist.

### `Parameters:`

-
name (Any) – The name of the component template. Wildcard (*) expressions are supported.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – When true, the request retrieves information from the local node only. When false, information is retrieved from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_component_template(*, name=None, params=None, headers=None)`

Returns one or more component templates.

### `Parameters:`

-
name (Any) – The name of the component template to retrieve. Wildcard (*) expressions are supported.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of “cluster”: { “max_shards_per_node”: 500 } is “cluster.max_shards_per_node”: “500”. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – When true, the request retrieves information from the local node only. When false, information is retrieved from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_decommission_awareness(*, awareness_attribute_name, params=None, headers=None)`

Retrieves the decommission status for all zones.

### `Parameters:`

-
awareness_attribute_name (Any) – The name of the awareness attribute.

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
awareness_attribute_name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_settings(*, params=None, headers=None)`

Returns cluster settings.

### `Parameters:`

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of “cluster”: { “max_shards_per_node”: 500 } is “cluster.max_shards_per_node”: “500”. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
include_defaults – When true, returns default cluster settings from the local node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_weighted_routing(*, attribute, params=None, headers=None)`

Fetches weighted shard routing weights.

### `Parameters:`

-
attribute (Any) – The name of the awareness attribute.

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
attribute

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `health(*, index=None, params=None, headers=None)`

Returns basic information about the health of the cluster.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
awareness_attribute – The name of the awareness attribute for which to return the cluster health status (for example, zone). Applicable only if level is set to awareness_attributes.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Specifies the type of index that wildcard expressions can match. Supports comma-separated values. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
level – Controls the amount of detail included in the cluster health response. Valid choices are awareness_attributes, cluster, indices, shards.

-
local – Whether to return information from the local node only instead of from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api- reference/common-parameters/#time-units).

-
wait_for_active_shards – Waits until the specified number of shards is active before returning a response. Use all for all shards.

-
wait_for_events – Waits until all currently queued events with the given priority are processed. Valid choices are immediate, urgent, high, normal, low, languid.

-
wait_for_no_initializing_shards – Whether to wait until there are no initializing shards in the cluster. Default is false.

-
wait_for_no_relocating_shards – Whether to wait until there are no relocating shards in the cluster. Default is false.

-
wait_for_nodes – Waits until the specified number of nodes (N) is available. Accepts >=N, <=N, >N, and <N. You can also use ge(N), le(N), gt(N), and lt(N) notation.

-
wait_for_status – Waits until the cluster health reaches the specified status or better. Valid choices are green, yellow, red.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `pending_tasks(*, params=None, headers=None)`

Returns a list of pending cluster-level tasks, such as index creation, mapping updates, or new allocations.

### `Parameters:`

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – When true, the request retrieves information from the local node only. When false, information is retrieved from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

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

### `post_voting_config_exclusions(*, params=None, headers=None)`

Updates the cluster voting configuration by excluding certain node IDs or names.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
node_ids – A comma-separated list of node IDs to exclude from the voting configuration. When using this setting, you cannot also specify node_names. Either node_ids or node_names are required to receive a valid response.

-
node_names – A comma-separated list of node names to exclude from the voting configuration. When using this setting, you cannot also specify node_ids. Either node_ids or node_names are required to receive a valid response.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – When adding a voting configuration exclusion, the API waits for the specified nodes to be excluded from the voting configuration before returning a response. If the timeout expires before the appropriate condition is satisfied, the request fails and returns an error.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_component_template(*, name, body, params=None, headers=None)`

Creates or updates a component template.

### `Parameters:`

-
name (Any) – The name of the component template to create. OpenSearch includes the following built-in component templates: logs- mappings, logs-settings, metrics-mappings, metrics-settings, synthetics-mapping, and synthetics-settings. OpenSearch uses these templates to configure backing indexes for its data streams. If you want to overwrite one of these templates, set the replacement template version to a higher value than the current version. If you want to disable all built-in component and index templates, set stack.templates.enabled to false using the [Cluster Update Settings API](https://opensearch.org/docs/latest/api-reference/cluster- api/cluster-settings/).

-
body (Any) – The template definition.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
create – When true, this request cannot replace or update existing component templates. Default is false.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
name

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_decommission_awareness(*, awareness_attribute_name, awareness_attribute_value, params=None, headers=None)`

Decommissions a cluster zone based on awareness. This can greatly benefit multi-zone deployments, where awareness attributes can aid in applying new upgrades to a cluster in a controlled fashion.

### `Parameters:`

-
awareness_attribute_name (Any) – The name of the awareness attribute.

-
awareness_attribute_value (Any) – The value of the awareness attribute. For example, if you have shards allocated in two different zones, you can give each zone a value of zone-a or zoneb. The cluster decommission operation decommissions the zone listed in the method.

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
awareness_attribute_name

-
awareness_attribute_value

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_settings(*, body, params=None, headers=None)`

Updates the cluster settings.

### `Parameters:`

-
body (Any) – The cluster settings to update.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of “cluster”: { “max_shards_per_node”: 500 } is “cluster.max_shards_per_node”: “500”. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_weighted_routing(*, attribute, body=None, params=None, headers=None)`

Updates weighted shard routing weights.

### `Parameters:`

-
attribute (Any) – The name of awareness attribute, usually zone.

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
attribute

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `remote_info(*, params=None, headers=None)`

Returns the information about configured remote clusters.

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

### `reroute(*, body=None, params=None, headers=None)`

Allows to manually change the allocation of individual shards in the cluster.

### `Parameters:`

-
body (Any) – The definition of commands to perform (move, cancel, allocate)

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
dry_run – When true, the request simulates the operation and returns the resulting state.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
explain – When true, the response contains an explanation of why reroute certain commands can or cannot be executed.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
metric – Limits the information returned to the specified metrics.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
retry_failed – When true, retries shard allocation if it was blocked because of too many subsequent failures.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `state(*, metric=None, index=None, params=None, headers=None)`

Returns comprehensive information about the state of the cluster.

### `Parameters:`

-
metric (Any) – Limits the information returned to only the [specified metric groups](https://opensearch.org/docs/latest/api- reference/cluster-api/cluster-stats/#metric-groups).

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – Whether to ignore a wildcard index expression that resolves into no concrete indexes. This includes the _all string or when no indexes have been specified.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Specifies the type of index that wildcard expressions can match. Supports comma-separated values. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of “cluster”: { “max_shards_per_node”: 500 } is “cluster.max_shards_per_node”: “500”. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – Whether the specified concrete indexes should be ignored when unavailable (missing or closed).

-
local – Whether to return information from the local node only instead of from the cluster manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): A duration. Units can be nanos, micros, ms (milliseconds), s (seconds), m (minutes), h (hours) and d (days). Also accepts 0 without a unit and -1 to indicate an unspecified value.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
wait_for_metadata_version – Wait for the metadata version to be equal or greater than the specified metadata version.

-
wait_for_timeout – The maximum time to wait for wait_for_metadata_version before timing out.

-
metric

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `stats(*, node_id=None, params=None, headers=None, metric=None, index_metric=None)`

Returns a high-level overview of cluster statistics.

### `Parameters:`

-
metric (Any) – Limit the information returned to the specified metrics.

-
index_metric (Any) – A comma-separated list of [index metric groups](https://opensearch.org/docs/latest/api-reference/cluster- api/cluster-stats/#index-metric-groups), for example, docs,store.

-
node_id (Any) – A comma-separated list of node IDs used to filter results. Supports [node filters](https://opensearch.org/docs/latest/api- reference/nodes-apis/index/#node-filters).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of “cluster”: { “max_shards_per_node”: 500 } is “cluster.max_shards_per_node”: “500”. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for each node to respond. If a node does not respond before its timeout expires, the response does not include its stats. However, timed out nodes are included in the response’s _nodes.failed property. Defaults to no timeout.

-
node_id

-
params (Any)

-
headers (Any)

-
metric

-
index_metric

### `Return type:`

Any


## Source: `api-ref/clients/dangling_indices_client.html`

## Dangling Indices Client

### `class opensearchpy.client.dangling_indices.DanglingIndicesClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `delete_dangling_index(*, index_uuid, params=None, headers=None)`

Deletes the specified dangling index.

### `Parameters:`

-
index_uuid (Any) – The UUID of the dangling index.

-
accept_data_loss – Must be set to true in order to delete the dangling index.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Specify timeout for connection to cluster manager.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Explicit operation timeout.

-
index_uuid

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `import_dangling_index(*, index_uuid, params=None, headers=None)`

Imports the specified dangling index.

### `Parameters:`

-
index_uuid (Any) – The UUID of the dangling index.

-
accept_data_loss – Must be set to true in order to import the dangling index.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Specify timeout for connection to cluster manager.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Explicit operation timeout.

-
index_uuid

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `list_dangling_indices(*, params=None, headers=None)`

Returns all dangling indexes.

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


## Source: `api-ref/clients/ingest_client.html`

## Ingest Client

### `class opensearchpy.client.ingest.IngestClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `delete_pipeline(*, id, params=None, headers=None)`

Deletes an ingest pipeline.

### `Parameters:`

-
id (Any) – The pipeline ID or wildcard expression of pipeline IDs used to limit the request. To delete all ingest pipelines in a cluster, use a value of *.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

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
timeout – The amount of time to wait for a response.

-
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_pipeline(*, id=None, params=None, headers=None)`

Returns an ingest pipeline.

### `Parameters:`

-
id (Any) – A comma-separated list of pipeline IDs to retrieve. Wildcard (*) expressions are supported. To get all ingest pipelines, omit this parameter or use *.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

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
id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `processor_grok(*, params=None, headers=None)`

Returns a list of built-in grok patterns.

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
s – Determines how to sort returned grok patterns by key name. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_pipeline(*, id, body, params=None, headers=None)`

Creates or updates an ingest pipeline.

### `Parameters:`

-
id (Any) – The ID of the ingest pipeline.

-
body (Any) – The ingest definition.

-
cluster_manager_timeout – The amount of time allowed to establish a connection to the cluster manager node.

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
timeout – The amount of time to wait for a response.

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

### `simulate(*, body, id=None, params=None, headers=None)`

Simulates an ingest pipeline with example documents.

### `Parameters:`

-
body (Any) – The simulate definition

-
id (Any) – The pipeline to test. If you don’t specify a pipeline in the request body, this parameter is required.

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
verbose – When true, the response includes output data for each processor in the pipeline Default is false.

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


## Source: `api-ref/clients/indices_client.html`

## Indices Client

### `class opensearchpy.client.indices.IndicesClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `add_block(*, index, block, params=None, headers=None)`

Adds a block to an index.

### `Parameters:`

-
index (Any) – A comma separated list of indexes to add a block to.

-
block (Any) – The block to add (one of read, write, read_only or metadata).

-
allow_no_indices – Whether to ignore if a wildcard indexes expression resolves into no concrete indexes. (This includes _all string or when no indexes have been specified).

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Whether to expand wildcard expression to concrete indexes that are open, closed or both. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – Whether specified concrete indexes should be ignored when unavailable (missing or closed).

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Specify timeout for connection to cluster manager.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Explicit operation timeout

-
index

-
block

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `analyze(*, body=None, index=None, params=None, headers=None)`

Performs the analysis process on a text and return the tokens breakdown of the text.

### `Parameters:`

-
body (Any) – Define analyzer/tokenizer parameters and the text on which the analysis should be performed

-
index (Any) – The name of the index to scope the operation.

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
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `clear_cache(*, index=None, params=None, headers=None)`

Clears all or specific caches for one or more indexes.

### `Parameters:`

-
index (Any) – A comma-separated list of indexes; use _all or empty string to perform the operation on all indexes.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
fielddata – If true, clears the fields cache. Use the fields parameter to clear the cache of specific fields only.

-
fields – A comma-separated list of field names used to limit the fielddata parameter.

-
file – If true, clears the unused entries from the file cache on nodes with the Search role. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
query – If true, clears the query cache.

-
request – If true, clears the request cache.

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

### `clone(*, index, target, body=None, params=None, headers=None)`

Clones an index.

### `Parameters:`

-
index (Any) – Name of the source index to clone.

-
target (Any) – Name of the target index to create.

-
body (Any) – The configuration for the target index (settings and aliases)

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
task_execution_timeout – Explicit task execution timeout, only useful when wait_for_completion is false, defaults to 1h.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – Should this request wait until the operation has completed before returning. Default is True.

-
index

-
target

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `close(*, index, params=None, headers=None)`

Closes an index.

### `Parameters:`

-
index (Any) – A comma-separated list or wildcard expression of index names used to limit the request.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

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
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create(*, index, body=None, params=None, headers=None)`

Creates an index with optional settings and mappings.

### `Parameters:`

-
index (Any) – The name of the index you wish to create.

-
body (Any) – The configuration for the index (settings and mappings)

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
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

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

### `create_data_stream(*, name, body=None, params=None, headers=None)`

Creates or updates a data stream.

### `Parameters:`

-
name (Any) – Name of the data stream, which must meet the following criteria: Lowercase only; Cannot include /, *, ?, “, <, >, |, ,, #, :, backslash, or a space character; Cannot start with -, _, +, or .ds-; Cannot be . or ..; Cannot be longer than 255 bytes. Multi-byte characters count towards this limit faster.

-
body (Any) – The data stream definition

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
name

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `data_streams_stats(*, name=None, params=None, headers=None)`

Provides statistics on operations happening in a data stream.

### `Parameters:`

-
name (Any) – A comma-separated list of data streams used to limit the request. Wildcard expressions (*) are supported. To target all data streams in a cluster, omit this parameter or use *.

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
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete(*, index, params=None, headers=None)`

Deletes an index.

### `Parameters:`

-
index (Any) – A comma-separated list of indexes to delete. You cannot specify index aliases. By default, this parameter does not support wildcards (*) or _all. To use wildcards or _all, set the action.destructive_requires_name cluster setting to false.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. Default is false.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_alias(*, index, name, params=None, headers=None)`

Deletes an alias.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams or indexes used to limit the request. Supports wildcards (*).

-
name (Any) – A comma-separated list of aliases to remove. Supports wildcards (*). To remove all aliases, use * or _all.

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
index

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_data_stream(*, name, params=None, headers=None)`

Deletes a data stream.

### `Parameters:`

-
name (Any) – A comma-separated list of data streams to delete. Wildcard (*) expressions are supported.

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
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_index_template(*, name, params=None, headers=None)`

Deletes an index template.

### `Parameters:`

-
name (Any) – The name of the index template to delete. Wildcard (*) expressions are supported.

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
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_template(*, name, params=None, headers=None)`

Deletes an index template.

### `Parameters:`

-
name (Any) – The name of the legacy index template to delete. Wildcard (*) expressions are supported.

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
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `exists(*, index, params=None, headers=None)`

Returns information about whether a particular index exists.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases. Supports wildcards (*).

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. Default is false.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – If true, returns settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index. Default is false.

-
include_defaults – If true, return all default settings in the response. Default is false.

-
local – If true, the request retrieves information from the local node only. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

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

### `exists_alias(*, name, index=None, params=None, headers=None)`

Returns information about whether a particular alias exists.

### `Parameters:`

-
name (Any) – A comma-separated list of aliases to check. Supports wildcards (*).

-
index (Any) – A comma-separated list of data streams or indexes used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, requests that include a missing data stream or index in the target indexes or data streams return an error.

-
local – If true, the request retrieves information from the local node only. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `exists_index_template(*, name, params=None, headers=None)`

Returns information about whether a particular index template exists.

### `Parameters:`

-
name (Any) – The name of the index template to check existence of. Wildcard (*) expressions are supported.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – Return settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Return local information, do not retrieve the state from cluster-manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `exists_template(*, name, params=None, headers=None)`

Returns information about whether a particular index template exists.

### `Parameters:`

-
name (Any) – The comma separated names of the index templates

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – Return settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Return local information, do not retrieve the state from cluster-manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `flush(*, index=None, params=None, headers=None)`

Performs the flush operation on one or more indexes.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to flush. Supports wildcards (*). To flush all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
force – If true, the request forces a flush even if there are no changes to commit to the index.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
wait_if_ongoing – If true, the flush operation blocks until execution when another flush operation is running. If false, OpenSearch returns an error if you request a flush when another flush operation is running. Default is True.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `forcemerge(*, index=None, params=None, headers=None)`

Performs the force merge operation on one or more indexes.

### `Parameters:`

-
index (Any) – A comma-separated list of index names; use _all or empty string to perform the operation on all indexes

-
allow_no_indices – Whether to ignore if a wildcard indexes expression resolves into no concrete indexes. (This includes _all string or when no indexes have been specified)

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Whether to expand wildcard expression to concrete indexes that are open, closed or both. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flush – Specify whether the index should be flushed after performing the operation. Default is True.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – Whether specified concrete indexes should be ignored when unavailable (missing or closed)

-
max_num_segments – The number of larger segments into which smaller segments are merged. Set this parameter to 1 to merge all segments into one segment. The default behavior is to perform the merge as necessary.

-
only_expunge_deletes – Specify whether the operation should only expunge deleted documents

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
primary_only – Specify whether the operation should only perform on primary shards. Defaults to false. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
wait_for_completion – Should the request wait until the force merge is completed. Default is True.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get(*, index, params=None, headers=None)`

Returns information about one or more indexes.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and index aliases used to limit the request. Wildcard expressions (*) are supported.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar. Default is false.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard expressions can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma-separated values, such as open,hidden. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – If true, returns settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, requests that target a missing index return an error. Default is false.

-
include_defaults – If true, return all default settings in the response. Default is false.

-
local – If true, the request retrieves information from the local node only. Defaults to false, which means information is retrieved from the cluster-manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

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

### `get_alias(*, index=None, name=None, params=None, headers=None)`

Returns an alias.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams or indexes used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
name (Any) – A comma-separated list of aliases to retrieve. Supports wildcards (*). To retrieve all aliases, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

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
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
index

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_data_stream(*, name=None, params=None, headers=None)`

Returns data streams.

### `Parameters:`

-
name (Any) – A comma-separated list of data stream names used to limit the request. Wildcard (*) expressions are supported. If omitted, all data streams are returned.

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
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_field_mapping(*, fields, index=None, params=None, headers=None)`

Returns mapping for one or more fields.

### `Parameters:`

-
fields (Any) – A comma-separated list or wildcard expression of fields used to limit returned information.

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

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
include_defaults – If true, return all default settings in the response.

-
local – If true, the request retrieves information from the local node only. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
fields

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_index_template(*, name=None, params=None, headers=None)`

Returns an index template.

### `Parameters:`

-
name (Any) – The name of the index template to retrieve. Wildcard (*) expressions are supported.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – If true, returns settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – If true, the request retrieves information from the local node only. Defaults to false, which means information is retrieved from the cluster-manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_mapping(*, index=None, params=None, headers=None)`

Returns mappings for one or more indexes.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

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
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

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

### `get_settings(*, index=None, name=None, params=None, headers=None)`

Returns settings for one or more indexes.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
name (Any) – A comma-separated list or wildcard expression of settings to retrieve.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – If true, returns settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
include_defaults – If true, return all default settings in the response. Default is false.

-
local – If true, the request retrieves information from the local node only. If false, information is retrieved from the cluster-manager node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
index

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_template(*, name=None, params=None, headers=None)`

Returns an index template.

### `Parameters:`

-
name (Any) – A comma-separated list of index template names used to limit the request. Wildcard (*) expressions are supported. To return all index templates, omit this parameter or use a value of _all or *.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – If true, returns settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – If true, the request retrieves information from the local node only. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_upgrade(*, index=None, params=None, headers=None)`

The _upgrade API is no longer useful and will be removed.

### `Parameters:`

-
index (Any) – A comma-separated list of indexes; use _all or empty string to perform the operation on all indexes.

-
allow_no_indices – Whether to ignore if a wildcard indexes expression resolves into no concrete indexes. (This includes _all string or when no indexes have been specified).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Whether to expand wildcard expression to concrete indexes that are open, closed or both. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – Whether specified concrete indexes should be ignored when unavailable (missing or closed).

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

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

### `open(*, index, params=None, headers=None)`

Opens an index.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). By default, you must explicitly name the indexes you using to limit the request. To limit a request using _all, *, or other wildcard expressions, change the action.destructive_requires_name setting to false. You can update this setting in the opensearch.yml file or using the cluster update settings API.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

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
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
task_execution_timeout – Explicit task execution timeout, only useful when wait_for_completion is false, defaults to 1h.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – Should this request wait until the operation has completed before returning. Default is True.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_alias(*, index=None, name=None, body=None, params=None, headers=None)`

Creates or updates an alias.

### `Parameters:`

-
body (Any) – The settings for the alias, such as routing or filter

-
index (Any) – A comma-separated list of data streams or indexes to add. Supports wildcards (*). Wildcard patterns that match both data streams and indexes return an error.

-
name (Any) – Alias to update. If the alias doesn’t exist, the request creates it. Index alias names support date math.

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
index

-
name

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_index_template(*, name, body, params=None, headers=None)`

Creates or updates an index template.

### `Parameters:`

-
name (Any) – Index or template name

-
body (Any) – The template definition

-
cause – User defined reason for creating/updating the index template. Default is false.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
create – If true, this request cannot replace or update existing index templates. Default is false.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Operation timeout for connection to cluster-manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_mapping(*, body, index=None, params=None, headers=None)`

Updates the index mappings.

### `Parameters:`

-
body (Any) – The mapping definition

-
index (Any) – Comma-separated list of indices; use _all or empty string to perform the operation on all indices.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

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
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
write_index_only – If true, the mappings are applied only to the current write index for the target. Default is false.

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

### `put_settings(*, body, index=None, params=None, headers=None)`

Updates the index settings.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. For example, a request targeting foo*,bar* returns an error if an index starts with foo but no index starts with bar.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – If true, returns settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – Whether specified concrete indexes should be ignored when unavailable (missing or closed).

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
preserve_existing – If true, existing index settings remain unchanged. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

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

### `put_template(*, name, body, params=None, headers=None)`

Creates or updates an index template.

### `Parameters:`

-
name (Any) – The name of the template

-
body (Any) – The template definition

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
create – If true, this request cannot replace or update existing index templates. Default is false.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
order – Order in which OpenSearch applies this template if index matches multiple templates. Templates with lower ‘order’ values are merged first. Templates with higher ‘order’ values are merged later, overriding templates with lower values.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `recovery(*, index=None, params=None, headers=None)`

Returns information about ongoing index shard recoveries.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
active_only – If true, the response only includes ongoing shard recoveries. Default is false.

-
detailed – If true, the response includes detailed information about shard recoveries. Default is false.

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
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `refresh(*, index=None, params=None, headers=None)`

Performs the refresh operation in one or more indexes.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

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
pretty – Whether to pretty-format the returned JSON response. Default is false.

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

### `resolve_index(*, name, params=None, headers=None)`

Returns information about any matching indexes, aliases, and data streams.

### `Parameters:`

-
name (Any) – Comma-separated name(s) or index pattern(s) of the indexes, aliases, and data streams to resolve. Resources on remote clusters can be specified using the <cluster>:<name> syntax.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `rollover(*, alias, body=None, new_index=None, params=None, headers=None)`

Updates an alias to point to a new index when the existing index is considered to be too large or too old.

### `Parameters:`

-
alias (Any) – Name of the data stream or index alias to roll over.

-
body (Any) – The conditions that needs to be met for executing rollover

-
new_index (Any) – The name of the index to create. Supports date math. Data streams do not support this parameter.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
dry_run – If true, checks whether the current index satisfies the specified conditions but does not perform a rollover. Default is false.

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
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
alias

-
body

-
new_index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `segments(*, index=None, params=None, headers=None)`

Provides low-level information about segments in a Lucene index.

### `Parameters:`

-
index (Any) – A comma-separated list of data streams, indexes, and aliases used to limit the request. Supports wildcards (*). To target all data streams and indexes, omit this parameter or use * or _all.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

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
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
verbose – If true, the request returns a verbose response. Default is false.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `shard_stores(*, index=None, params=None, headers=None)`

Provides store information for shard copies of indexes.

### `Parameters:`

-
index (Any) – Limits health reporting to a specific source. Can be a single source or a comma-separated list of sources (comprised of data streams, indexes, and aliases).

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes. Default is false.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If true, missing or closed indexes are not included in the response. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
status – A list of shard health statuses used to limit the request. Default is [‘yellow’, ‘red’].

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `shrink(*, index, target, body=None, params=None, headers=None)`

Allow to shrink an existing index into a new index with fewer primary shards.

### `Parameters:`

-
index (Any) – Name of the source index to shrink.

-
target (Any) – Name of the target index to create.

-
body (Any) – The configuration for the target index (settings and aliases)

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
copy_settings – whether or not to copy settings from the source index. Default is false.

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
task_execution_timeout – Explicit task execution timeout, only useful when wait_for_completion is false, defaults to 1h.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – Should this request wait until the operation has completed before returning. Default is True.

-
index

-
target

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `simulate_index_template(*, name, body=None, params=None, headers=None)`

Simulate matching the given index name against the index templates in the system.

### `Parameters:`

-
name (Any) – Index or template name to simulate

-
body (Any) – New index template definition, which will be included in the simulation, as if it already exists in the system

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
name

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `simulate_template(*, body=None, name=None, params=None, headers=None)`

Simulate resolving the given template name or body.

### `Parameters:`

-
name (Any) – The name of the index template to simulate. To test a template configuration before you add it to the cluster, omit this parameter and specify the template configuration in the request body.

-
cause – User defined reason for dry-run creating the new template for simulation purposes. Default is false.

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
create – If true, the template passed in the body is only used if no existing templates match the same index patterns. If false, the simulation uses the template with the highest priority. Note that the template is not permanently added or updated in either case; it is only used for the simulation. Default is false.

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
body (Any)

-
name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `split(*, index, target, body=None, params=None, headers=None)`

Allows you to split an existing index into a new index with more primary shards.

### `Parameters:`

-
index (Any) – Name of the source index to split.

-
target (Any) – Name of the target index to create.

-
body (Any) – The configuration for the target index (settings and aliases)

-
cluster_manager_timeout – Operation timeout for connection to cluster-manager node.

-
copy_settings – whether or not to copy settings from the source index. Default is false.

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
task_execution_timeout – Explicit task execution timeout, only useful when wait_for_completion is false, defaults to 1h.

-
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
wait_for_active_shards – The number of shard copies that must be active before proceeding with the operation. Set to all or any positive integer up to the total number of shards in the index (number_of_replicas+1).

-
wait_for_completion – Should this request wait until the operation has completed before returning. Default is True.

-
index

-
target

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `stats(*, index=None, metric=None, params=None, headers=None)`

Provides statistics on operations happening in an index.

### `Parameters:`

-
index (Any) – A comma-separated list of index names; use _all or empty string to perform the operation on all indexes

-
metric (Any) – Limit the information returned the specific metrics.

-
completion_fields – A comma-separated list or wildcard expressions of fields to include in field data and suggest statistics.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid choices are all, closed, hidden, none, open.

-
fielddata_fields – A comma-separated list or wildcard expressions of fields to include in field data statistics.

-
fields – A comma-separated list or wildcard expressions of fields to include in the statistics.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
forbid_closed_indices – If true, statistics are not collected from closed indexes. Default is True.

-
groups – A comma-separated list of search groups to include in the search statistics.

-
human – Whether to return human-readable values for statistics. Default is false.

-
include_segment_file_sizes – If true, the call reports the aggregated disk usage of each one of the Lucene index files (only applies if segment stats are requested). Default is false.

-
include_unloaded_segments – If true, the response includes information from segments that are not loaded into memory. Default is false.

-
level – Indicates whether statistics are aggregated at the cluster, index, or shard level. Valid choices are cluster, indices, shards.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
index

-
metric

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_aliases(*, body, params=None, headers=None)`

Updates index aliases.

### `Parameters:`

-
body (Any) – The definition of actions to perform

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
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `upgrade(*, index=None, params=None, headers=None)`

The _upgrade API is no longer useful and will be removed.

### `Parameters:`

-
index (Any) – A comma-separated list of indexes; use _all or empty string to perform the operation on all indexes.

-
allow_no_indices – Whether to ignore if a wildcard indexes expression resolves into no concrete indexes. (This includes _all string or when no indexes have been specified).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Whether to expand wildcard expression to concrete indexes that are open, closed or both. Valid choices are all, closed, hidden, none, open.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – Whether specified concrete indexes should be ignored when unavailable (missing or closed).

-
only_ancient_segments – If true, only ancient (an older Lucene major release) segments will be upgraded.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
wait_for_completion – Should this request wait until the operation has completed before returning. Default is false.

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `validate_query(*, body=None, index=None, params=None, headers=None)`

Allows a user to validate a potentially expensive query without executing it.

### `Parameters:`

-
body (Any) – The query definition specified with the Query DSL

-
index (Any) – A comma-separated list of data streams, indexes, and aliases to search. Supports wildcards (*). To search all data streams or indexes, omit this parameter or use * or _all.

-
all_shards – If true, the validation is executed on all shards instead of one random shard per index.

-
allow_no_indices – If false, the request returns an error if any wildcard expression, index alias, or _all value targets only missing or closed indexes. This behavior applies even if the request targets other open indexes.

-
analyze_wildcard – If true, wildcard and prefix queries are analyzed. Default is false.

-
analyzer – Analyzer to use for the query string. This parameter can only be used when the q query string parameter is specified.

-
default_operator – The default operator for query string query: AND or OR. Valid choices are and, or.

-
df – Field to use as default where no field prefix is given in the query string. This parameter can only be used when the q query string parameter is specified.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
expand_wildcards – Type of index that wildcard patterns can match. If the request can target data streams, this argument determines whether wildcard expressions match hidden data streams. Supports comma- separated values, such as open,hidden. Valid values are: all, open, closed, hidden, none.

-
explain – If true, the response returns detailed information if an error has occurred.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – If false, the request returns an error if it targets a missing or closed index.

-
lenient – If true, format-based query failures (such as providing text to a numeric field) in the query string will be ignored.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
q – Query in the Lucene query string syntax.

-
rewrite – If true, returns a more detailed explanation showing the actual Lucene query that will be executed.

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


## Source: `api-ref/clients/nodes_client.html`

## Nodes Client

### `class opensearchpy.client.nodes.NodesClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `hot_threads(*, node_id=None, params=None, headers=None)`

Returns information about hot threads on each node in the cluster.

### `Parameters:`

-
node_id (Any) – A comma-separated list of node IDs or names to limit the returned information; use _local to return information from the node you’re connecting to, leave empty to get information from all nodes.

-
doc_type – The type to sample. Valid choices are block, cpu, wait.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_idle_threads – Whether to show threads that are in known-idle places, such as waiting on a socket select or pulling from an empty task queue. Default is True.

-
interval – The time interval between thread stack trace samples.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
snapshots – The number of thread stack trace samples to collect. Default is 10.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
threads – The number of threads to provide information for. Default is 3.

-
timeout – The amount of time to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
node_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `info(*, node_id=None, metric=None, node_id_or_metric=None, params=None, headers=None)`

Returns information about nodes in the cluster.

### `Parameters:`

-
node_id (Any) – A comma-separated list of node IDs or names used to limit returned information.

-
metric (Any) – Limits the information returned to the specific metrics. Supports a comma-separated list, such as http,ingest.

-
node_id_or_metric (Any) – Limits the information returned to a list of node IDs or specific metrics. Supports a comma-separated list, such as node1,node2 or http,ingest.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
flat_settings – When true, returns settings in flat format. Default is false.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
node_id

-
metric

-
node_id_or_metric

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `reload_secure_settings(*, body=None, node_id=None, params=None, headers=None)`

Reloads secure settings.

### `Parameters:`

-
body (Any) – An object containing the password for the OpenSearch keystore.

-
node_id (Any) – The names of particular nodes in the cluster to target.

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
timeout – The amount of time to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
body

-
node_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `stats(*, node_id=None, metric=None, index_metric=None, params=None, headers=None)`

Returns statistical information about nodes in the cluster.

### `Parameters:`

-
node_id (Any) – A comma-separated list of node IDs or names used to limit returned information.

-
metric (Any) – Limit the information returned to the specified metrics.

-
index_metric (Any) – Limit the information returned for indexes metric to the specified index metrics. It can be used only if indexes (or all) metric is specified.

-
completion_fields – A comma-separated list or wildcard expressions of fields to include in field data and suggest statistics.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
fielddata_fields – A comma-separated list or wildcard expressions of fields to include in field data statistics.

-
fields – A comma-separated list or wildcard expressions of fields to include in the statistics.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
groups – A comma-separated list of search groups to include in the search statistics.

-
human – Whether to return human-readable values for statistics. Default is false.

-
include_segment_file_sizes – When true, reports the aggregated disk usage of each one of the Lucene index files (only applies if segment stats are requested). Default is false.

-
level – Indicates whether statistics are aggregated at the cluster, index, or shard level. Valid choices are cluster, indices, shards.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
types – A comma-separated list of document types for the indexing index metric.

-
node_id

-
metric

-
index_metric

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `usage(*, node_id=None, metric=None, params=None, headers=None)`

Returns low-level information about REST actions usage on nodes.

### `Parameters:`

-
node_id (Any) – A comma-separated list of node IDs or names to limit the returned information; use _local to return information from the node you’re connecting to, leave empty to get information from all nodes

-
metric (Any) – Limits the information returned to the specific metrics. A comma-separated list of the following options: _all, rest_actions.

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
timeout – Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error.

-
node_id

-
metric

-
params (Any)

-
headers (Any)

### `Return type:`

Any


## Source: `api-ref/clients/remote_client.html`

## Remote Client

### `class opensearchpy.client.remote.RemoteClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)


## Source: `api-ref/clients/security_client.html`

## Security Client

### `class opensearchpy.client.security.SecurityClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `authinfo(*, params=None, headers=None)`

Returns or updates authentication information for the currently authenticated user.

### `Parameters:`

-
auth_type – The type of the current authentication request.

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
verbose – Whether to return a verbose response.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `authtoken(*, params=None, headers=None)`

Returns the authorization token for the current user.

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

### `cache(*, params=None, headers=None)`

Not supported for the Cache API.

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

### `change_password(*, body, params=None, headers=None)`

Changes the password for the current user.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `config_upgrade_check(*, params=None, headers=None)`

Checks whether or not an upgrade can be performed and which security resources can be updated.

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

### `config_upgrade_perform(*, body=None, params=None, headers=None)`

Assists the cluster operator with upgrading missing default values and stale default definitions.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_action_group(*, action_group, body, params=None, headers=None)`

Creates or replaces the specified action group.

### `Parameters:`

-
action_group (Any) – The name of the action group to create or replace.

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
action_group

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_allowlist(*, body, params=None, headers=None)`

Creates or replaces APIs permitted for users on the allow list. Requires a super admin certificate or REST API permissions.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_role(*, role, body, params=None, headers=None)`

Creates or replaces the specified role.

### `Parameters:`

-
role (Any) – The name of the role to create.

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
role

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_role_mapping(*, role, body, params=None, headers=None)`

Creates or replaces the specified role mapping.

### `Parameters:`

-
role (Any) – The name of the role for which to create a role mapping.

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
role

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_tenant(*, tenant, body, params=None, headers=None)`

Creates or replaces the specified tenant.

### `Parameters:`

-
tenant (Any) – The name of the tenant to create.

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
tenant

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_update_tenancy_config(*, body, params=None, headers=None)`

Creates or replaces the multi-tenancy configuration. Requires super admin or REST API permissions.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_user(*, username, body, params=None, headers=None)`

Creates or replaces the specified user.

### `Parameters:`

-
username (Any) – The name of the user to create.

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
username

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_user_legacy(*, username, body, params=None, headers=None)`

Creates or replaces the specified user. Legacy API.

### `Parameters:`

-
username (Any) – The name of the user to create.

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
username

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_action_group(*, action_group, params=None, headers=None)`

Deletes the specified action group.

### `Parameters:`

-
action_group (Any) – The name of the action group to delete.

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
action_group

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_distinguished_name(*, cluster_name, params=None, headers=None)`

Deletes all distinguished names in the specified cluster or node allowlist. Requires super admin or REST API permissions.

### `Parameters:`

-
cluster_name (Any) – The cluster name to delete from list of distinguished names.

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
cluster_name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_role(*, role, params=None, headers=None)`

Deletes the specified role.

### `Parameters:`

-
role (Any) – The name of the role to delete.

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
role

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_role_mapping(*, role, params=None, headers=None)`

Deletes the specified role mapping.

### `Parameters:`

-
role (Any) – The name of the role for which to delete the role’s mappings.

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
role

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_tenant(*, tenant, params=None, headers=None)`

Deletes the specified tenant.

### `Parameters:`

-
tenant (Any) – The name of the tenant to delete.

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
tenant

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_user(*, username, params=None, headers=None)`

Deletes the specified internal user.

### `Parameters:`

-
username (Any) – The name of the user to delete.

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
username

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_user_legacy(*, username, params=None, headers=None)`

Delete the specified user. Legacy API.

### `Parameters:`

-
username (Any) – The name of the user to delete.

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
username

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `flush_cache(*, params=None, headers=None)`

Flushes the Security plugin’s user, authentication, and authorization cache.

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

### `generate_obo_token(*, body, params=None, headers=None)`

Generates a On-Behalf-Of token for the current user.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `generate_user_token(*, username, params=None, headers=None)`

Generates an authorization token for the specified user.

### `Parameters:`

-
username (Any) – The name of the user for whom to issue an authorization token.

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
username

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `generate_user_token_legacy(*, username, params=None, headers=None)`

Generates authorization token for the given user. Legacy API. Not Implemented.

### `Parameters:`

-
username (Any) – The name of the user for whom to issue an authorization token.

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
username

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_account_details(*, params=None, headers=None)`

Returns account information for the current user.

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

### `get_action_group(*, action_group, params=None, headers=None)`

Retrieves one action group.

### `Parameters:`

-
action_group (Any) – The name of the action group to retrieve.

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
action_group

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_action_groups(*, params=None, headers=None)`

Retrieves all action groups.

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

### `get_all_certificates(*, params=None, headers=None)`

Retrieves the cluster security certificates.

### `Parameters:`

-
cert_type – The type of certificates (HTTP, TRANSPORT, or ALL) to retrieve from all nodes.

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
timeout – The maximum duration, in seconds, to spend retrieving certificates from all nodes before a timeout.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_allowlist(*, params=None, headers=None)`

Retrieves the current list of allowed APIs accessible to a normal user.

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

### `get_audit_configuration(*, params=None, headers=None)`

Retrieves the audit configuration.

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

### `get_certificates(*, params=None, headers=None)`

Retrieves the cluster security certificates.

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

### `get_configuration(*, params=None, headers=None)`

Returns the current Security plugin configuration in a JSON format.

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

### `get_dashboards_info(*, params=None, headers=None)`

Retrieves the current values for dynamic security settings for OpenSearch Dashboards.

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

### `get_distinguished_name(*, cluster_name, params=None, headers=None)`

Retrieves all node distinguished names. Requires super admin or REST API permissions.

### `Parameters:`

-
cluster_name (Any) – The name of the cluster to retrieve that cluster’s nodes DN settings.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
show_all – Whether to include or exclude any static node’s DN settings from the final result.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
cluster_name

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_distinguished_names(*, params=None, headers=None)`

Retrieves all node distinguished names. Requires super admin or REST API permissions.

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
show_all – Whether to include or exclude any static node’s DN settings from the final result.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_node_certificates(*, node_id, params=None, headers=None)`

Retrieves the specified node’s security certificates.

### `Parameters:`

-
node_id (Any) – The node ID to retrieve certificates for.

-
cert_type – The type of certificates (HTTP, TRANSPORT, or ALL) to retrieve from a node.

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
timeout – The maximum duration, in seconds, to spend retrieving certificates from all nodes before a timeout.

-
node_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_permissions_info(*, params=None, headers=None)`

Retrieves the evaluated REST API permissions for the currently logged in user.

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

### `get_role(*, role, params=None, headers=None)`

Retrieves one role.

### `Parameters:`

-
role (Any) – The name of the role to retrieve.

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
role

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_role_mapping(*, role, params=None, headers=None)`

Retrieves the specified role mapping.

### `Parameters:`

-
role (Any) – The name of the role mapping to retrieve.

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
role

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_role_mappings(*, params=None, headers=None)`

Retrieves all role mappings.

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

### `get_roles(*, params=None, headers=None)`

Retrieves all roles.

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

### `get_sslinfo(*, params=None, headers=None)`

Retrieves information about the SSL configuration.

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
show_dn – Whether to include all domain names in the response.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_tenancy_config(*, params=None, headers=None)`

Retrieves the multi-tenancy configuration. Requires super admin or REST API permissions.

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

### `get_tenant(*, tenant, params=None, headers=None)`

Retrieves the specified tenant.

### `Parameters:`

-
tenant (Any) – The name of the tenant to retrieve.

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
tenant

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_tenants(*, params=None, headers=None)`

Retrieves all tenants.

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

### `get_user(*, username, params=None, headers=None)`

Retrieve information about the specified internal user.

### `Parameters:`

-
username (Any) – The name of the user to retrieve.

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
username

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_user_legacy(*, username, params=None, headers=None)`

Retrieve one user. Legacy API.

### `Parameters:`

-
username (Any) – The name of the user to retrieve.

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
username

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_users(*, params=None, headers=None)`

Retrieve all internal users.

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

### `get_users_legacy(*, params=None, headers=None)`

Retrieve all internal users. Legacy API.

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

### `health(*, params=None, headers=None)`

Checks to see if the Security plugin is running.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
mode – A flag that determines whether to consider the security status before returning a response for a health query response. For example, strict mode indicates service should check the Security plugin status.

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

### `migrate(*, params=None, headers=None)`

Migrates the security configuration from v6 to v7.

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

### `patch_action_group(*, action_group, body, params=None, headers=None)`

Updates the individual attributes of an action group.

### `Parameters:`

-
action_group (Any) – The name of the action group to update.

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
action_group

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_action_groups(*, body, params=None, headers=None)`

Creates, updates, or deletes multiple action groups in a single request.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_allowlist(*, body, params=None, headers=None)`

Updates the current list of APIs accessible for users on the allow list.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_audit_configuration(*, body, params=None, headers=None)`

Updates the specified fields in the audit configuration.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_configuration(*, body, params=None, headers=None)`

Updates the existing security configuration using the REST API. Requires super admin or REST API permissions.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_distinguished_name(*, cluster_name, body=None, params=None, headers=None)`

Updates the distinguished cluster name for the specified cluster. Requires super admin or REST API permissions.

### `Parameters:`

-
cluster_name (Any) – The cluster name to update the nodesDn value.

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
cluster_name

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_distinguished_names(*, body, params=None, headers=None)`

Bulk updates specified node distinguished names. Requires super admin or REST API permissions.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_role(*, role, body, params=None, headers=None)`

Updates the individual attributes of a role.

### `Parameters:`

-
role (Any) – The name of the role to update.

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
role

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_role_mapping(*, role, body, params=None, headers=None)`

Updates the individual attributes of a role mapping.

### `Parameters:`

-
role (Any) – The name of the role to update a role mapping for

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
role

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_role_mappings(*, body, params=None, headers=None)`

Creates or updates multiple role mappings in a single request.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_roles(*, body, params=None, headers=None)`

Creates, updates, or deletes multiple roles in a single call.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_tenant(*, tenant, body, params=None, headers=None)`

Adds, deletes, or modifies a single tenant.

### `Parameters:`

-
tenant (Any) – The name of the tenant to update.

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
tenant

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_tenants(*, body, params=None, headers=None)`

Adds, deletes, or modifies multiple tenants in a single request.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_user(*, username, body, params=None, headers=None)`

Updates individual attributes for an internal user.

### `Parameters:`

-
username (Any) – The name of the user to update.

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
username

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `patch_users(*, body, params=None, headers=None)`

Creates, updates, or deletes multiple internal users in a single request.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `post_dashboards_info(*, params=None, headers=None)`

Retrieves the current values for dynamic security settings for OpenSearch Dashboards.

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

### `reload_http_certificates(*, params=None, headers=None)`

Reloads the HTTP communication certificates.

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

### `reload_transport_certificates(*, params=None, headers=None)`

Reloads the transport communication certificates.

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

### `tenant_info(*, params=None, headers=None)`

Retrieves the names of current tenants. Requires super admin or kibanaserver permissions.

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

### `update_audit_configuration(*, body, params=None, headers=None)`

Updates the audit configuration.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_configuration(*, body, params=None, headers=None)`

Updates the settings for an existing security configuration. Requires super admin or REST API permissions.

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
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_distinguished_name(*, cluster_name, body=None, params=None, headers=None)`

Adds or updates the specified distinguished names in the cluster or node allowlist. Requires super admin or REST API permissions.

### `Parameters:`

-
cluster_name (Any) – The name of the cluster containing the nodesDn value to create or update.

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
cluster_name

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `validate(*, params=None, headers=None)`

Checks whether the v6 security configuration is valid and ready to be migrated to v7.

### `Parameters:`

-
accept_invalid – Whether an invalid v6 configuration should be allowed.

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

### `who_am_i(*, params=None, headers=None)`

Gets the identity information for the user currently logged in.

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

### `who_am_i_protected(*, params=None, headers=None)`

Gets the identity information for the user currently logged in. To use this operation, you must have access to this endpoint when authorization at REST layer is enabled.

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


## Source: `api-ref/clients/snapshot_client.html`

## Snapshot Client

### `class opensearchpy.client.snapshot.SnapshotClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `cleanup_repository(*, repository, params=None, headers=None)`

Removes any stale data from a snapshot repository.

### `Parameters:`

-
repository (Any) – Snapshot repository to clean up.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for a response.

-
repository

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `clone(*, repository, snapshot, target_snapshot, body, params=None, headers=None)`

Creates a clone of all or part of a snapshot in the same repository as the original snapshot.

### `Parameters:`

-
repository (Any) – The name of repository which will contain the snapshots clone.

-
snapshot (Any) – The name of the original snapshot.

-
target_snapshot (Any) – The name of the cloned snapshot.

-
body (Any) – The snapshot clone definition.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
repository

-
snapshot

-
target_snapshot

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create(*, repository, snapshot, body=None, params=None, headers=None)`

Creates a snapshot within an existing repository.

### `Parameters:`

-
repository (Any) – The name of the repository where the snapshot will be stored.

-
snapshot (Any) – The name of the snapshot. Must be unique in the repository.

-
body (Any) – The snapshot definition.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

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
wait_for_completion – When true, the request returns a response when the snapshot is complete. When false, the request returns a response when the snapshot initializes. Default is false.

-
repository

-
snapshot

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_repository(*, repository, body, params=None, headers=None)`

Creates a snapshot repository.

### `Parameters:`

-
repository (Any) – The name for the newly registered repository.

-
body (Any) – The repository definition.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for a response.

-
verify – When true, verifies the creation of the snapshot repository.

-
repository

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete(*, repository, snapshot, params=None, headers=None)`

Deletes a snapshot.

### `Parameters:`

-
repository (Any) – The name of the snapshot repository to delete.

-
snapshot (Any) – A comma-separated list of snapshot names to delete from the repository.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
repository

-
snapshot

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_repository(*, repository, params=None, headers=None)`

Deletes a snapshot repository.

### `Parameters:`

-
repository (Any) – The name of the snapshot repository to unregister. Wildcard (*) patterns are supported.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for a response.

-
repository

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get(*, repository, snapshot, params=None, headers=None)`

Returns information about a snapshot.

### `Parameters:`

-
repository (Any) – A comma-separated list of snapshot repository names used to limit the request. Wildcard (*) expressions are supported.

-
snapshot (Any) – A comma-separated list of snapshot names to retrieve. Also accepts wildcard expressions. (*). To get information about all snapshots in a registered repository, use a wildcard (*) or _all. To get information about any snapshots that are currently running, use _current.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – When false, the request returns an error for any snapshots that are unavailable. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Period to wait for a connection to the cluster-manager node. If no response is received before the timeout expires, the request fails and returns an error.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
verbose – When true, returns additional information about each snapshot, such as the version of OpenSearch which took the snapshot, the start and end times of the snapshot, and the number of shards contained in the snapshot. When false, returns only snapshot names and contained indexes. This is useful when the snapshots belong to a cloud-based repository, where each blob read is a cost or performance concern.

-
repository

-
snapshot

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_repository(*, repository=None, params=None, headers=None)`

Returns information about a snapshot repository.

### `Parameters:`

-
repository (Any) – A comma-separated list of repository names.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
local – Whether to get information from the local node. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
repository

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `restore(*, repository, snapshot, body=None, params=None, headers=None)`

Restores a snapshot.

### `Parameters:`

-
repository (Any) – The name of the repository containing the snapshot

-
snapshot (Any) – The name of the snapshot to restore.

-
body (Any) – Determines which settings and indexes to restore when restoring a snapshot

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
wait_for_completion – Whether to return a response after the restore operation has completed. When false, the request returns a response when the restore operation initializes. When true, the request returns a response when the restore operation completes. Default is false.

-
repository

-
snapshot

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `status(*, repository=None, snapshot=None, params=None, headers=None)`

Returns information about the status of a snapshot.

### `Parameters:`

-
repository (Any) – The name of the repository containing the snapshot.

-
snapshot (Any) – A comma-separated list of snapshot names.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
ignore_unavailable – Whether to ignore any unavailable snapshots, When false, a SnapshotMissingException is thrown. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
repository

-
snapshot

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `verify_repository(*, repository, params=None, headers=None)`

Verifies a repository.

### `Parameters:`

-
repository (Any) – The name of the repository containing the snapshot.

-
cluster_manager_timeout – The amount of time to wait for a response from the cluster manager node. For more information about supported time units, see [Common parameters](https://opensearch.org/docs/latest/api-reference/common- parameters/#time-units).

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
(Deprecated (master_timeout) – To promote inclusive language, use cluster_manager_timeout instead.): Explicit operation timeout for connection to cluster-manager node

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for a response.

-
repository

-
params (Any)

-
headers (Any)

### `Return type:`

Any


## Source: `api-ref/clients/tasks_client.html`

## Tasks Client

### `class opensearchpy.client.tasks.TasksClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `cancel(*, task_id=None, params=None, headers=None)`

Cancels a task, if it can be cancelled through an API.

### `Parameters:`

-
task_id (Any) – The task ID.

-
actions – A comma-separated list of actions that should be returned. Keep empty to return all.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
nodes – A comma-separated list of node IDs or names used to limit the returned information. Use _local to return information from the node you’re connecting to, specify the node name to get information from a specific node, or keep the parameter empty to get information from all nodes.

-
parent_task_id – Returns tasks with a specified parent task ID (node_id:task_number). Keep empty or set to -1 to return all.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
wait_for_completion – Waits for the matching task to complete. When true, the request is blocked until the task has completed. Default is false.

-
task_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get(*, task_id=None, params=None, headers=None)`

Returns information about a task.

### `Parameters:`

-
task_id (Any) – The task ID.

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
timeout – The amount of time to wait for a response.

-
wait_for_completion – Waits for the matching task to complete. When true, the request is blocked until the task has completed. Default is false.

-
task_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `list(*, params=None, headers=None)`

Returns a list of tasks.

### `Parameters:`

-
actions – A comma-separated list of actions that should be returned. Keep empty to return all.

-
detailed – When true, the response includes detailed information about shard recoveries. Default is false.

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
group_by – Groups tasks by parent/child relationships or nodes. Valid choices are nodes, none, parents.

-
human – Whether to return human-readable values for statistics. Default is false.

-
nodes – A comma-separated list of node IDs or names used to limit the returned information. Use _local to return information from the node you’re connecting to, specify the node name to get information from a specific node, or keep the parameter empty to get information from all nodes.

-
parent_task_id – Returns tasks with a specified parent task ID (node_id:task_number). Keep empty or set to -1 to return all.

-
pretty – Whether to pretty-format the returned JSON response. Default is false.

-
source – The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests.

-
timeout – The amount of time to wait for a response.

-
wait_for_completion – Waits for the matching task to complete. When true, the request is blocked until the task has completed. Default is false.

-
params (Any)

-
headers (Any)

### `Return type:`

Any


## Source: `api-ref/clients/features_client.html`

## Features Client

### `class opensearchpy.client.features.FeaturesClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `get_features(params=None, headers=None)`

Gets a list of features which can be included in snapshots using the feature_states field when creating a snapshot

### `Parameters:`

-
(Deprecated (master_timeout) – use cluster_manager_timeout): Explicit operation timeout for connection to master node

-
cluster_manager_timeout – Explicit operation timeout for connection to cluster_manager node

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `reset_features(params=None, headers=None)`

Resets the internal state of features, usually by deleting system indices

Warning

This API is experimental so may include breaking changes or be removed in a future version

### `Parameters:`

-
params (Any)

-
headers (Any)

### `Return type:`

Any
