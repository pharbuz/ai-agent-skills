> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions)

# Aggregation functions

Aggregation functions compute results from a list of records.

You can use the aggregation functions listed on this page with the [summarize](/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize) command. See the description of the [timeseries](/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries) command and the [makeTimeseries](/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries) command for the aggregation functions available to use with those commands.

### Aggregation functions in/out table for homogeneous data types

The below table explains the results of combining homogeneous data types in the aggregation function, for example the `avg()` function for two numeric expressions.

In/out

**Numeric**

**Numeric**

**Numeric**

**Calculables**

**Calculables**

**Clear ordering**

**Clear ordering**

**Ambiguous ordering**

**Ambiguous ordering**

**Ambiguous ordering**

double

long

double & long

duration

timestamp

boolean

string

timeframe

record

array

**count()**

long

long

long

long

long

long

long

long

long

long (number of arrays)

**countif()**

long

long

long

long

long

long

long

long

long

long (number of arrays)

**sum()**

double

double

double

duration

`null`

`null`

`null`

`null`

`null`

`null`

**avg()**

double

double

double

duration

`null`

`null`

`null`

`null`

`null`

`null`

**correlation()**

double

double

double

`null`

`null`

`null`

`null`

`null`

`null`

`null`

**stddev**

double

double

double

`null`

`null`

`null`

`null`

`null`

`null`

`null`

**variance()**

double

double

double

`null`

`null`

`null`

`null`

`null`

`null`

`null`

**last()**

same as input

same as input

same as input

same as input

same as input

same as input

same as input

same as input

same as input

same as input

**first()**

same as input

same as input

same as input

same as input

same as input

same as input

same as input

same as input

same as input

same as input

General rules:

- If you mix two data types, the result is `null`, unless you mix data for which combinations are allowed, such as `long` and `double`.

- You will also get the `null` result for operations not covered by a given function, for example the `sum()` of two `boolean` expressions.

Function-specific rules:

