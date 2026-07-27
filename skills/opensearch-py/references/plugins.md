# Plugins

> Local snapshot generated from OpenSearch Python Client API Reference on 2026-07-27. Use this file instead of browsing the live documentation during skill execution.


## Source: `api-ref/plugins.html`

## Plugins

- Alerting Plugin
- Index Management Plugin
- ML Commons Plugin


## Source: `api-ref/plugins/alerting_plugin.html`

## Alerting Plugin

### `class opensearchpy.plugins.alerting.AlertingClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `acknowledge_alert(monitor_id, body=None, params=None, headers=None)`

Acknowledges an alert.

### `Parameters:`

-
monitor_id (Any) – The id of the monitor, the alert belongs to

-
body (Any) – The alerts to be acknowledged

-
monitor_id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_destination(body=None, params=None, headers=None)`

Creates a destination for slack, mail, or custom-webhook.

### `Parameters:`

-
body (Any) – The configuration for the destination

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_monitor(body=None, params=None, headers=None)`

Creates a monitor with inputs, triggers, and actions.

### `Parameters:`

-
body (Any) – The configuration for the monitor (inputs, triggers, and actions)

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_destination(destination_id, params=None, headers=None)`

Deletes a specific destination.

### `Parameters:`

-
destination_id (Any) – The id of the destination we are trying to delete

-
destination_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_monitor(monitor_id, params=None, headers=None)`

Deletes a specific monitor.

### `Parameters:`

-
monitor_id (Any) – The id of the monitor we are trying to delete

-
monitor_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_alerts(params=None, headers=None)`

Returns all alerts.

### `Parameters:`

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_destination(destination_id=None, params=None, headers=None)`

Returns the details of a specific destination.

### `Parameters:`

-
destination_id (Any) – The id of the destination we are trying to fetch. If None, returns all destinations

-
destination_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_monitor(monitor_id, params=None, headers=None)`

Returns the details of a specific monitor.

### `Parameters:`

-
monitor_id (Any) – The id of the monitor we are trying to fetch

-
monitor_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `run_monitor(monitor_id, params=None, headers=None)`

Runs/Executes a specific monitor.

### `Parameters:`

-
monitor_id (Any) – The id of the monitor we are trying to execute

-
dryrun – Shows the results of a run without actions sending any message

-
monitor_id

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search_monitor(body, params=None, headers=None)`

Returns the search result for a monitor.

### `Parameters:`

-
monitor_id – The configuration for the monitor we are trying to search

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_destination(destination_id, body=None, params=None, headers=None)`

Updates a destination’s inputs, triggers, and actions.

### `Parameters:`

-
destination_id (Any) – The id of the destination we are trying to update

-
body (Any) – The configuration for the destination

-
destination_id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_monitor(monitor_id, body=None, params=None, headers=None)`

Updates a monitor’s inputs, triggers, and actions.

### `Parameters:`

-
monitor_id (Any) – The id of the monitor we are trying to update

-
body (Any) – The configuration for the monitor (inputs, triggers, and actions)

-
monitor_id

-
body

-
params (Any)

-
headers (Any)

### `Return type:`

Any


## Source: `api-ref/plugins/index_management_plugin.html`

## Index Management Plugin

### `class opensearchpy.plugins.index_management.IndexManagementClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `add_policy(index, body=None, params=None, headers=None)`

Adds a policy to an index. This operation does not change the policy if the index already has one.

### `Parameters:`

-
index (Any) – The name of the index to add policy on

-
index

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `change_policy(index, body=None, params=None, headers=None)`

Updates the managed index policy to a new policy (or to a new version of the policy).

### `Parameters:`

-
index (Any) – The name of the index to change policy on

-
index

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_policy(policy, params=None, headers=None)`

Deletes the policy by policy_id.

### `Parameters:`

-
policy (Any) – The name of the policy to delete

-
policy

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `explain_index(index, params=None, headers=None)`

Gets the current state of the index.

### `Parameters:`

-
index (Any) – The name of the index to explain

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_policy(policy=None, params=None, headers=None)`

Gets the policy by policy_id; returns all policies if no policy_id is provided.

### `Parameters:`

-
policy (Any) – The name of the policy

-
policy

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `put_policy(policy, body=None, params=None, headers=None)`

Creates, or updates, a policy.

### `Parameters:`

-
policy (Any) – The name of the policy

-
policy

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `remove_policy_from_index(index, params=None, headers=None)`

Removes any ISM policy from the index.

### `Parameters:`

-
index (Any) – The name of the index to remove policy on

