> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands)

# DQL aggregation commands

## fieldsSummary

The `fieldsSummary` command calculates the cardinality of field values that the specified fields have.

#### Syntax

`fieldsSummary field, … [, topValues] [, extrapolateSamples]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | field |  | field identifier |  | A field identifier. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| topValues |  | positive long |  | The number of top N values to be returned. The default value is `20`. |  |  |  |  |  |  |  |  |  |  |
| extrapolateSamples |  | boolean |  | Flag indicating if the cardinality shall be multiplied with a possible sampling rate. |  |  |  |  |  |  |  |  |  |  |

#### Basic example

##### Example: Simple fields summary

The following example shows the cardinality of values for the field `host`.

```
data record(host = "host-a"),
     record(host = "host-a"),
     record(host = "host-b")
| fieldsSummary host

```

Query result:

| field |
| --- |
| rawCount |
| count |
| values |
| `host` |
| `3` |
| `3` |
| [**value:** `host-a` **count:** `2`, **value:** `host-b` **count:** `1`] |

#### Practical example

##### Example: Log count by host

In this example, the query fetches logs with a sampling ratio of 10,000 and calculates the cardinality of values for the `dt.entity.host` field, providing the 10 top values encountered when extrapolating the value count by the sampling ratio.

```
fetch logs, samplingRatio: 10000
| fieldsSummary dt.entity.host, topValues: 10, extrapolateSamples: true

```

## makeTimeseries

Creates timeseries from the data in the stream. The `makeTimeseries` command provides a convenient way to chart raw non-metric data (such as events or logs) over time.

#### Syntax

`makeTimeseries [by: { [expression, …] }] [, interval] [, bins] [, from] [, to] [, timeframe] [, time ,] [, spread ,] [, nonempty ,] [, scalar:] aggregation, …`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | aggregation |  | aggregation function |  | The aggregation function that should be used to create the series.  Input values in the aggregation function need to be numeric. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| time |  | expression |  | The expression that provides the timestamp for a record, which will be assigned to a series bucket. If the current data does not contain a field `timestamp` the parameter needs to be specified, referencing the time field. The default value is `timestamp`. If the `timestamp` field doesn't exist, the second default value is `start_time`. |  |  |  |  |  |  |  |  |  |  |
| from |  | timestamp, duration |  | The start timestamp of the series. The actual series timeframe will be adjusted by the series alignment. |  |  |  |  |  |  |  |  |  |  |
| to |  | timestamp, duration |  | The end timestamp of the series. The actual series timeframe will be adjusted by the series alignment. |  |  |  |  |  |  |  |  |  |  |
| timeframe |  | timeframe |  | The timeframe of the series.  The actual series timeframe will be adjusted by the series alignment. The default value is query timeframe. |  |  |  |  |  |  |  |  |  |  |
| bins |  | positive integer |  | The number of buckets that should be created for the series.  Must not be specified if interval is specified. The default value is `120`. |  |  |  |  |  |  |  |  |  |  |
| interval |  | positive duration |  | The length of a bucket in the series. Must not be specified if bins is specified. Automatically calculated based on the number of bins. |  |  |  |  |  |  |  |  |  |  |
| by |  | list of expressions |  | The expressions the series should be split by. |  |  |  |  |  |  |  |  |  |  |
| spread |  | timeframe |  | A timeframe expression that provides the timeframe for the bucket calculation of the values in the series. `Spread` can only be used instead of `time` and you can only use it with the `count` or `countIf` functions. |  |  |  |  |  |  |  |  |  |  |
| nonempty |  | boolean |  | Produces empty series when there is no data. |  |  |  |  |  |  |  |  |  |  |
| scalar |  | boolean |  | Flag to indicate that a single scalar value spanning the whole timeframe shall be calculated. Can be used on any aggregation function except `start` and `end`. |  |  |  |  |  |  |  |  |  |  |

#### Basic example

##### Example: Count records

The following example counts the number of records per time interval.

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400")),
     record(timestamp = toTimestamp("2019-08-01T09:31:00.000-0400")),
     record(timestamp = toTimestamp("2019-08-01T09:31:30.000-0400")),
     record(timestamp = toTimestamp("2019-08-01T09:32:00.000-0400"))
| makeTimeseries count(),
    from: toTimestamp("2019-08-01T09:30:00.000-0400"),
    to: toTimestamp("2019-08-01T09:33:00.000-0400")

```

