> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/metric-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/metric-commands)

# DQL metric commands

## timeseries

The `timeseries` command is a starting command of DQL. It combines loading, filtering and aggregating metrics data into a time series output.

#### Syntax

`timeseries [column =] aggregation(metricKey [, filter:] [, default:] [, rollup:] [, rate:] [, scalar:]) [, [column =] aggregation(metricKey, ...), ...] [, by:] [, filter:] [, union:] [, nonempty:] [, interval: | bins:] [, from:] [, to:] [,timeframe:] [,shift:] [,bucket: bucket, …]`

#### Basic examples

##### Example 1

```
timeseries usage=avg(dt.host.cpu.usage)

```

##### Example 2

```
timeseries min_cpu=min(dt.host.cpu.usage), max(dt.host.cpu.usage, default:99.9), by:dt.entity.host, filter:in(dt.entity.host, "HOST-1", "HOST-2"), interval:1h, from:-7d

```

#### Timeseries response

The `timeseries` command produces homogenous time series of aggregated data: all series have identical start and end timestamps, time interval and number of elements. The `timeframe` column holds the start and end timestamps. The `interval` column holds the time interval expressed as a `duration`. Each aggregation (`sum`, `avg`, `min`, `max`, `count`, `percentile` and `countDistinct`)
produces a column with the specified column name or a name derived from the aggregation expression. Each aggregation cell consists of the entire array of aggregated values for each time slot defined by `timeframe` and `interval`.

Here is an example of the result of the `timeseries` command. Note that:

- the first aggregation column name has been specified in the query (`min_cpu`)

- the second aggregation column name has not been specified in the query, hence the name is derived from the expression (`max(dt.host.cpu.usage)`)

- the first aggregation does not specify a `default` parameter, hence it can contain `null` for empty time slots

- the second aggregation does specify a `default` parameter, hence the empty time slots are replaced with the `default` value (`99.9` in this example)

| timeframe |
| --- |
| interval |
| dt.entity.host |
| min_cpu |
| max(dt.host.cpu.usage) |
| `{"start":"2022-10-24T07:00:00","end":"2022-10-31T07:00:00"}` |
| `"1h"` |
| `HOST-1` |
| `[35.1,35.9,35.5,36.7,...,37.9,39.4]` |
| `[36.9,37.8,38.8,38.8,...,38.6,39.5]` |
| `{"start":"2022-10-24T07:00:00","end":"2022-10-31T07:00:00"}` |
| `"1h"` |
| `HOST-2` |
| `[24.9,25.1,null,25.0,...,23.8,24.5]` |
| `[30.9,31.3,99.9,32.7,...,33.1,37.1]` |

#### Aggregation functions

You can use the following aggregation functions with the `timeseries` command:

- `sum` - Calculates the sum of the metric in each time slot.

- `avg` - Calculates the average of the metric in each time slot.

- `min` - Calculates the minimum of the metric in each time slot.

- `max` - Calculates the maximum of the metric in each time slot.

- `count` - Calculates the number of distinct metric series in each timeslot (cardinality).

- `percentile` - Calculates the percentile of the metric in each time slot. It applies to metrics of type `histogram`. If the metric is a `gauge` or a `count`, the `rollup` parameter needs to be specified.

- `percentRank` - Calculates the percentile rank for a given value. It applies to metrics of type `histogram`. If the metric is a `gauge` or a `count`, the `rollup` parameter needs to be specified. This aggregation is the inverse of the `percentile` aggregation, it returns the fraction of values that are below the provided parameter. The calculated value is a number between `0.0` and `1.0`.

-  `countDistinct` - Calculates an approximate count of distinct values in each timeslot. It applies to metrics of type `cardinality`.

It is also possible to use the following functions. However, they need to be used with one of the above aggregation functions:

- `start` - Generates the start timestamp of the timeslot.

- `end` - Generates the end timestamp of the timeslot.

##### Syntax

These functions have the following syntax:

- `sum(metric.key [, filter:] [, default:] [, rollup:] [, rate:] [, scalar:])`

- `avg(metric.key [, filter:] [, default:] [, rollup:] [, rate:] [, scalar:])`

- `min(metric.key [, filter:] [, default:] [, rollup:] [, rate:] [, scalar:])`

- `max(metric.key [, filter:] [, default:] [, rollup:] [, rate:] [, scalar:])`

- `count(metric.key [, filter:] [, default:] [, scalar:])`

- `percentile(metric.key, percentile [, filter:] [, default:] [, rollup:] [, rate:] [, scalar:])`

