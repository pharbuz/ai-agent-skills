> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/structuring-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/structuring-commands)

# DQL structuring commands

## expand

Expands an array into separate records. This command takes an array, and for each incoming record, produces as many new records as there are elements in the array of the expression. The number of elements is limited by the `limit` parameter or the length of the array. If the array is empty, no records are produced. Elements are taken from the beginning of the array till the end of the array or the limit.

#### Syntax

`expand [alias =] expression [, limit]`

#### Basic examples

##### Example 1: Expand field and add limit

The following example uses the `expand` command to create new records for each element in the array `a`. Because no alias is specified, the expanded field `a` overwrites the existing array field `a`.
The `limit` parameter limits the number of created records to `2` elements per array.

```
data record(a = array(1, 2), b = "DQL"),
     record(a = array(3, 4, 5), b = "Dynatrace Query Language")
| expand a, limit: 2

```

Query result:ab`1``DQL``2``DQL``3``Dynatrace Query Language``4``Dynatrace Query Language`

##### Example 2: Expand field and introduce a new field

The following example uses the `expand` command to create new records for each element in the array `events`.
The new field `event` contains the created values.

```
data record(ts = toTimestamp("2019-08-01T13:30"), events = array("start", "shutdown", "crash")),
     record(ts = toTimestamp("2019-08-01T14:40"), events = array("start", "shutdown"))
| expand event = events

```

Query result:tseventsevent`2019-08-01T13:30:00.000Z``[start, shutdown, crash]``start``2019-08-01T13:30:00.000Z``[start, shutdown, crash]``shutdown``2019-08-01T13:30:00.000Z``[start, shutdown, crash]``crash``2019-08-01T14:40:00.000Z``[start, shutdown]``start``2019-08-01T14:40:00.000Z``[start, shutdown]``shutdown`

#### Practical example

##### Example: Process groups and their services

The following example shows the process groups and services they run. There is a many-to-many relationship between `dt.entity.service` and `dt.entity.process_group`. The field `runs[dt.entity.service]` represents the relationship and contains an array of services.

```
fetch dt.entity.process_group
| expand dt.entity.service = runs[dt.entity.service]

```

## fieldsFlatten

The `fieldsFlatten` command can be used to extract/flatten fields from a nested record.

#### Syntax

`fieldsFlatten expression [, prefix] [, fields: { [field, …] }] [, depth]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | string |  | An identifier returning the record from which to flatten the fields. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| prefix |  | string |  | Prefix that is applied to all fields that are going to be flattened out. It can't be used together with the fields parameter. Default: The provided field name and a dot. |  |  |  |  |  |  |  |  |  |  |
| fields |  | map of field identifiers and an optional alias |  | Fields from the record that are going to be flattened out. It can't be used together with the prefix parameter. |  |  |  |  |  |  |  |  |  |  |
| depth |  | long |  | Flatten nested records until the specified depth is reached. Must be between `1` and `10`. The default value is `1`. |  |  |  |  |  |  |  |  |  |  |

#### Basic examples

##### Example 1: Extract fields and add prefix

The following example extracts all fields from the nested field `r`.
The extracted fields have the `flat.` prefix.

```
data record(r = record(a = "DQL", b = 1, c = 0)),
     record(r = record(a = "Dynatrace Query Language", b = 2, c = "1"))
| fieldsFlatten r, prefix:"flat."

```

Query result:rflat.aflat.bflat.c**a**: `DQL`
**b**: `1`
**c**: `0``DQL``1``0`**a**: `Dynatrace Query Language`
**b**: `2`
**c**: `1``Dynatrace Query Language``2``1`

##### Example 2: Extract selected fields

The following example extracts the fields `a` and `b` from the nested field `r`.

```
data record(r = record(a = "DQL", b = 1, c = 0)),
     record(r = record(a = "Dynatrace Query Language", b = 2, c = "1"))
| fieldsFlatten r, fields: { a, b }

```

Query result:rab**a**: `DQL`
**b**: `1`
**c**: `0``DQL``1`**a**: `Dynatrace Query Language`
**b**: `2`
**c**: `1``Dynatrace Query Language``2`

##### Example 3: Extract fields with multiple levels of nesting

The following example extracts all fields from the nested field `r` and the nested fields inside `r`.

```
data record(r = record(a = "DQL", b = 1, c = record(d = 0))),
     record(r = record(a = "Dynatrace Query Language", b = 2, c = "1"))
| fieldsFlatten r, depth: 2

```

Query result:

| r |  | r.a |  | r.b |  | r.c.d |  | r.c |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a:`DQL`  b: `1`  c: d: `0` |  | `DQL` |  | `1` |  | `0` |  |  |
| a: `Dynatrace Query Language`  **b**: `2`  **c**: `1` |  | `Dynatrace Query Language` |  | `2` |  |  |  |  |
| `1` |  |  |  |  |  |  |  |  |

#### Practical example

##### Example: Extract offer details

The following query fetches business events of `event.type` `com.easytrade.offer` and parses the `Response` field as nested JSON.
With the `fieldsFlatten` command, the fields from the nested JSON are extracted. The prefix `offerdetails.` is added to every extracted field.

```
fetch bizevents
| filter event.type == "com.easytrade.offer"
| parse Response, "JSON:json"
| fields timestamp, json
| fieldsFlatten json, prefix:"offerdetails."

```