Query result:

| timeframe |
| --- |
| interval |
| count() |
| **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T13:33:00.000Z` |
| `1 min` |
| `[1, 2, 1]` |

#### Practical examples

##### Example 1: Error logs for host

This example shows error logs for a host over time.

```
fetch logs
| filter dt.entity.host == "HOST-15FE58391F97B7AA" and loglevel == "ERROR"
| makeTimeseries count()

```

##### Example 2: Buy activity for account

The following example shows the buy activity for a specific account for the last 24 hours.
The `interval` parameter sets the time interval to 30 minutes, resulting in 48 bins in the query outcome.
A bin with no buy activity has the value `0` because the `default` parameter is `0`. Not setting this parameter results in `NULL` values for the bins.

```
fetch bizevents, from: now() - 24h
| filter accountId == 7
| filter in(event.category, array("/broker-service/v1/trade/long/buy", "/v1/trade/buy"))
| makeTimeseries count(default: 0), interval: 30m

```

##### Example 3: Transaction statistics

The following advanced example takes sell transactions of the last seven days recorded as business events and charts the total number of transactions and high-volume transactions based on the conditional `countIf()` function and the maximum price by `accountId`. The `interval` parameter defines a fixed chart resolution of 1 day.

```
fetch bizevents, from: now() - 7d
| filter in(event.type, array("com.easytrade.long-sell", "com.easytrade.quick-sell"))
| makeTimeseries {
      count(),
      high_volume = countIf(amount >= 100 and amount <= 10000),
      max(price)
    },
    by: { accountId },
    interval: 1d

```

##### Example 4: Chart response time percentiles for a specific endpoint

The `timestamp` field doesn't exist on spans, so the `makeTimeseries` command uses the `start_time` field for calculating the timeseries instead.

```
fetch spans
| filter request.is_root_span == true
| filter endpoint.name == "GET /api/cart"
| makeTimeseries {
    avg = avg(duration),
    p50 = median(duration),
    p90 = percentile(duration, 90)
  }

```

##### Example 5: Distinct hosts sorted by k8s cluster name

```
fetch logs
| makeTimeseries countDistinct(dt.entity.host, scalar: true),
by:{k8s.cluster.name}

```

#### Bins parameter

The `interval` and `bins` parameters are exclusive. Both parameters are optional.

The actual time interval, whether specified via `bins` or `interval` parameter, is adjusted to meet the following conditions:

- It matches a well-known interval: 1, 2, 3, 5, 10, 15, or 30 minutes; 1, 2, 3, 4, 6, 8, 12, or 24 hours; or any multiple of 24 hours up to 30 days.

- The resulting number of time slots does not exceed the maximum number of elements per series (1,500).

To further ensure a consistent time series result, the time slots are aligned to the next midnight in the specified timezone. Because of this alignment, the returned timeframe will always be equal to or larger than the originally requested one—the start time may shift earlier and the end time later to accommodate complete time slots at both ends.

Assuming a query with specified timeframe `July 14 10:00 – July 16 10:00` and time interval of `5h`. `5h` isn't in the list of well-known intervals, so the command selects 6h instead. The anchor point from which the bin alignment is done is the next midnight in the user's timezone, i.e., `July 17, 00:00`. From the anchor point the nearest full interval offset later than the specified query end is selected as new query end: `July 16, 12:00`. Finally, the first full interval offset that falls before the original query start becomes the new query start: `July 14, 06:00`.

#### Default value for empty time slots

The `makeTimeseries` command produces homogenous time series of aggregated data: all series have identical start and end timestamps, time interval and number of elements. If data is missing for a particular time slot, it is filled with `null`. Specifying a `default` parameter fills empty time slots with the `default` parameter value instead of `null`.

There might be no record processed by the `makeTimeseries` command. For example, when no relevant data is available for the timeframe. The `makeTimeseries` command returns an empty result in this case. If the expected result is a chart with 0 values, using `nonempty: true` in combination with `default: 0` produces the desired result.

##### Example 1

```
fetch logs
| filter status >= 500
| makeTimeseries count = count(default: 0), interval: 30m

