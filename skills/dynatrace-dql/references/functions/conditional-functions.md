> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/conditional-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/conditional-functions)

# Conditional functions

Functions that return a conditional result.

## coalesce

Returns the first non-`null` argument, if any, otherwise `null`.

#### Syntax

`coalesce(expression, …)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | Returned if previous arguments are `null`. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

Returns the first non-`null` argument, if any, otherwise `null`.

#### Examples

##### Example 1

```
data record(a = "a", b = "b", c = "c"),
     record(b = "b", c = "c"),
     record(c = "c"),
     record()
| fieldsAdd coalesce(a, b, c)

```

Query result:

| a |  | b |  | c |  | coalesce(a, b, c) |  | `a` |  | `b` |  | `c` |  | `a` |  | *null* |  | `b` |  | `c` |  | `b` |  | *null* |  | *null* |  | `c` |  | `c` |  | *null* |  | *null* |  | *null* |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## if

Evaluates the condition, and returns the value of either the `then` or `else` parameter.

#### Syntax

`if(condition, then [, else])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| condition |  | boolean |  | The condition to check. |  |  |
| then |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | The expression if the condition is `true`. |  |  |
| else |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | The expression if the condition is `false` or `null`. |  |  |

#### Returns

Returns the value of the `then` parameter if the condition evaluated to `true`. Returns the value of the `else` parameter if the condition evaluated to `false` or `null`. Returns `null` if the condition evaluated to `false` or `null` and the `else` parameter is missing.

#### Examples

##### Example 1

```
data record(a = 10),
     record(a = 20)
| fieldsAdd if(a < 15, "a is smaller than 15"),
            if(a < 15, "a is smaller than 15", else: "a is not smaller than 15")

```

Query result:

| a |  | if(a < 15, "a is smaller than 15") |  | if(a < 15, "a is smaller than 15", else:"a is not smaller than 15") |  | `10` |  | `a is smaller than 15` |  | `a is smaller than 15` |  | `20` |  | *null* |  | `a is not smaller than 15` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