-
index

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `retry(index, body=None, params=None, headers=None)`

Retries the failed action for an index.

### `Parameters:`

-
index (Any) – The name of the index whose is in a failed state

-
index

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any


## Source: `api-ref/plugins/ml_plugin.html`

## ML Commons Plugin

### `class opensearchpy.plugins.ml.MlClient(client)`

Bases: NamespacedClient

### `Parameters:`

client (Any)

### `add_agentic_memory(*, memory_container_id, body=None, params=None, headers=None)`

Add agentic memory to a memory container.

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
memory_container_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `chunk_model(*, model_id, chunk_number, body=None, params=None, headers=None)`

Uploads model chunk.

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
model_id (Any)

-
chunk_number (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_connector(*, body=None, params=None, headers=None)`

Creates a standalone connector.

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

### `create_controller(*, model_id, body=None, params=None, headers=None)`

Creates a controller.

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
model_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_memory(*, body=None, params=None, headers=None)`

Create a memory.

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

### `create_memory_container(*, body=None, params=None, headers=None)`

Create a memory container.

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

### `create_memory_container_session(*, memory_container_id, body=None, params=None, headers=None)`

Create session in a memory container.

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
memory_container_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_message(*, memory_id, body=None, params=None, headers=None)`

Create a message.

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
memory_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `create_model_meta(*, body=None, params=None, headers=None)`

Registers model metadata.

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

### `delete_agent(*, agent_id, params=None, headers=None)`

Delete an agent.

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
agent_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_agentic_memory(*, memory_container_id, doc_type, id, params=None, headers=None)`

Delete a specific memory by its type and ID.

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
memory_container_id (Any)

-
doc_type (Any)

-
id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_agentic_memory_query(*, memory_container_id, doc_type, body=None, params=None, headers=None)`

Delete multiple memories using a query to match specific criteria.

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
memory_container_id (Any)

-
doc_type (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_connector(*, connector_id, params=None, headers=None)`

Deletes a standalone connector.

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
connector_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_controller(*, model_id, params=None, headers=None)`

Deletes a controller.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_memory(*, memory_id, params=None, headers=None)`

Delete a memory.

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
memory_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_memory_container(*, memory_container_id, params=None, headers=None)`

Delete a memory container.

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
memory_container_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_model(*, model_id, params=None, headers=None)`

Deletes a model.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_model_group(*, model_group_id, params=None, headers=None)`

Deletes a model group.

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
model_group_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `delete_task(*, task_id, params=None, headers=None)`

Deletes a task.

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
task_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `deploy_model(*, model_id, params=None, headers=None)`

Deploys a model.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `execute_agent(*, agent_id, body=None, params=None, headers=None)`

Execute an agent.

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
agent_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `execute_agent_stream(*, agent_id, body=None, params=None, headers=None)`

Execute an agent in streaming mode.

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
agent_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `execute_algorithm(*, algorithm_name, body=None, params=None, headers=None)`

Execute an algorithm.

### `Parameters:`

-
algorithm_name (Any) – The function name.

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
algorithm_name

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `execute_tool(*, tool_name, body=None, params=None, headers=None)`

Execute a tool.

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
tool_name (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_agent(*, agent_id, params=None, headers=None)`

Get an agent.

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
agent_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_agentic_memory(*, memory_container_id, doc_type, id, params=None, headers=None)`

Get a specific memory by its type and ID.

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
memory_container_id (Any)

-
doc_type (Any)

-
id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_all_memories(*, params=None, headers=None)`

Get all memories.

### `Parameters:`

-
error_trace – Whether to include the stack trace of returned errors. Default is false.

-
filter_path – A comma-separated list of filters used to filter the response. Use wildcards to match any field or part of a field’s name. To exclude fields, use -.

-
human – Whether to return human-readable values for statistics. Default is false.

-
max_results – The maximum number of results to return. If there are fewer memories than the number set in max_results, the response returns only the number of memories that exist. Default is 10.

-
next_token – The index of the first memory in the sorted list of memories to return. Memories are ordered by create_time. For example, if memories A, B, and C exist, next_token=1 returns memories B and C. Default is 0 (return all memories).

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

### `get_all_messages(*, memory_id, params=None, headers=None)`

Get all messages in a memory.

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
memory_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_all_tools(*, params=None, headers=None)`

Get tools.

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

### `get_connector(*, connector_id, params=None, headers=None)`

Retrieves a standalone connector.

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
connector_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_controller(*, model_id, params=None, headers=None)`

Retrieves a controller.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_memory(*, memory_id, params=None, headers=None)`

Get a memory.

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
memory_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_memory_container(*, memory_container_id, params=None, headers=None)`

Get a memory container.

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
memory_container_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_message(*, message_id, params=None, headers=None)`

Get a message.

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
message_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_message_traces(*, message_id, params=None, headers=None)`

Get a message traces.

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
message_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_model(*, model_id, params=None, headers=None)`

Retrieves a model.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_model_group(*, model_group_id, params=None, headers=None)`

Retrieves a model group.

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
model_group_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_profile(*, body=None, params=None, headers=None)`

Get a profile.

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

### `get_profile_models(*, body=None, model_id=None, params=None, headers=None)`

Get a profile models.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_profile_tasks(*, body=None, task_id=None, params=None, headers=None)`

Get a profile tasks.

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
task_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_stats(*, node_id=None, stat=None, params=None, headers=None)`

Get stats.

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
node_id (Any)

-
stat (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_task(*, task_id, params=None, headers=None)`

Retrieves a task.

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
task_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `get_tool(*, tool_name, params=None, headers=None)`

Get tools.

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
tool_name (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `load_model(*, model_id, params=None, headers=None)`

Deploys a model.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `predict(*, algorithm_name, model_id, body=None, params=None, headers=None)`

Predicts new data with trained model.

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
algorithm_name (Any)

-
model_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `predict_model(*, model_id, body=None, params=None, headers=None)`

Predicts a model.

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
model_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `predict_model_stream(*, model_id, body=None, params=None, headers=None)`

Predicts a model in streaming mode.

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
model_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `register_agents(*, body=None, params=None, headers=None)`

Register an agent.

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

### `register_model(*, body=None, params=None, headers=None)`

Registers a model.

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

### `register_model_group(*, body=None, params=None, headers=None)`

Registers a model group.

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

### `register_model_meta(*, body=None, params=None, headers=None)`

Registers model metadata.

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

### `search_agentic_memory(*, memory_container_id, doc_type, body=None, params=None, headers=None)`

Search for memories of a specific type within a memory container.

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
memory_container_id (Any)

-
doc_type (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search_agents(*, body=None, params=None, headers=None)`

Search agents.

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

### `search_connectors(*, body=None, params=None, headers=None)`

Searches for standalone connectors.

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

### `search_memory(*, body=None, params=None, headers=None)`

Search memory.

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

### `search_memory_container(*, body=None, params=None, headers=None)`

Search memory containers.

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

### `search_message(*, memory_id, body=None, params=None, headers=None)`

Search messages.

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
memory_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `search_model_group(*, body=None, params=None, headers=None)`

Searches for model groups.

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

### `search_models(*, body=None, params=None, headers=None)`

Searches for models.

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

### `search_tasks(*, body=None, params=None, headers=None)`

Searches for tasks.

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

### `train(*, algorithm_name, body=None, params=None, headers=None)`

Trains a model synchronously.

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
algorithm_name (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `train_predict(*, algorithm_name, body=None, params=None, headers=None)`

Trains a model and predicts against the same training dataset.

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
algorithm_name (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `undeploy_model(*, body=None, model_id=None, params=None, headers=None)`

Undeploys a model.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `unload_model(*, body=None, model_id=None, params=None, headers=None)`

Unloads a model.

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
model_id (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_agentic_memory(*, memory_container_id, doc_type, id, body=None, params=None, headers=None)`

Update a specific memory by its type and ID.

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
memory_container_id (Any)

-
doc_type (Any)

-
id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_connector(*, connector_id, body=None, params=None, headers=None)`

Updates a standalone connector.

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
connector_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_controller(*, model_id, body=None, params=None, headers=None)`

Updates a controller.

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
model_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_memory(*, memory_id, body=None, params=None, headers=None)`

Update a memory.

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
memory_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_memory_container(*, memory_container_id, body=None, params=None, headers=None)`

Update a memory container.

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
memory_container_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_message(*, message_id, body=None, params=None, headers=None)`

Update a message.

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
message_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_model(*, model_id, body=None, params=None, headers=None)`

Updates a model.

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
model_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `update_model_group(*, model_group_id, body=None, params=None, headers=None)`

Updates a model group.

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
model_group_id (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `upload_chunk(*, model_id, chunk_number, body=None, params=None, headers=None)`

Uploads model chunk.

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
model_id (Any)

-
chunk_number (Any)

-
body (Any)

-
params (Any)

-
headers (Any)

### `Return type:`

Any

### `upload_model(*, body=None, params=None, headers=None)`

Registers a model.

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
