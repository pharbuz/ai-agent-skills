> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/array-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/array-functions)

# Array functions

Functions related to a collection of items of the same data type stored at adjacent memory locations.

## array

Creates an `array` from the list of given parameters.

#### Syntax

`array(expression, …)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | An element inside the array. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record()
| fieldsAdd array(2, 3, 7, 7, 1)

```

Query result:

| array(2, 3, 7, 7, 1) |
| --- |
| `[2, 3, 7, 7, 1]` |

## arrayAvg

Returns the average of an array. Values that are not numeric are ignored. Returns 0 if there is no matching element.

#### Syntax

`arrayAvg(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayAvg(a)

```

Query result:

| a |
| --- |
| arrayAvg(a) |
| `[2, 3, 7, 7, 1]` |
| `4` |

## arrayConcat

Concatenates multiple arrays into a single array. This function skips all null values and non-array input parameter values. If no array parameter input is available, it returns null.

#### Syntax

`arrayConcat(array, …)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array expression |  | Array expression that should be combined with others. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1), b = array("hello", "world"), c = array(null, 13))
| fieldsAdd arrayConcat(a, b, c)

```

Query result:

| a |
| --- |
| b |
| c |
| arrayConcat(a, b, c) |
| `[2, 3, 7, 7, 1]` |
| `[hello, world]` |
| `[NULL, 13]` |
| `[2, 3, 7, 7, 1, hello, world, NULL, 13]` |

## arrayCumulativeSum

Returns the cumulative sum, also known as the running total, of the elements of the input array.

#### Syntax

`arrayCumulativeSum(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| array |  | array |  | The input array. |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = array(2, null, 7, null, 1)),
     record(a = array(2, "3", 7, 7, 1))
| fieldsAdd arrayCumulativeSum(a)

```

Query result:

| a |  | arrayCumulativeSum(a) |  | `2, 3, 7, 7, 1` |  | `[2, 5, 12, 19, 20]` |  | `2, null, 7, null, 1` |  | `[2, 2, 9, 9, 10]` |  | `2, 3, 7, 7, 1` |  | ***null*** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## arrayDelta

Returns an array where each element is the difference from the previous non-null element, when positive, otherwise it returns 0. Null elements are skipped. The first element of the returned array is null.

#### Syntax

`arrayDelta(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayDelta(a)

```

Query result:

| a |
| --- |
| arrayDelta(a) |
| `[2, 3, 7, 7, 1]` |
| `[NULL, 1, 4, 0, 0]` |

## arrayDiff

Calculates the element-wise difference between consecutive elements in an array. For each element at index `i > 0`, the result is: `result[i] = array[i] - array[i - 1]`. The first element of the returned array is `null`. The function supports array elements of numeric type (`long`, `double`), `timestamp` or `duration`.

Unlike `arrayDelta`, `arrayDiff` uses the immediate previous element rather than the previous non-null element and preserves negative differences.

#### Syntax

`arrayDiff(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |  | The array expression to get the element-wise difference from. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = array(5, null, 2, 4, -1)),
     record(a = array(now(), now()+1h, now())),
     record(a = array(2, 3, 1h, now(), 1h, 2h))
| fieldsAdd arrayDiff(a)

```

Query result:

| a |
| --- |
| arrayDiff(a) |
| `[2, 3, 7, 7, 1]` |
| `[null, 1, 4, 0, -6]` |
| `[5, null, 2, 4, -1]` |
| `[null, null, null, 2, -5]` |
| `[now(), now()+1h, now(),]` |
| `[null, 1h, -1h]` |
| `[2, 3, 1h, now(), 1h, 2h]` |
| `[null, 1, null, now()-1h, null, 1h]` |

## arrayDistinct

Returns the array without duplicates. It sorts numbers in ascending order and strings in lexicographic order.

#### Syntax

`arrayDistinct(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayDistinct(a)

```

Query result:

| a |
| --- |
| arrayDistinct(a) |
| `[2, 3, 7, 7, 1]` |
| `[1, 2, 3, 7]` |

## arrayElement

Extracts a single element with the given index from an array. The index can be defined as any dynamic expression of data type `long`. When the index is a literal, you can alternatively use the bracket notation: `array[...]`.

#### Syntax

`arrayElement(expression, index)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array |  | The array from which to extract an element. |  |  |  | index |  | long |  | The index of the element to extract. Negative numbers are counted from the end. Use `-1` for the last element of the array. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value matches the data type of the element at the specified index.

#### Examples

##### Example 1

```
data record(a = array(0, 1, 2, 3, 4, 5, 6), i = 2),
     record(a = array("foo", "bar"), i = -1)