- `percentRank(metric.key, value [, filter:] [, default:] [, rollup:]  [, rate:] [, scalar:])`

- `countDistinct(metric.key [, filter:] [, default:] [, scalar:])`

- `start()`

- `end()`

##### Parameters

| Parameter |  | Type |  | Description |  | Required |  | metric key |  | metric key identifier |  | The metric key the series should be created for. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rollup |  | enumeration |  | The time rollup that should be used for the aggregation. Can be `min`, `max`, `sum`, `avg`, `total`. |  |  |  |  |  |  |  |  |  |  |
| default |  | number |  | The default value that should be used to fill empty time slots. The default value is null. |  |  |  |  |  |  |  |  |  |  |
| rate |  | duration |  | The duration that should be used to adjust the values using the following formula: `(value / interval) * rate`. |  |  |  |  |  |  |  |  |  |  |
| percentile |  | double, long |  | The nth-percentile, such that approximately n percent of observed measurements fall below this value. Must be between 0 and 100. |  |  |  |  |  |  |  |  |  |  |
| scalar |  | boolean |  | Flag to indicate that a single value spanning the whole timeframe shall be calculated. Can be used on any aggregation function except `start` and `end`. |  |  |  |  |  |  |  |  |  |  |
| filter |  | boolean |  | An additional filter condition that shall be applied on the source records before time-/space-aggregation. If all aggregations are filtering on the same condition, the global `filter` parameter can be used over specifying the same condition in each aggregation individually. |  |  |  |  |  |  |  |  |  |  |
| value |  | double, long |  | The value for which to retrieve the percentile. |  |  |  |  |  |  |  |  |  |  |

##### Example 1

```
timeseries sum(dt.host.availability)

```

##### Example 2

```
timeseries avg(dt.host.cpu.idle, rollup: avg, default: 0, rate: 10m)

```

##### Example 3

```
timeseries min(dt.host.cpu.iowait, default: -1), by: dt.entity.host

```

##### Example 4

```
timeseries max(dt.host.cpu.iowait, default: -1), by: dt.entity.host

```

##### Example 5

```
timeseries count(dt.host.cpu.load), by: dt.entity.host

```

##### Example 6

```
timeseries p99=percentile(dt.service.request.response_time, 99),
by:{dt.entity.service}
| limit 5

```

##### Example 7

```
timeseries rank=percentRank(dt.service.request.response_time, 70000),
// The upper value should use the same unit as the metric.
// The dt.service.request.response_time metric is reported in microseconds.
// 70000 means 70000 microseconds (us) or 70 milliseconds (ms).
by:{dt.entity.service}
| limit 5

```

##### Example 8

```
timeseries countDistinct(dt.frontend.user.active.estimated_count)

```

##### Example 9

```
timeseries min(dt.host.cpu.load), start(), end()

```

#### Aggregating multiple timeseries

Multiple timeseries can be aggregated using the `summarize` command with an iterative expression in the aggregation function. The `min`, `max`, `sum` and `avg` aggregation functions support iterative expressions.

##### Example

This example shows how to use the aggregation functions with iterative expressions.

```
timeseries usage=avg(dt.host.cpu.usage), by: dt.entity.host
| fieldsAdd entityName(dt.entity.host)
| filter dt.entity.host.name == "EasyTrade"
| summarize usage=avg(usage[]), by:{timeframe, interval}

```

#### Percentile aggregation

When used with the `timeseries` command, the `percentile` aggregation returns an estimated percentile. The estimates are not guaranteed to be exact but are accurate to ~2.2%. For example, if the estimated 90th percentile is 679 ms, then the exact, actual 90th percentile is between 664 - 693 ms.

In exceptional circumstances, a higher error guarantee may be necessary to optimize for exceptionally skewed distributions.
Two metrics support `timeseries percentile` without a `rollup` parameter:

- `dt.service.request.response_time`

- `dt.service.request.service_mesh.response_time`

All other metrics must use the `rollup` parameter, for example, to calculate the 90th percentile average CPU usage:

```
timeseries percentile(dt.host.cpu.usage, 90, rollup:avg)

```

When you use the percentile function for buckets from histograms ingested via OTLP or from Prometheus:

- It isn't guaranteed to align with the PromQL implementation.

- Percentile estimates cannot be smaller than `float.MIN_VALUE` or larger than `float.MAX_VALUE`.

#### Default value for empty time slots

The `timeseries` command produces homogenous time series of aggregated data: all series have identical start and end timestamps, time interval and number of elements. If data is missing for a particular time slot, it is filled with `null`. Specifying a `default` parameter fills empty time slots with the `default` parameter value instead of `null`.

