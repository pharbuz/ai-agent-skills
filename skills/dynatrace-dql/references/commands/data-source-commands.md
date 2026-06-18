> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/data-source-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/data-source-commands)

# DQL data source commands

## data

The `data` command generates sample data during query runtime. It is intended to test and document query scenarios based on a small, exemplary dataset.

-

Based on an input according to the DQL record datatype, or passing a valid JSON string, a tabular list of records is returned.

-

The data command is a starting command which can be used without a pipeline input.

#### Syntax

`data [ records ] [, json: json_string ]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | records |  | record expressions |  | A list of record expressions. Either records or JSON has to be specified. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| json |  | string |  | A string that defines either a single JSON object or a JSON array. Either records or JSON has to be specified. |  |  |  |  |  |  |  |  |  |  |

#### Basic examples

##### Example 1: Create records

In this example, the `data` command generates three heterogeneous records.

```
data record(a = "DQL", b = 1, c = 0),
     record(a = "Dynatrace Query Language", b = 2.9, e = "1"),
     record()

```

Query result:

| a |
| --- |
| b |
| c |
| e |
| `DQL` |
| `1` |
| `0` |
| *null* |
| `Dynatrace Query Language` |
| `2.9` |
| *null* |
| `1` |
| *null* |
| *null* |
| *null* |
| *null* |

##### Example 2: Create records from json

The following example generates records based on a JSON input.
The use of triple double quotes (`"""`) is intentional: in multiline strings, a string surrounded by triple double quotes respects new lines, and you don't need to escape double or single quotes inside the string.

```
data json:"""[
    {
      "amount": 1152,
      "accountId": 12
    },
    {
      "amount": 709,
      "accountId": 96
    }
  ]"""

```

Query result:

| amount |
| --- |
| accountId |
| `1,152` |
| `12` |
| `709` |
| `96` |

## describe

Describes the on-read schema extraction definition for a given data object. It returns the specified fields and their consecutive datatypes. The on-read schema extraction in Grail ensures that every record returned by querying the data of a data object via the `fetch` command will contain at least those fields.

**Known fields:** Fields specified for a data object and returned by the `describe` command or by a DQL statement.

**Unknown/dynamic fields:** Any ingested field not part of the on-read schema extraction definition for a given data object. The field name and datatype are derived at runtime when using a field within a DQL statement.

#### Syntax

`describe dataObject`

#### Basic example

##### Example: Describe business events

The following example uses the `describe` command to retrieve information about all known fields for the `bizevents` data object.

```
describe bizevents

```

Query result:

| field |
| --- |
| data_types |
| `dt.system.table` |
| `[string]` |
| `dt.system.environment` |
| `[string]` |
| `dt.system.bucket` |
| `[string]` |
| `dt.system.segment_id` |
| `[string]` |
| `timestamp` |
| `[timestamp]` |
| `dt.system.sampling_ratio` |
| `[long]` |

## fetch

Loads data from the specified data object.

#### Syntax

`fetch dataObject [, bucket: bucket, …] [, from] [, to] [, timeframe] [, samplingRatio] [, scanLimitGBytes]`

#### Basic examples

##### Example 1: Query logs

Here is an example of the `fetch` command in its simplest form.

```
fetch logs

```

#### Relative query timeframes

All duration literals valid for the [duration data type](/platform/grail/dynatrace-query-language/data-types#duration) are applicable for the `from:` and `to:` parameters.

This example with relative time ranges uses DQL time literals to query logs from the last 25 minutes:

-

On the UI level: in the timeframe selector in the upper-right corner:

- To choose one of the existing values (for example last 72 hours or last 365 days), select **Presets**

- To create your own timeframe value, select **Custom**

- To select the last 2 hours, select **Recent**

-

[On the query level](/platform/grail/dynatrace-query-language/dql-guide#specifytimeframe)

##### Example 2: Query relative timeframe

This example with relative time ranges uses DQL's time literals to set the time frame to query logs with the optional `from` and `to` parameters.

```
fetch logs, from: -24h, to: -2h

```

##### Example 3: Query with absolute timeframe

You can also use absolute time ranges with the `timeframe` parameter.

```
fetch logs, timeframe: "2021-10-20T00:00:00Z/2021-10-28T12:00:00Z"

```

#### Bucket filter

You can use the `bucket` parameter to select the buckets from which to fetch data. To optimize query performance, always limit the query to the relevant buckets.
The `bucket` parameter supports a single or a list of string literals containing the bucket names. Pattern matching using wildcards (`*`) is also supported.

##### Example 4: Query selected buckets

The following example fetches logs from the `default_logs` bucket and all buckets with names starting with `logs_365_`.

```
fetch logs, bucket:{"default_logs", "logs_365_*"}

```

#### Sampling

Currently, to improve query performance, sampling is applicable for **Log data** within the initial `fetch` pipeline stage. Sampling happens vertically across the data, resulting in the selection of a subset of Log records, according to the specified, optional `samplingRatio` parameter.

The applicable value ranges for sampling are:

- 1: Default value, resulting in no applied sampling.

- 10

- 100

- 1000

- 10000

Depending on the specified value, `1/<samplingRatio>` of available raw Log records are returned.

The selected `samplingRatio` is reported in the query result for each record through `dt.system.sampling_ratio`, which is a hidden field. To see the hidden field, you need to select it via the `fields` command.

Sampling in general is non-deterministic, and may return a different result set with each query run. Also, all the following commands will work based on the sampled set of input data, yielding unprecise aggregates.

Furthermore, result sets may vary greatly with different `samplingRatio` values. This is the nature of sampling, as a high sampling ratio is more likely to leave out low-frequency logs. For example, if you had one `ERROR` log among millions of `INFO` logs, `filter loglevel == "ERROR"` would very likely return an empty result set for any sampled data.

##### Example 5: Sampling ratio

The following example estimates the occurrences of ERROR logs across the last 7 days.

- The `fetch` command's `samplingRatio` parameter defines the sampling ratio.

- The `summarize` command, combined with the `countIf` function, counts only error logs.

- You need to multiply the count with the sampling ratio to get an estimation.

```
fetch logs, from: -7d, samplingRatio: 100
| summarize c = countIf(loglevel == "ERROR") * takeAny(dt.system.sampling_ratio)

```

#### Read data limit

The optional `scanLimitGBytes` parameter controls the amount of uncompressed data to be read by the `fetch` stage. The default value is `500GB` unless specified otherwise. If set to `-1`, all data available in the query time range is analyzed.

You need the respective bucket and table permissions to fetch data from the selected table. For details, see [Permissions in Grail](/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table).

## fieldsSnapshot

The `fieldsSnapshot` command returns a snapshot of the fields present in records of the specified data object. For each field, the command reports the percentage of records that contain it as `relative_count`. Use the optional `by:` parameter to break down results by bucket, data type, or other dimensions.
The `fieldsSnapshot` command queries data that is periodically collected for `logs`, `spans`, `smartscape.nodes` and `metrics`. Newly ingested fields can take some time to appear in the output.

#### Syntax

`fieldsSnapshot dataObject [, bucket: {bucket, ...}] [, by: {field, ...}]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| dataObject |  | data object |  | The data object to inspect. Supported values: `logs`, `spans`, `metrics`, `smartscape.nodes`. |  |  |
| bucket |  | `string` (bucket name or pattern) |  | Limits the snapshot to records from the specified buckets. Supports a single name, a list of names, and name patterns (using wildcards `*`). |  |  |
| by |  | field identifier |  | Splits results by one or more dimensions. Supported values are `dt.system.bucket`, `data_type`, or both. For `smartscape.nodes`, you can use `node.type` instead of `dt.system.bucket`. For `metrics`, `metric.key` is additionally supported. The results are aggregated over all omitted dimensions. |  |  |

#### Returns

Each result record contains two fields: `field` and `relative_count`. Additional fields appear only when you specify them in the `by` parameter.

| Field |  | Description |  | field |  | The name of the field. |  | dt.system.bucket |  | The bucket the field was found in. Present only when `dt.system.bucket` is used in `by:`. |  | data_type |  | The data type of the field value. Present only when `data_type` is used in `by:`. |  | node.type |  | The Smartscape node type. Present only when querying `smartscape.nodes` with `by:{node.type}`. |  | metric.key |  | The metric key. Present only when querying metrics with `by:{metric.key}`. |  | relative_count |  | Percentage of records in the given scope that contain this field. The range is `[0.0, 100.0]`. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Basic examples

##### Example 1: List all fields in logs

The following example returns all fields across all log buckets, aggregated into a single list.

```
fieldsSnapshot logs

```

##### Example 2: List fields per bucket

The following example lists fields separately for each log bucket. Use this to quickly compare which fields are present in different parts of your logs.

```
fieldsSnapshot logs, by:{dt.system.bucket}

```

##### Example 3: List fields with data type breakdown

The following example splits results by bucket and data type. `relative_count` informs you what percentage of records in that specific bucket match the field with that exact data type. For example, a result row with `field`: `"content"`, `dt.system.bucket`: `"default_logs"`, `data_type`: `"string"`, and `relative_count`: `97.5` means that 97.5% of records in the `default_logs` bucket have a `content` field with a value of type `string`.

```
fieldsSnapshot logs, by:{dt.system.bucket, data_type}

```

##### Example 4: Find sparsely populated fields

The following example identifies fields that are present in fewer than 10% of log records.

```
fieldsSnapshot logs, by:{dt.system.bucket}
| filter relative_count < 10
| sort relative_count asc

```

The `fieldsSnapshot` command doesn't scan raw data, which means that it doesn't produce any consumption.

You must have at least `read` access to one bucket within the selected data object. The output is automatically filtered to include only data from buckets you have permission to.

## load

Loads data from the specified resource. The `load` command is used with [lookup data](/platform/grail/lookup-data).

#### Syntax

`load tabularFile [, offset]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| tabularFile |  | string |  | The name of the tabular file to load. |  |  |
| offset |  | long |  | The number of skipped records. |  |  |

#### Basic examples

##### Example 1: Query lookup data

The following example shows how to query the content of a tabular file storing lookup data.

```
load "/lookups/pricelist"

```

##### Example 2: Join lookup data

In the following example, lookup data is joined to bizevents records.

```
fetch bizevents
| lookup [ load "/lookups/pricelist" ],​
    sourceField: product.id,​
    lookupField: product.id

```