```

Query result:

timeframe

interval

count

No records

No records

No records

##### Example 2

```
fetch logs
| filter status >= 500
| makeTimeseries count = count(default: 0), interval: 30m, nonempty: true

```

Query result:

| **start**: `2019-08-01T13:00:00.000Z`**end**: `2019-08-01T15:30:00.000Z` |  | `30 min` |  | `[0, 0, 0, 0, 0]` |
| --- | --- | --- | --- | --- |

#### Aggregation functions

Different aggregation functions are available to use with the `makeTimeseries` command. These functions are:

- `sum`

- `avg`

- `min`

- `max`

- `median`

- `percentile`

- `percentileFromSamples`

- `percentRank`

- `count`

- `countIf`

- `countDistinctExact`

- `countDistinctApprox`

It is also possible to use `start` and `end` with `makeTimeseries`. However, they need to be used together with another aggregation function.

##### Syntax

These functions have the following syntax:

- `sum(expression [, default] [, rate])`

- `avg(expression [, default] [, rate])`

- `min(expression [, default] [, rate])`

- `max(expression [, default] [, rate])`

- `median(expression [, weight] [, default] [, rate])`

- `percentile(expression, percentile [, weight] [, default] [, rate])`

- `percentileFromSamples(expression, percentile [, originalCount] [, default] [, rate])`

- `percentRank(expression, value [, default] [, rate])`

- `count([default] [, rate])`

- `countIf(expression [, default] [, rate])`

- `countDistinctExact(expression [, default] [, rate])`

- `countDistinctApprox(expression [, precision] [, default] [, rate])`

- `start()`

- `end()`

##### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | expression |  | The expression the series should be created for. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| default |  | number |  | The default value that should be used to fill gaps/empty bins. The default value is null. |  |  |  |  |  |  |  |  |  |  |
| rate |  | duration |  | The duration that shall be used to adjust the bin values using the following formula: (binValue / interval) * rate. |  |  |  |  |  |  |  |  |  |  |
| percentile |  | double, long |  | The nth-percentile, such that approximately n percent of observed measurements fall below this value. Must be between `0` and `100`. |  |  |  |  |  |  |  |  |  |  |
| precision |  | long |  | Parameter that sets the precision level of the estimation. Must be between `3` and `16`. The default value is `14`. |  |  |  |  |  |  |  |  |  |  |
| weight |  | double, long |  | The weight of the corresponding expression. The minimum value is: `0`.The default value is: `1`. |  |  |  |  |  |  |  |  |  |  |
| originalCount |  | double, long |  | The original element count of the given array expression. The minimum value is: `0`. |  |  |  |  |  |  |  |  |  |  |
| value |  | double, long |  | The value for which to retrieve the percentile. |  |  |  |  |  |  |  |  |  |  |

## summarize

Groups together records that have the same values for a given field and aggregates them.

#### Syntax

`summarize [field =] aggregation, ... [, by: {[field =] expression, ...}]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array, boolean, counter, double, duration, ip, long, record, string, timeframe, timestamp |  | An expression to group by. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aggregation |  | array, boolean, counter, double, duration, ip, long, record, string, timeframe, timestamp |  | An aggregation function |  |  |  |  |  |  |  |  |  |  |

#### Aggregation functions

You can use different aggregation functions with the `summarize` command. See all available [aggregation](/platform/grail/dynatrace-query-language/functions/aggregation-functions) functions.