The `timeseries` command might not return any data. This can be a challenge when combining two metrics—for example, when calculating the percentage of all HTTP responses that are HTTP 503 responses. If the `timeseries` command returns no records (no HTTP 503 responses were found), the expected result is `0%`, but the actual result is empty, because, the default value of a `nonempty` parameter is `false`.

##### Example 1

```
timeseries http_503=sum(http_requests),
filter:{code==503}
| join on:interval, [timeseries http_total=sum(http_requests)], fields:{http_total}
| fieldsAdd ratio=http_503[]/http_total[]*100

```

Query result:

http_503

http_total

ratio

No records

No records

No records

##### Example 2

To achieve the desired result, you can combine the `nonempty` and `default` parameters.

```
timeseries http_503=sum(http_requests, default:0), filter:{code==503}, nonempty:true
| join on:interval, [timeseries http_total=sum(http_requests)], fields:{http_total}
| fieldsadd ratio=http_503[]/http_total[]*100

```

Query result:

| … |
| --- |
| http_503 |
| http_total |
| ratio |
| … |
| `[0,0,0,0]` |
| `[1,5,2,4]` |
| `[0,0,0,0]` |

#### Rate normalization

The `rate` parameter divides the aggregated timeseries by the interval to normalize the timeseries to the selected specified duration. For instance, if `timeseries sum(dt.requests.failed)` returns `[300,300,600,900]` with a `5m` interval, then `timeseries sum(dt.requests.failed, rate:1s)` would return `[1,1,2,3]`.

#### Join behavior (union parameter)

The `union` parameter controls the way multiple series are combined when series are absent from one or more columns. The default is `union:false` meaning only series that are present on all columns are returned (equivalent to an intersection of the results, or SQL's `INNER JOIN`). Specifying `union:true` results in all matching series with possibly empty columns (equivalent to an union of the results, or SQL's `OUTER JOIN`).

For example, assuming two metrics `dt.requests.failed` and `dt.requests.success` and 3 hosts,

Results of `timeseries failed=sum(dt.requests.failed), by:host`

| host |
| --- |
| failed |
| `HOST-1` |
| `[1,1,1,1]` |
| `HOST-2` |
| `[2,2,2,2]` |

Results of `timeseries success=sum(dt.requests.success), by:host`

| host |
| --- |
| success |
| `HOST-2` |
| `[20,20,20,20]` |
| `HOST-3` |
| `[30,30,30,30]` |

Results of `timeseries failed=sum(dt.requests.failed), success=sum(dt.requests.success), by:host`

| host |
| --- |
| failed |
| success |
| `HOST-2` |
| `[2,2,2,2]` |
| `[20,20,20,20]` |

Results of `timeseries failed=sum(dt.requests.failed), success=sum(dt.requests.success), by:host, union:true`

| host |
| --- |
| failed |
| success |
| `HOST-1` |
| `[1,1,1,1]` |
| `[null,null,null,null]` |
| `HOST-2` |
| `[2,2,2,2]` |
| `[20,20,20,20]` |
| `HOST-3` |
| `[null,null,null,null]` |
| `[30,30,30,30]` |

#### Time interval

The `timeseries` command automatically calculates an appropriate time interval derived from the query timeframe. The timeframe is divided into time slots of identical time intervals, and data is then rolled up into each of these time slots so that the number of points per time series is suitable for graphing. For instance, to graph a metric over a 1-day timeframe, it is more manageable to use 10-minute interval data (144 points) than 1-minute interval data (1,440 points).

You can influence the calculated time interval by specifying either a custom `interval` parameter or, via the `bins` parameter, the desired number of time slots.

#### Interval and bins parameters

The `interval` and `bins` parameters are exclusive. Both parameters are optional.

The actual time interval, whether specified via `bins` or `interval` parameter, is adjusted to meet the following conditions:

- It matches a well-known interval: 1, 2, 3, 5, 10, 15, or 30 minutes; 1, 2, 3, 4, 6, 8, 12, or 24 hours; or any multiple of 24 hours up to 30 days.

- The resulting number of time slots does not exceed the maximum number of elements per series (1,500).

To further ensure a consistent time series result, the time slots are aligned to the next midnight in the specified timezone. Because of this alignment, the returned timeframe will always be equal to or larger than the originally requested one—the start time may shift earlier and the end time later to accommodate complete time slots at both ends.

