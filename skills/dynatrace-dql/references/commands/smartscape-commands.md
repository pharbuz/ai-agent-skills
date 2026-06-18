> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands)

# DQL Smartscape commands

This page describes Smartscape commands in DQL.
For more information about the new Smartscape model and model definitions for entities, see the [Semantic Dictionary](/semantic-dictionary/model/smartscape).

## smartscapeNodes

Loads Smartscape nodes using a type pattern (use `*` for all types).

#### Syntax

`smartscapeNodes type [, from] [, to] [, timeframe], ...`

##### Parameters

| Parameter |  | Type |  | Description |  | Required |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| type |  | string, identifier, string pattern |  |  |  |  |  |  |
|  |  | timeframe |  | timeframe, string |  | The desired timeframe (if not specified, global timeframe is used). |  |  |
| from |  | timestamp, duration, string |  | The start of the timeframe (if no explicit timeframe is specified). A duration is interpreted as an offset from [`now()`](/platform/grail/dynatrace-query-language/functions/time-functions#now). |  |  |  |  |
| to |  | timestamp, duration, string |  | The end of the timeframe (if no explicit timeframe is specified). A duration is interpreted as an offset from [`now()`](/platform/grail/dynatrace-query-language/functions/time-functions#now). |  |  |  |  |

#### Basic examples

##### Example 1

Get a list of all unique smartscapeNodes.

```
smartscapeNodes "*"
| fields type
| dedup type

```

##### Example 2

Get a list of the first 10 `HOST` nodes.

```
smartscapeNodes HOST
| fields id, type
| limit 10

```

##### Example 3

Get a list of the first 10 `HOST` and `PROCESS` nodes.

```
smartscapeNodes { HOST, PROCESS }
| fields id, type
| limit 10

```

#### Working with node type patterns

The `smartscapeNodes` command supports node type patterns using wildcards. To match any sequence of zero or more characters in the node type, you can use a `*` character anywhere in the pattern. A pattern supports a maximum of 64 wildcard characters. Consecutive wildcards (for example, `**`) aren't supported.

##### Example 4

Get a list of the first 10 nodes fitting the pattern `*EC2*`.

```
smartscapeNodes "*EC2*"
| fields id, type
| limit 10

```

## smartscapeEdges

Loads Smartscape edges using an edge type pattern (use `*` for all types).

#### Syntax

`smartscapeEdges type [, from] [, to] [, timeframe ,] ...`

##### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timeframe |  | timeframe, string |  | The desired timeframe (if not specified, global timeframe is used). |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| from |  | timestamp, duration, string |  | The start of the timeframe (if no explicit timeframe is specified). A duration is interpreted as an offset from [`now()`](/platform/grail/dynatrace-query-language/functions/time-functions#now). |  |  |  |  |  |  |  |  |  |  |
| to |  | timestamp, duration, string |  | The end of the timeframe (if no explicit timeframe is specified). A duration is interpreted as an offset from [`now()`](/platform/grail/dynatrace-query-language/functions/time-functions#now). |  |  |  |  |  |  |  |  |  |  |
| type |  | string, identifier, string pattern |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Basic examples

##### Example 1

Get a list of all `runs_on` edges.

```
smartscapeEdges runs_on

```

##### Example 2

Get a list of all edges starting at Kubernetes Pods.

```
smartscapeEdges "*"
| filter source_type == "K8S_POD"
| summarize by:{type, target_type}, edges = count()

```

##### Example 3

Get a list of all entity types that have a `belongs_to` edge leading to a Kubernetes Namespace.

```
smartscapeEdges belongs_to
| filter target_type == "K8S_NAMESPACE"
| dedup source_type
| fields source_type

```

##### Example 4

Get a list of all Kubernetes Deployment IDs that belong to a Kubernetes Namespace with a specific owner tag.

```
smartscapeEdges belongs_to
| filter source_type == "K8S_DEPLOYMENT" and target_type == "K8S_NAMESPACE"
| fieldsAdd namespace_tags = getNodeField(target_id, "tags")
| filter namespace_tags[owner] == "john.doe@example.com"
| fields source_id

```

#### Working with edge type patterns

The `smartscapeEdges` command supports edge type patterns using wildcards. To match any sequence of zero or more characters in the edge type, you can use a `*` character anywhere in the pattern. A pattern supports a maximum of 64 wildcard characters. Consecutive wildcards (for example, `**`) aren't supported.

##### Example 5

Get a list of all entity types that have `*to` edges (for example, `is_attached_to` and `belongs_to`) leading to a Kubernetes Namespace.

```
smartscapeEdges "*to"
| filter target_type == "K8S_NAMESPACE"
| dedup source_type
| fields source_type

```

## traverse

Traverses source nodes to target nodes in the specified direction, following edge types defined by edgeTypes.

The `traverse` command follows the `smartscapeNodes` command. As an input for the source node, it takes records containing `nodeId`.

The command returns the target node with an additional field - `dt.traverse.history`, which is an array of records containing information about the source node. Every traverse operation adds a single record to `dt.traverse.history`. By default, the record contains the following fields: `id`, `edge_type`, and `direction`. More fields can be added to the record using the command's `fieldsKeep` parameter.

#### Syntax

`traverse edgeType, …, targetType, … [, direction] [, fieldsKeep: field, …] [, nodeId]`

##### Parameters

| Parameter |  | Type |  | Description |  | Required |  | edgeType |  | string, identifier, string pattern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |
| targetType |  | string, identifier, string pattern |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| direction |  | enumeration |  | The traversal direction. The possible values are: `forward`, `backward`. The default value is: `forward`. |  |  |  |  |  |  |
| fieldsKeep |  | string, field identifier, string pattern |  | A list of fields from the source node that should be preserved in `dt.traverse.history` column. |  |  |  |  |  |  |
| nodeId |  | field identifier |  | The field that contains the id of the source node that should be traversed. The default value is: `id`. |  |  |  |  |  |  |

#### Basic examples

##### Example 1

Traverse from all `PROCESS` nodes to the `HOST` they run on, keeping each process name in the traverse history.

```
smartscapeNodes PROCESS
 | traverse runs_on, HOST, direction: forward, fieldsKeep: name

```

##### Example 2

Get a list of all Kubernetes Services that belong to Kubernetes Namespaces with a specific annotation.

```
smartscapeNodes K8S_NAMESPACE
| filter tags[`example.com/annotation`] == "my-annotation"
| traverse belongs_to, K8S_SERVICE, direction: backward

```

##### Example 3

Get a list of process names and host names for all processes with a specific exe name by using the `fieldsKeep` parameter and accessing the `dt.traverse.history` field.

```
smartscapeNodes PROCESS
| filter process.metadata[EXE_NAME] == "envoy"
| traverse runs_on, HOST, fieldsKeep:name
| fields process_name = dt.traverse.history[0][name], host_name = name

```

##### Example 4

Find all EC2 volumes owned by a certain team that are attached to EC2 Instances.

```
smartscapeNodes AWS_EC2_INSTANCE
| filter tags[dt_owner_team] == "team-piranhas"
| traverse is_attached_to, AWS_EC2_VOLUME, direction: backward

```

#### Working with type patterns

The `traverse` command supports node type and edge type patterns using wildcards. To match any sequence of zero or more characters in the type, you can use a `*` character anywhere in the pattern. A pattern supports a maximum of 64 wildcard characters. Consecutive wildcards (for example, `**`) aren't supported.