#### Basic examples

##### Example 1: Sum field

The below example uses the `summarize` command and the `sum` aggregation function to sum the field `value`.

```
data record(value = 2),
     record(value = 3),
     record(value = 7),
     record(value = 7),
     record(value = 1)
| summarize sum(value)

```

Query result:

| sum(value) |
| --- |
| `20` |

##### Example 2: Summarize by category

The following example calculates the sum of the field `value` and splits the result by the field `cat`. Furthermore, the resulting aggregation field gets the alias name `sum` and the grouping field the alias `category`.

```
data record(value = 2, cat = "a"),
     record(value = 3, cat = "b"),
     record(value = 7, cat = "a"),
     record(value = 7, cat = "b"),
     record(value = 1, cat = "b")
| summarize sum = sum(value),
    by: { category = cat }

```

Query result:

| category |
| --- |
| sum |
| `a` |
| `9` |
| `b` |
| `11` |

##### Example 3: Empty aggregation result

If the `summarize` command has no input records and you don't use the `by` clause, the `summarize` command will still return a single record a as result.

```
data record(value = 2),
     record(value = 3),
     record(value = 7),
     record(value = 7),
     record(value = 1)
| filter value > 7
| summarize count(), sum(value), collectArray(value), takeAny(value)

```

Query result:

| count() |
| --- |
| sum(value) |
| collectArray(value) |
| takeAny(value) |
| `0` |
| *null* |
| *null* |
| *null* |

##### Example 4: Group by field doesn't exist for every record

If the grouped field does not exist for every record, the summarize command adds a `null` group to the result.

```
data record(value = 2),
     record(value = 3, category = "b"),
     record(value = 7, category = "a"),
     record(value = 7, category = "b"),
     record(value = 1)
| summarize sum(value),
    by: { category }

```

Query result:

| category |
| --- |
| sum(value) |
| `a` |
| `7` |
| `b` |
| `10` |
| *null* |
| `3` |

##### Example 5: Using summarize instead of join

You can use the `summarize` command instead of the `join` command when joining on the same table.
As input for the `summarize` command, there are two types of records.
In this example, there are records with fields `key` and `value` and records with fields `key` and `amount`. The `key` field is set as the `by` parameter.
The other fields are added to the aggregation list.
If a record type has duplicate key values, use the aggregation function `collectArray` for its fields.
Otherwise, use the `takeAny` aggregation function for its record type fields. As the last step, you need to expand the fields that use the `collectArray` function.
Use the `summarize` command instead of the `join` to avoid fetching the same table twice.

```
data record(key = "a", value = 1),
     record(key = "b", value = 2),
     record(key = "c", value = 4),
     record(key = "b", amount = 10),
     record(key = "c", amount = 20),
     record(key = "c", amount = 40),
     record(key = "d", amount = 50)
| summarize {
      value = takeAny(value),
      amount = arrayRemoveNulls(collectArray(amount))
    },
    by: { key }
| expand amount

```

Query result:

| key |
| --- |
| value |
| amount |
| `b` |
| `2` |
| `10` |
| `c` |
| `4` |
| `20` |
| `c` |
| `4` |
| `40` |
| `d` |
| *null* |
| `50` |

##### Example 6: Element-wise aggregation

The following example uses 'summarize' with an iterative expression in the 'sum' aggregation function to calculate the element-wise sum of arrays in the input records.

```
data record(a = array(2, 2)),
     record(a = array(7, 1))
| summarize sum(a[])

```

Query result:

| sum(a[]) |
| --- |
| `[9, 3]` |

#### Practical example

##### Example: Count selected log levels

The following example counts selected log levels and groups them by `dt.entity.host` and `dy.entity.process_group`.

```
fetch logs
| summarize {
      errors = countIf(loglevel == "ERROR"),
      warnings = countIf(loglevel == "WARN"),
      severe = countIf(loglevel == "DEBUG")
    },
    by: {
      dt.entity.host,
      dt.entity.process_group
    }

```