Assuming a query with specified timeframe `July 14 10:00 – July 16 10:00` and time interval of `5h`. `5h` isn't in the list of well-known intervals, so the command selects 6h instead. The anchor point from which the bin alignment is done is the next midnight in the user's timezone, i.e., `July 17, 00:00`. From the anchor point the nearest full interval offset later than the specified query end is selected as new query end: `July 16, 12:00`. Finally, the first full interval offset that falls before the original query start becomes the new query start: `July 14, 06:00`.

Data points are aggregated across time into time slots to deal with potentially large amounts of data. For instance, a day's data is combined into 10-minute time slots. This aggregation is called a `rollup` and happens in every `timeseries` query.

The aggregation function used to combine the data is dependent on the function used in the aggregation. For instance, assuming a metric with a `host` dimension, `timeseries min(dt.host.cpu.usage)` combines data into time slots using the `min` function for each time slot and each host, and then aggregates using the `min` function again across all hosts within each time slot, effectively performing a min of the min as expected.

##### Example

The `rollup` parameter can be used if it's necessary to specify a time aggregation function independently from the main aggregation, such as the average of the sums in the following example.

```
timeseries failed = avg(dt.requests.failed, rollup:sum)

```

The `rollup` parameter supports the following functions: `min`, `max`, `sum`, `avg`, and `total`.

Timeseries `shift` parameter allows to compare two different timeframes for a metric series.

The `shift` parameter shifts the timeframe specified in the query parameters and maps the resulting data points to timestamps from the original timeframe.

A positive argument shifts the timeframe into the future; a negative argument shifts the timeframe into the past.

For example, a timeframe from March 12, 2021 13:00 CET to 15:00 CET and a time shift of -1d (one day into the past) will result in
the data points being queried for the timeframe from March 11, 2021 13:00 CET to 15:00 CET. Timestamps in the response will be aligned to the original timeframe. For example, the data point with a timestamp of March 11, 2021 13:30 CET will be returned as March 12, 2021 13:30 CET.

##### Example

In this example, we compare two timeframes.

```
timeseries avail=avg(dt.host.disk.avail), by:{dt.entity.host}, from:-24h
| append [
      timeseries avail.7d=avg(dt.host.disk.avail), by:{dt.entity.host}, shift:-7d
    ]

```

## metrics

The `metrics` command retrieves metric series, which can be used for exploring metric keys, dimension keys, and values. You can't use it for charting or calculations, as neither timestamp nor timeseries values are returned. For such use cases, we recommend that you use the `timeseries` command instead.

The timeframe of `metrics` is limited to the last ten days. We recommend filtering the results, as there's a limit to the number of series that can be scanned.

#### Syntax

`metrics [, bucket: bucket, …] [, from] [, to] [, timeframe]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| bucket |  | `string` (bucket name or pattern) |  | A bucket (name or pattern) to retrieve data from. |  |  |
| from |  | `timestamp`, `duration`, `string` |  | The start of the timeframe (if no explicit timeframe is specified). A duration is interpreted as an offset from `now()`. |  |  |
| to |  | `timestamp`, `duration`, `string` |  | The end of the timeframe (if no explicit timeframe is specified). A duration is interpreted as an offset from `now()`. |  |  |
| timeframe |  | `timestamp`, `string` |  | The desired timeframe (if not specified, global timeframe is used). |  |  |

#### Limits

The `metrics` command is intended for exploratory queries and is subject to the following limits:

- time range — up to the last 10 days

- series count — limited to `100,000` metric series per query

Use the [timeseries](/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries) command to query actual time series data for further analysis.

#### Basic examples

##### Example 1: Query metric data

This example shows how to use the `metrics` command in its simplest form.

```
metrics

```

##### Example 2: Obtain metric keys

In this example, we obtain a list of metric keys that are sent by a specific host.

```
metrics
| filter dt.entity.host == "HOST-6DF6DE092963F2AB"
| dedup metric.key

```

You need the corresponding `storage:metrics:read` and `storage:buckets:read` permissions to read metrics data using the `timeseries` and `metrics` commands. For details, see [Permissions in Grail](/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table).

When using the `from`, `to`, or `timeframe` parameters to filter metric data, it's important to understand how the command determines which metric series to return. Metric queries use efficient storage groupings to decide which series are relevant to the requested time range. This means that the relevance of a series is determined at a coarse time window, not per individual data point. If a series has any data in a broader window that overlaps the requested timeframe, the series is considered relevant and may appear in the result even when its individual data points don't fall within the exact query time range.

Use the [timeseries](/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries) command to get data points strictly within the specified timeframe for more precise analysis.