| fieldsAdd a[2],
            arrayElement(a, 2),
            arrayElement(a, i),
            arrayElement(a, (arraySize(a)-1) / 2)

```

Query result:

| a |
| --- |
| i |
| a[2] |
| arrayElement(a, 2) |
| arrayElement(a, i) |
| arrayElement(a, (arraySize(a)-1) / 2) |
| `[0, 1, 2, 3, 4, 5, 6]` |
| `2` |
| `2` |
| `2` |
| `2` |
| `3` |
| `["foo", "bar"]` |
| `-1` |
| `null` |
| `null` |
| `"bar"` |
| `"foo"` |

## arrayFirst

Returns the first non-null element of an array.

#### Syntax

`arrayFirst(arrayName)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value matches the data type of the first element of the input array.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayFirst(a)

```

Query result:

| a |
| --- |
| arrayFirst(a) |
| `[2, 3, 7, 7, 1]` |
| `2` |

## arrayFlatten

Returns a flattened array.

#### Syntax

`arrayFlatten(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |  | The array that should be flattened. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = array(array(2, 3), array(7, 7, 1))),
     record(a = array(array(2, 3, null), array(record(a = 7), "7", 1)))
| fieldsAdd arrayFlatten(a)

```

Query result:

| a |  | arrayFlatten(a) |  | `[2, 3, 7, 7, 1]` |  | `[2, 3, 7, 7, 1]` |  | `[[2, 3], [7, 7, 1]]` |  | `[2, 3, 7, 7, 1]` |  | [[`2`, `3`, `NULL`], [**a:**`7`, `7`, `1`]] |  | [`2`, `3`, `NULL`, **a:** `7`, `7`, `1`] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## arrayIndexOf

Returns the position of the first member in the array, which is equal to the given value.

#### Syntax

`arrayIndexOf(array, value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |  | The array expression in which the value is searched for. |  |  |  | value |  | expression |  | The primitive value to search for in the expression. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayIndexOf(a, 2), arrayIndexOf(a, 7), arrayIndexOf(a, 11)

```

Query result:

| a |
| --- |
| arrayIndexOf(a, 2) |
| arrayIndexOf(a, 7) |
| arrayIndexOf(a, 11) |
| `[2, 3, 7, 7, 1]` |
| `0` |
| `2` |
| `-1` |

## arrayLast

Returns the last non-null element of an array.

#### Syntax

`arrayLast(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value matches the data type of the last element of the input array.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayLast(a)

```

Query result:

| a |
| --- |
| arrayLast(a) |
| `[2, 3, 7, 7, 1]` |
| `1` |

## arrayLastIndexOf

Returns position of the last member in the array, which is equal to the given value.

#### Syntax

`arrayLastIndexOf(array, value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |  | The array expression in which the value is searched for. |  |  |  | value |  | expression |  | The primitive value to search for in the expression. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayLastIndexOf(a, 2), arrayLastIndexOf(a, 7), arrayLastIndexOf(a, 11)

```

Query result:

| a |
| --- |
| arrayLastIndexOf(a, 2) |
| arrayLastIndexOf(a, 7) |
| arrayLastIndexOf(a, 11) |
| `[2, 3, 7, 7, 1]` |
| `0` |
| `3` |
| `-1` |

## arrayMax

Returns the maximum element of an array. Strings are compared in lexicographic order.

#### Syntax

`arrayMax(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value matches the data type of the last element of the input array.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayMax(a)

```

Query result:

| a |
| --- |
| arrayMax(a) |
| `[2, 3, 7, 7, 1]` |
| `7` |

## arrayMedian

Returns the median of the members of an array. Returns `null` for arrays with mixed data type. Quantile calculations use an exponential histogram representation suitable for large data sets with high dynamic ranges, producing small relative errors. Results might differ slightly from those obtained through less calculation-efficient methods.

#### Syntax

`arrayMedian(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array |  | The array from which to compute the median. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value can be `boolean`, `double`, `duration`, or `timestamp`.

#### Examples

##### Example 1

```
fetch bizevents | filter matchesValue(event.category, {"/v1/trade/buy", "/v1/trade/sell"}) | summarize amounts = collectArray(amount), by: event.category | fieldsAdd arrayMedian(amounts)

```

## arrayMin

Returns the minimum element of an array. Strings are compared in lexicographic order.

#### Syntax

`arrayMin(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value matches the data type of the minimum (smallest) element of the input array.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayMin(a)

```

Query result:

| a |
| --- |
| arrayMin(a) |
| `[2, 3, 7, 7, 1]` |
| `1` |

## arrayMovingAvg

Replaces each element of the input array with the average of current and previous elements within the window.

#### Syntax

`arrayMovingAvg(array, window)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | window |  | double, long |  | The maximum number of elements to look back at. Maximum 60. |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = array(2, null, 7, null, 1)),
     record(a = array(2, "3", 7, 7, 1))
| fieldsAdd arrayMovingAvg(a, 2), arrayMovingAvg(a, 6)

```

Query result:

| a |
| --- |
| arrayMovingAvg(a, 2) |
| arrayMovingAvg(a, 6) |
| `[2, 3, 7, 7, 1]` |
| `[2, 2.5, 5, 7, 4]` |
| `[2, 2.5, 4, 4.75, 4]` |
| `[2, NULL, 7, NULL, 1]` |
| `[2, 2, 7, 7, 1]` |
| `[2, 2, 4.5, 4.5, 3.3333333333333335]` |
| `[2, 3, 7, 7, 1]` |
| *null* |
| *null* |

## arrayMovingMax

Replaces each element of the input array with the maximum of current and previous elements within the window.

#### Syntax

`arrayMovingMax(array, window)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | window |  | double, long |  | The maximum number of elements to look back at. Maximum 60. |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = array(2, null, 7, null, 1)),
     record(a = array(2, "3", 7, 7, 1))
| fieldsAdd arrayMovingMax(a, 2), arrayMovingMax(a, 6)

```

Query result:

| a |
| --- |
| arrayMovingMax(a, 2) |
| arrayMovingMax(a, 6) |
| `[2, 3, 7, 7, 1]` |
| `[2, 3, 7, 7, 7]` |
| `[2, 3, 7, 7, 7]` |
| `[2, NULL, 7, NULL, 1]` |
| `[2, 2, 7, 7, 1]` |
| `[2, 2, 7, 7, 7]` |
| `[2, 3, 7, 7, 1]` |
| *null* |
| *null* |

## arrayMovingMin

Replaces each element of the input array with the minimum of current and previous elements within the window.

#### Syntax

`arrayMovingMin(array, windowSize)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | window |  | double, long |  | The maximum number of elements to look back at. Maximum 60. |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = array(2, null, 7, null, 1)),
     record(a = array(2, "3", 7, 7, 1))
| fieldsAdd arrayMovingMin(a, 2), arrayMovingMin(a, 6)

```

Query result:

| a |
| --- |
| arrayMovingMin(a, 2) |
| arrayMovingMin(a, 6) |
| `[2, 3, 7, 7, 1]` |
| `[2, 2, 3, 7, 1]` |
| `[2, 2, 2, 2, 1]` |
| `[2, NULL, 7, NULL, 1]` |
| `[2, 2, 7, 7, 1]` |
| `[2, 2, 2, 2, 1]` |
| `[2, 3, 7, 7, 1]` |
| *null* |
| *null* |

## arrayMovingSum

Replaces each element of the input array with the sum of current and previous elements within the window.

#### Syntax

`arrayMovingSum(array, windowSize)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | window |  | double, long |  | The maximum number of elements to look back at. Maximum 60. |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = array(2, null, 7, null, 1)),
     record(a = array(2, "3", 7, 7, 1))
| fieldsAdd arrayMovingSum(a, 2), arrayMovingSum(a, 6)

```

Query result:

| a |
| --- |
| arrayMovingSum(a, 2) |
| arrayMovingSum(a, 6) |
| `[2, 3, 7, 7, 1]` |
| `[2, 5, 10, 14, 8]` |
| `[2, 5, 12, 19, 20]` |
| `[2, NULL, 7, NULL, 1]` |
| `[2, 2, 7, 7, 1]` |
| `[2, 2, 9, 9, 10]` |
| `[2, 3, 7, 7, 1]` |
| *null* |
| *null* |

## arrayPercentile

Calculates a given percentile of an array. Quantile calculations use an exponential histogram representation suitable for large data sets with high dynamic ranges, producing small relative errors. Results might differ slightly from those obtained through less calculation-efficient methods.

#### Syntax

`arrayPercentile(expression, percentile)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array |  | The array from which to compute a percentile. |  |  |  | percentile |  | double, long |  | The percentile to compute, between 0 and 100. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value can be `boolean`, `double`, `duration`, or `timestamp`.

#### Examples

##### Example 1

```
fetch bizevents | filter matchesValue(event.category, {"/v1/trade/buy", "/v1/trade/sell"}) | summarize amounts = collectArray(amount), by: event.category | fieldsAdd arrayPercentile(amounts, 90)

```

## arrayRemoveNulls

Returns the array where NULL elements are removed.

#### Syntax

`arrayRemoveNulls(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, null, 7, 7, 1))
| fieldsAdd arrayRemoveNulls(a)

```

Query result:

| a |
| --- |
| arrayRemoveNulls(a) |
| `[2, 3, NULL, 7, 7, 1]` |
| `[2, 3, 7, 7, 1]` |

## arrayReverse

Returns the array with elements in reversed order.

#### Syntax

`arrayReverse(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arrayReverse(a)

```

Query result:

| a |
| --- |
| arrayReverse(a) |
| `[2, 3, 7, 7, 1]` |
| `[1, 7, 7, 3, 2]` |

## arraySize

Returns the size of an array.

#### Syntax

`arraySize(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arraySize(a)

```

Query result:

| a |
| --- |
| arraySize(a) |
| `[2, 3, 7, 7, 1]` |
| `5` |

## arraySlice

Extracts a slice from the input array using a `from` index (inclusive) and a `to` index (exclusive). Indexes that are `>= 0` are counted from the start of the array, and indexes `< 0` are counted from the end of the array. The index `0` represents the first array element and index `-1` represents the last array element. Positive indexes beyond the array length are clamped to the array end, and negative indexes beyond the start are clamped to the array start. If `from >= to`, the function returns an empty array.

#### Syntax

`arraySlice(array [, from] [, to])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |  | The array expression to get the slice from. |  |  |  | from |  | long |  | Index of the first element to include in the slice (inclusive). Default: `0`. |  |  |  | to |  | long |  | Index of the last element to include in the slice (exclusive). Default: array length. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(0, 1, 2, 3, 4))
| fieldsAdd arraySlice(a),
            arraySlice(a, from: 2),
            arraySlice(a, from: -2),
            arraySlice(a, to: -1),
            arraySlice(a, from: -100, to: 100),
            arraySlice(a, from: -1, to: 1),
            arraySlice(a, from: 100, to: 101)

```

Query result:

| a |  | arraySlice(a) |  | arraySlice(a, from: 2) |  | arraySlice(a, from: -2) |  | arraySlice(a, to: -1) |  | arraySlice(a, from: -100, to: 100) |  | arraySlice(a, from: -1, to: 1) |  | arraySlice(a, from: 100, to: 101) |  | `[0,1,2,3,4]` |  | `[0,1,2,3,4]` |  | `[2,3,4]` |  | `[3,4]` |  | `[0,1,2,3]` |  | `[0,1,2,3,4]` |  | `[]` |  | `[]` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## arraySort

Returns the array with elements sorted in ascending order by default. If you need to control the order, use the `direction` parameter.

#### Syntax

`arraySort(array, direction)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | direction |  | string |  | A sort order. Possible values: ascending, descending. Default: ascending. |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arraySort(a), arraySort(a, direction: "descending")

```

Query result:

| a |
| --- |
| arraySort(a) |
| arraySort(a, direction:"descending") |
| `[2, 3, 7, 7, 1]` |
| `[1, 2, 3, 7, 7]` |
| `[7, 7, 3, 2, 1]` |

## arraySum

Returns the sum of an array. Values that are not numeric are ignored. Returns 0 if there is no matching element.

#### Syntax

`arraySum(array)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | array |  | array |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd arraySum(a)

```

Query result:

| a |
| --- |
| arraySum(a) |
| `[2, 3, 7, 7, 1]` |
| `20` |

## arrayToString

Converts an array into a string. You can specify the optional `delimiter` parameter to add a delimiter between elements in the output string.

#### Syntax

`arrayToString(expression [, delimiter])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array |  | The array to convert to a string. |  |  |  | delimiter |  | string |  | The character(s) to insert between array elements. Default: `""` (none). |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(a = array(1, 2, 3)),
     record(a = array("D", "Q", "L"))
| fieldsAdd arrayToString(a), arrayToString(a, delimiter:", ")

```

Query result:

| a |  | arrayToString(a) |  | arrayToString(a, delimiter:", ") |  | `[1, 2, 3]` |  | `"123"` |  | `"1, 2, 3"` |  | `["D", "Q", "L"]` |  | `"DQL"` |  | `"D, Q, L"` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