- The [`sum function`](/platform/grail/dynatrace-query-language/functions/aggregation-functions#sum) allows numeric expressions and duration expressions. If you mix types, the result is `null`.

- The sum of two numeric expressions results in a `double` data type (for example, `double + double`, `double + long`, `long + long`).

- The sum of two duration expressions results in a `duration` data type.

- The sum of a numeric expression and a duration expression is `null`.

- The [`avg function`](/platform/grail/dynatrace-query-language/functions/aggregation-functions#avg) allows numeric expressions and duration expressions. If you mix types, the result is `null`.

- The average of two numeric expressions results in a `double` data type (for example, `double + double`, `double + long`, `long + long`).

- The average of two duration expressions results in a `duration` data type.

- The average of a numeric expression and a duration expression is `null`.

- The [`min`](/platform/grail/dynatrace-query-language/functions/aggregation-functions#min) and [`max`](/platform/grail/dynatrace-query-language/functions/aggregation-functions#max) functions allow numeric expressions, duration expressions, timestamp expressions, string expressions, and boolean expressions.

- The minimum/maximum of numerical expressions results in a double data type, apart from min/max of long expressions that results in a long data type.

- The minimum/maximum of any mixed types (other than double + long) is `null`.

- For strings, lexicographic ordering is used.

- For the boolean expressions, false < true.

- The [`takeFirst`](/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeFirst) and the [`takeLast`](/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeLast) functions allow expressions of all types.

- The first function selects the first non-null value (and the data type retrieved is the one of that value) within the existing order.

- The last function selects the last non-null value (and the data type retrieved is the one of that value) within the existing order.

## avg

Calculates the average value of a field for a list of records.

#### Syntax

`avg(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long, duration, iterative expression |  | The expression whose average is to be calculated. |  |  |

#### Returns

The data type of the returned value can be `double` or `duration`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize avg(a)

```

Query result:

| avg(a) |  | `4` |
| --- | --- | --- |

## collectArray

Collects the values of the provided field into an array. The original order of elements is not guaranteed.

#### Syntax

`collectArray(expression [, expand] [, maxLength])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | The expression whose values are to be collected into an array. |  |  |
| expand |  | boolean |  | The boolean expression that indicates whether the output should be a flat array. |  |  |
| maxLength |  | long |  | The maximum length of the resulting array. Must be between `1` and `131072`. The default value is `131072`. |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize collectArray(a),
            collectArray(a, maxLength: 3)

```

Query result:

| collectArray(a) |  | collectArray(a, maxLength:3) |  | `[2, 3, 7, 7, 1]` |  | `[2, 3, 7]` |
| --- | --- | --- | --- | --- | --- | --- |

##### Example 2

```
data record(a = 2),
     record(a = array(3, 7)),
     record(a = array(7)),
     record(a = array(array(1)))
| summarize collectArray(a, expand: false),
            collectArray(a, expand: true)

```

Query result:

| collectArray(a, expand:FALSE) |  | collectArray(a, expand:TRUE) |  | `[2, [3, 7], [7], [[1]]]` |  | `[2, 3, 7, 7, 1]` |
| --- | --- | --- | --- | --- | --- | --- |

## collectDistinct

Collects distinct values of the provided field into an array. The original order of elements is not guaranteed.

#### Syntax

`collectDistinct(expression [, expand] [, maxLength])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | The expression whose distinct values are to be collected. |  |  |
| expand |  | boolean |  | The boolean expression that indicates whether the output should be a flat array. |  |  |
| maxLength |  | long |  | The maximum length of the resulting array. Must be between `1` and `131072`. The default value is `131072`. |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize collectDistinct(a),
            collectDistinct(a, maxLength: 3)

```

Query result:

| collectDistinct(a) |  | collectDistinct(a, maxLength:3) |  | `[2, 3, 7, 1]` |  | `[2, 3, 7]` |
| --- | --- | --- | --- | --- | --- | --- |

##### Example 2

```
data record(a = 2),
     record(a = array(3, 7)),
     record(a = array(7)),
     record(a = array(array(1)))
| summarize collectDistinct(a, expand: false),
            collectDistinct(a, expand: true)

```

Query result:

| collectDistinct(a, expand:FALSE) |  | collectDistinct(a, expand:TRUE) |  | `[2, [3, 7], [7], [[1]]]` |  | `[2, 3, 7, 1]` |
| --- | --- | --- | --- | --- | --- | --- |

## correlation

Calculates the Pearson correlation of two numeric fields for a list of records. If one of the fields has a constant value, the covariance of both fields used for correlation is zero. In this case, the correlation coefficient causes a division by zero, yielding `null` for the correlation.

#### Syntax

`correlation(expression1, expression2)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression1 |  | double, long |  | The first numeric expression to be used in calculating the correlation. |  |  |
| expression2 |  | double, long |  | The second numeric expression to be used in calculating the correlation. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(a = 2, b = 14.55),
     record(a = 3, b = -6.13),
     record(a = 7, b = -77.2),
     record(a = 7, b = 99.99),
     record(a = 1, b = -6.13)
| summarize correlation(a, b)

```

Query result:

| correlation(a, b) |  | `0.0888` |
| --- | --- | --- |

## count

Counts the total number of records.

#### Syntax

`count()`

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize count()

```

Query result:

| count() |  | `5` |
| --- | --- | --- |

## countDistinct

This function is an alias for the `countDistinctApprox` function. For more information, see [`countDistinctApprox`.](/platform/grail/dynatrace-query-language/functions/aggregation-functions#countDistinctApprox)

## countDistinctApprox

Calculates the cardinality of unique values of a field for a list of records based on a stochastic estimation. The stochastic estimation relies on the UltraLogLog (ULL) algorithm, which is characterized by a guaranteed error rate as defined by the [ULL algorithm.](https://arxiv.org/abs/2308.16862) The UltraLogLog (ULL) sketch is a variant of HyperLogLog and is used for approximate distinct counts. Compared to the HyperLogLog sketch, the UltraLogLog sketch requires less space to achieve the same estimation error.

The precision parameter affects the relative standard error of the final estimation. The formula for getting the standard relative errors is `0.782/((2^precision)^(1/2))`. Note that, this is the standard error (expected or average error), this means that the estimation error can be greater than the calculated one.

#### Syntax

`countDistinctApprox(expression [, precision])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | any |  | The field or expression whose unique values are to be counted. |  |  |
| precision |  | long |  | Parameter that sets the precision level of the estimation. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize countDistinctApprox(a),
            countDistinctApprox(a, precision: 4)

```

Query result:

| countDistinctApprox(a) |  | countDistinctApprox(a, precision:4) |  | `4` |  | `3` |
| --- | --- | --- | --- | --- | --- | --- |

## countDistinctExact

Calculates the cardinality of unique values of a field for a list of records.

This function counts up to 1M distinct values and if exceeded the query will fail. The function issues a warning once it reaches 100k distinct values.

#### Syntax

`countDistinctExact(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | any |  | The expression whose distinct values are to be counted. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize countDistinctExact(a)

```

Query result:

| countDistinctExact(a) |  | `4` |
| --- | --- | --- |

## countIf

Counts the number of records that match the condition.

#### Syntax

`countIf(condition)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| condition |  | boolean |  | The expression that determines which records to count. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize countIf(a > 2)

```

Query result:

| countIf(a > 2) |  | `3` |
| --- | --- | --- |

## max

Calculates the maximum value of a field for a list of records.

#### Syntax

`max(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long, duration, timestamp, string, boolean, iterative expression |  | The expression whose maximum value is to be calculated. |  |  |

#### Returns

The data type of the returned value can be `double`, `long`, `timestamp`, `duration`, `string` or `boolean`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize max(a)

```

Query result:

| max(a) |  | `7` |
| --- | --- | --- |

## median

Calculates the median of an expression (short for `percentile(expression, 50)`). Quantile calculations use an exponential histogram representation suitable for large data sets with high dynamic ranges, producing small relative errors. Results might differ slightly from those obtained through less calculation-efficient methods.

#### Syntax

`median(expression [, weight])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long, duration, timestamp, boolean |  | The expression whose median value is to be calculated. |  |  |
| weight |  | double, long |  | The weight of the corresponding expression. The minimum value is: `0`. The default value is: `1`. |  |  |

#### Returns

The data type of the returned value can be `boolean`, `double`, `duration` or `timestamp`.

#### Examples

##### Example 1

```
fetch bizevents | filter event.category == "/broker-service/v1/trade/buy" | summarize median(amount)

```

## min

Calculates the minimum value of a field for a list of records.

#### Syntax

`min(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long, duration, string, timestamp, boolean, iterative expression |  | The expression whose minimum value is to be calculated. |  |  |

#### Returns

The data type of the returned value can be `double`, `long`, `timestamp`, `duration`, `string` or `boolean`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize min(a)

```

Query result:

| min(a) |  | `1` |
| --- | --- | --- |

## percentile

Calculates a given percentile of an expression. Quantile calculations use an exponential histogram representation suitable for large data sets with high dynamic ranges, producing small relative errors. Results might differ slightly from those obtained through less calculation-efficient methods.

#### Syntax

`percentile(expression, percentile [, weight])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long, duration, timestamp, boolean |  | The expression from which to compute a percentile. |  |  |
| percentile |  | double, long |  | The percentile to compute (between 0 and 100). |  |  |
| weight |  | double, long |  | The weight of the corresponding expression. The minimum value is: `0`. The default value is: `1`. |  |  |

#### Returns

The data type of the returned value can be `double`, `boolean`, `duration` or `timestamp`.

#### Examples

##### Example 1

```
fetch bizevents | filter event.category == "/broker-service/v1/trade/buy" | summarize percentile(amount, 90)

```

## percentiles

Calculates the given percentiles of an expression. The function is similar to the `percentile` function, but returns an array of values instead of a single one.

#### Syntax

`percentiles(expression, percentile, … [, weight])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long, duration, timestamp, boolean |  | The expression from which to compute a percentile. |  |  |
| percentile |  | double, long |  | The percentile to compute (between `0` and `100`). |  |  |
| weight |  | double, long |  | The weight of the corresponding expression. The minimum value is: `0`. The default value is: `1`. |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
fetch bizevents | filter event.category == "/broker-service/v1/trade/buy" | summarize percentiles(amount, 90, 95, 99)

```

## percentileFromSamples

Calculates a given percentile of an array expression.

#### Syntax

`percentileFromSamples(expression, percentile [, originalCount])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | array |  | The expression to which the aggregation function should be applied. |  |  |
| percentile |  | double, long |  | The percentile to compute, between `0` and `100`. |  |  |
| originalCount |  | double, long |  | The original element count of the given array expression. The minimum value is: `0`. |  |  |

#### Returns

The data type of the returned value is `boolean`, `double`, `timestamp`, or `duration`.

#### Examples

##### Example 1

```
fetch spans
| filter isNotNull(aggregation.duration_samples) and isNotNull(aggregation.count)
| summarize p95 = percentileFromSamples(aggregation.duration_samples, 95, originalCount: aggregation.count)

```

## percentRank

Calculates the percentile rank for a given value. This aggregation is the inverse of the percentile aggregation, it returns the fraction of values that are below the provided parameter. The calculated value is a number between `0.0` and `1.0`.

#### Syntax

`percentRank(expression, value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long, duration |  | The expression for which to compute a percentile rank. |  |  |
| value |  | double, long, duration |  | The value for which to retrieve the percentile. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
fetch bizevents | filter event.category == "/broker-service/v1/trade/buy" | summarize percentRank(amount, 5000)

```

## stddev

Calculates the standard deviation of a field for a list of records.

#### Syntax

`stddev(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The expression whose standard deviation is to be calculated. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize stddev(a)

```

Query result:

| stddev(a) |  | `2.5298` |
| --- | --- | --- |

## sum

Calculates the sum of a field for a list of records.

#### Syntax

`sum(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, duration, long |  | The expression that specifies which values are to be added together. |  |  |

#### Returns

The data type of the returned value can be `double` or `duration`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize sum(a)

```

Query result:

| sum(a) |  | `20` |
| --- | --- | --- |

## takeAny

Returns any non-null value of a field for a list of records.

#### Syntax

`takeAny(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | any |  | The expression from which to retrieve any non-null value. |  |  |

#### Returns

The data type of the returned value can be `array`, `binary`, `boolean`, `double`, `duration`, `ip`, `long`, `record`, `string`, `timeframe`, `timestamp` or `uid`.

#### Examples

##### Example 1

```
data record(a = null),
     record(a = 3),
     record(a = 7),
     record(a = 5),
     record(a = null)
| summarize takeAny(a)

```

Query result:

| takeAny(a) |  | `3` |
| --- | --- | --- |

## takeFirst

Returns the first value of a field for a list of records.

The order of records may differ each time a query is executed. Since the [summarize](/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize) command doesn't sort the records, we recommend using the [sort](/platform/grail/dynatrace-query-language/commands/ordering-commands#sort) command before using `summarize takeFirst(expression)` to ensure consistent results.

#### Syntax

`takeFirst(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | any |  | The expression from which the first value is retrieved. |  |  |

#### Returns

The data type of the returned value can be `array`, `binary`, `boolean`, `double`, `duration`, `ip`, `long`, `record`, `string`, `timeframe`, `timestamp` or `uid`.

#### Examples

##### Example 1

```
data record(a = null),
     record(a = 3),
     record(a = 7),
     record(a = 5),
     record(a = null)
| summarize takeFirst(a)

```

Query result:

| takeFirst(a) |  | `3` |
| --- | --- | --- |

## takeLast

Returns the last value of a field for a list of records.

The order of records may differ each time a query is executed. Since the [summarize](/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize) command doesn't sort the records, we recommend using the [sort](/platform/grail/dynatrace-query-language/commands/ordering-commands#sort) command before using `summarize takeLast(expression)` to ensure consistent results.

#### Syntax

`takeLast(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | any |  | The expression from which the last value is retrieved. |  |  |

#### Returns

The data type of the returned value can be `array`, `binary`, `boolean`, `double`, `duration`, `ip`, `long`, `record`, `string`, `timeframe`, `timestamp` or `uid`.

#### Examples

##### Example 1

```
data record(a = null),
     record(a = 3),
     record(a = 7),
     record(a = 5),
     record(a = null)
| summarize takeLast(a)

```

Query result:

| takeLast(a) |  | `5` |
| --- | --- | --- |

## takeMax

Retrieves the maximum from a list of records. Renders results for lists with both homogenous and non-homogenous data.

#### Syntax

`takeMax(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | any |  | The expression from which the maximum value is to be extracted. |  |  |

#### Returns

The data type of the returned value can be `array`, `binary`, `boolean`, `double`, `duration`, `ip`, `long`, `record`, `string`, `timeframe`, `timestamp` or `uid`.

#### Examples

##### Example 1

```
data record(a = 2, b = 2),
     record(a = 3, b = array(1, 2, 3)),
     record(a = 7, b = ("2019-08-01T09:30:00.000-0400")),
     record(a = 7, b = "DQL is awesome!"),
     record(a = 1, b = 5m)
| summarize takeMax(a),
            max(a),
            takeMax(b),
            max(b)

```

Query result:

| takeMax(a) |  | max(a) |  | takeMax(b) |  | max(b) |  | `7` |  | `7` |  | `[1, 2, 3]` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## takeMin

Returns the minimum value of a field for a list of records.

#### Syntax

`takeMin(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | any |  | The expression from which the minimum value is to be extracted. |  |  |

#### Returns

The data type of the returned value can be `array`, `binary`, `boolean`, `double`, `duration`, `ip`, `long`, `record`, `string`, `timeframe`, `timestamp` or `uid`.

#### Examples

##### Example 1

```
data record(a = 2, b = 2),
     record(a = 3, b = array(1, 2, 3)),
     record(a = 7, b = ("2019-08-01T09:30:00.000-0400")),
     record(a = 7, b = "DQL is awesome!"),
     record(a = 1, b = 5m)
| summarize takeMin(a),
            min(a),
            takeMin(b),
            min(b)

```

Query result:

| takeMin(a) |  | min(a) |  | takeMin(b) |  | min(b) |  | `1` |  | `1` |  | `2` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## variance

Calculates the variance of a field for a list of records.

#### Syntax

`variance(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The expression from which to compute variance. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| summarize variance(a)

```

Query result:

| variance(a) |  | `6.4` |
| --- | --- | --- |
