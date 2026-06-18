> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/boolean-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/boolean-functions)

# Boolean functions

Functions that evaluate boolean expressions and test the presence of values.

## isFalseOrNull

Evaluates if an expression is `false` or `null`.

#### Syntax

`isFalseOrNull(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | boolean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(value = true),
     record(value = false),
     record(value = null),
     record() // field does not exist
| fieldsAdd isFalseOrNull(value)

```

Query result:

| value |  | isFalseOrNull(value) |  | `true` |  | `false` |  | `false` |  | `true` |  | *null* |  | `true` |  | *null* |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## isNotNull

Tests if a value is not `null`.

#### Syntax

`isNotNull(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(value = true),
     record(value = false),
     record(value = "DQL is awesome!"),
     record(value = null),
     record() // field does not exist
| fieldsAdd isNotNull(value)

```

Query result:

| value |  | isNotNull(value) |  | `true` |  | `true` |  | `false` |  | `true` |  | `DQL is awesome!` |  | `true` |  | *null* |  | `false` |  | *null* |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## isNull

Tests if a value is `null`.

#### Syntax

`isNull(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(value = true),
     record(value = false),
     record(value = "DQL is awesome!"),
     record(value = null),
     record() // field does not exist
| fieldsAdd isNull(value)

```

Query result:

| value |  | isNull(value) |  | `true` |  | `false` |  | `false` |  | `false` |  | `DQL is awesome!` |  | `false` |  | *null* |  | `true` |  | *null* |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## isTrueOrNull

Evaluates if an expression is `true` or `null`.

#### Syntax

`isTrueOrNull(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | boolean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(value = true),
     record(value = false),
     record(value = null),
     record() // field does not exist
| fieldsAdd isTrueOrNull(value)

```

Query result:

| value |  | isTrueOrNull(value) |  | `true` |  | `true` |  | `false` |  | `false` |  | *null* |  | `true` |  | *null* |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
