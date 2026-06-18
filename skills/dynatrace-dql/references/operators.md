> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/operators](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/operators)

# DQL operators

The following table shows a list of all the DQL operators.

| Operator |  | Description |
| --- | --- | --- |
| `+` |  | Addition |
| `-` |  | Subtraction or arithmetic negation |
| `*` |  | Multiplication |
| `/` |  | Division |
| `%` |  | Modulo |
| `<` |  | Less than |
| `<=` |  | Less than or equal to |
| `>` |  | Greater than |
| `>=` |  | Greater than or equal to |
| `==` |  | Equals |
| `!=` |  | Does not equal |
| `not` |  | Logical NOT (negation) |
| `and` |  | Logical AND |
| `or` |  | Logical OR |
| `xor` |  | Logical XOR (exclusive or) |
| `in` |  | Subquery comparison |
| `@` |  | Time alignment |
| `~` |  | Search |

The precedence for the operators is as follows (from strongest to weakest):

- `-` (arithmetic negation)

- `*`, `/`, `%`

- `@`

- `+`, `-` (subtraction)

- `~`

- `==`, `!=`, `>`, `>=`, `<`, `<=`

- `in`

- `not`

- `and`

- `xor`

- `or`

## Arithmetic operators

You can use arithmetic operators with numbers, represented by both the types `long` or `double`. In addition, some operators support the types `timestamp`, `timeframe`, `duration` or `ip`.

| Operator |  | Description |  | Example |
| --- | --- | --- | --- | --- |
| `+` |  | Addition |  | `2 + 2.5` |
| `-` |  | Subtraction |  | `0.2 - 0.11` |
| `*` |  | Multiplication |  | `4 * 5`, `60 * 1s` |
| `/` |  | Division |  | `10 / 2`, `1h / 60` |
| `%` |  | Modulo |  | `4 % 2` |
| `-` |  | Arithmetic negation |  | `-1` |

### ADDITION

| ADDITION |
| --- |
| Long |
| Double |
| String |
| Boolean |
| Timestamp |
| Duration |
| Timeframe |
| Binary |
| IP |
| UID |
| Array |
| Record |
| Long |
| (long) |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
| (IP) |
|  |
|  |
|  |
| Double |
| (double) |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
| (IP) |
|  |
|  |
|  |
| String |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Boolean |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timestamp |
|  |
|  |
|  |
|  |
|  |
| (timestamp) |
|  |
|  |
|  |
|  |
|  |
|  |
| Duration |
|  |
|  |
|  |
|  |
| (timestamp) |
| (duration) |
| (timeframe) |
|  |
|  |
|  |
|  |
|  |
| Timeframe |
|  |
|  |
|  |
|  |
|  |
| (timeframe) |
|  |
|  |
|  |
|  |
|  |
|  |
| Binary |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| IP |
| (IP) |
| (IP) |
|  |
|  |
|  |
|  |
|  |
|  |
| (IP) |
|  |
|  |
|  |
| UID |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Array |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Record |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

### SUBTRACTION

| SUBTRACTION |
| --- |
| Long |
| Double |
| String |
| Boolean |
| Timestamp |
| Duration |
| Timeframe |
| Binary |
| IP |
| UID |
| Array |
| Record |
| Long |
| (long) |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Double |
| (double) |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| String |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Boolean |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timestamp |
|  |
|  |
|  |
|  |
| (duration) |
| (timestamp) |
|  |
|  |
|  |
|  |
|  |
|  |
| Duration |
|  |
|  |
|  |
|  |
|  |
| (duration) |
|  |
|  |
|  |
|  |
|  |
|  |
| Timeframe |
|  |
|  |
|  |
|  |
|  |
| (timeframe) |
|  |
|  |
|  |
|  |
|  |
|  |
| Binary |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| IP |
| (IP) |
| (IP) |
|  |
|  |
|  |
|  |
|  |
|  |
| (IP) |
|  |
|  |
|  |
| UID |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Array |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Record |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

### MULTIPLICATION

| MULTIPLICATION |
| --- |
| Long |
| Double |
| String |
| Boolean |
| Timestamp |
| Duration |
| Timeframe |
| Binary |
| IP |
| UID |
| Array |
| Record |
| Long |
| (long) |
| (double) |
|  |
|  |
|  |
| (duration) |
|  |
|  |
|  |
|  |
|  |
|  |
| Double |
| (double) |
| (double) |
|  |
|  |
|  |
| (duration, rounded to full nanos) |
|  |
|  |
|  |
|  |
|  |
|  |
| String |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Boolean |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timestamp |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Duration |
| (duration) |
| (duration, rounded to full nanos) |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timeframe |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Binary |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| IP |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| UID |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Array |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Record |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

### DIVISION

When you divide a `long` value by another `long` value using the `/` operator, the result is also a `long` value, and any fractional part is discarded. To get a result with the fractional part (a `double` value), you need to convert or cast at least one of the operands to `double` (e.g., by using the [toDouble](/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toDouble) function).

| DIVISION |
| --- |
| Long |
| Double |
| String |
| Boolean |
| Timestamp |
| Duration |
| Timeframe |
| Binary |
| IP |
| UID |
| Array |
| Record |
| Long |
| (long) |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Double |
| (double) |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| String |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Boolean |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timestamp |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Duration |
| (duration rounded to full nanos) |
| (duration rounded to full nanos) |
|  |
|  |
|  |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
| Timeframe |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Binary |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| IP |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| UID |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Array |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Record |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

The data type resulting from the operation is indicated in parentheses in the table above.

### MODULO

| MODULO |
| --- |
| Long |
| Double |
| String |
| Boolean |
| Timestamp |
| Duration |
| Timeframe |
| Binary |
| IP |
| UID |
| Array |
| Record |
| Long |
| (long) |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Double |
| (double) |
| (double) |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| String |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Boolean |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timestamp |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Duration |
|  |
|  |
|  |
|  |
|  |
| (duration) |
|  |
|  |
|  |
|  |
|  |
|  |
| Timeframe |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Binary |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| IP |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| UID |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Array |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Record |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

### ARITHMETIC NEGATION

| NEGATION |
| --- |
| Long |
| Double |
| String |
| Boolean |
| Timestamp |
| Duration |
| Timeframe |
| Binary |
| IP |
| UID |
| Array |
| Record |
| SELF |
| (long) |
| (double) |
|  |
|  |
|  |
| (duration) |
|  |
|  |
|  |
|  |
|  |
|  |

## Comparison operators

| Operator |  | Description |  | Example |
| --- | --- | --- | --- | --- |
| `<` |  | Less than |  | `8 < 9`, `now()-1m < now()` |
| `<=` |  | Less than or equal to |  | `4 <= 5` |
| `>` |  | Greater than |  | `5 > 4`, `"a" > "A"` |
| `>=` |  | Greater than or equal to |  | `4 >=4` |

### Comparison operators (<, <=, >, >=)

- (  ) - `true` or `false` based on the result of the operator

- (  ) - `null`

| <, <=, >, >= |
| --- |
| Long |
| Double |
| String |
| Boolean |
| Timestamp |
| Duration |
| Timeframe |
| Binary |
| IP |
| UID |
| Array |
| Record |
| Long |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Double |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| String |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Boolean |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timestamp |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Duration |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timeframe |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Binary |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| IP |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| UID |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Array |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Record |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

## Equality operators

| Operator |  | Description |  | Example |
| --- | --- | --- | --- | --- |
| `==` |  | Equals |  | `2 == 2` |
| `!=` |  | Does not equal |  | `1 != 2` |

Equality comparisons (`==`, `!=`) use a tri-state boolean algebra (`true`, `false`, `null`). This means that if any side of the equality comparison is `null`, the overall result of the comparison is `null`.
There are four DQL functions that cover scenarios where missing or `null` records need to be retrieved:

- The [`isTrueOrNull` function](/platform/grail/dynatrace-query-language/functions/boolean-functions#isTrueOrNull)

- The [`isFalseOrNull` function](/platform/grail/dynatrace-query-language/functions/boolean-functions#isFalseOrNull)

- The [`isNull` function](/platform/grail/dynatrace-query-language/functions/boolean-functions#isNull)

- The [`isNotNull` function](/platform/grail/dynatrace-query-language/functions/boolean-functions#isNotNull)

For example, the below query that uses basic filtering does not provide records with `null` or missing values:

```
fetch logs
| filter log.source != "logsourcename"  // does not provide the records where `log.source` is null or missing

```

However, using the `isTrueOrNull` function includes those records with `null` and missing values:

```
fetch logs
| filter isTrueOrNull(log.source != "logsourcename") // also provides the records where `log.source` is null or missing

```

### Equality operators (==, !=)

- (  ) - `false` for non-comparable types in case of `==` operator, `true` for non-compatible types in case of `!=` operator

- (  ) - `true` or `false` based on the result of the operator

- `null` - if one of the operands is `null`

- `null == null` - `null`

| ==, != |
| --- |
| Long |
| Double |
| String |
| Boolean |
| Timestamp |
| Duration |
| Timeframe |
| Binary |
| IP |
| UID |
| Array |
| Record |
| Long |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Double |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| String |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Boolean |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timestamp |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Duration |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Timeframe |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Binary |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| IP |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| UID |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Array |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Record |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

## Logical operators

| Operator |  | Description |  | Example (yields true) |
| --- | --- | --- | --- | --- |
| `not` |  | Logical NOT (negation) - Negates a logical state |  | `not 2==1` |
| `and` |  | Logical AND (multiplication) - Yields `true` if both operands are `true`. |  | `not 2==1 and 1<2` |
| `or` |  | Logical OR (addition) - Yields `true` if one of the operands is `true`, regardless of the other operand. |  | `1 < 2 or 1 > 2` |
| `xor` |  | Logical XOR (exclusive OR) - Yields `true` if one of the operands is `true`, but `false` in case both are `true`. |  | `1 < 2 xor 1 > 2` |

The behavior of logical operators follows the tri-state boolean logic.

-

**AND**

- `true` AND `null` = `null`

- `null` AND `true` = `null`

- `false` AND `null` = `false`

- `null` AND `false` = `false`

- `null` AND `null` = `null`

-

**OR**

- `true` OR `null` = `true`

- `null` OR `true` = `true`

- `false` OR `null` = `null`

- `null` OR `false` = `null`

- `null` OR `null` = `null`

-

**XOR**

- `true` XOR `null` = `null`

- `null` XOR `true` = `null`

- `false` XOR `null` = `null`

- `null` XOR `false` = `null`

- `null` XOR `null` = `null`

-

**NOT**

- NOT `null` = `null`

## Iterative expressions

Iterative expressions allow you to perform element-wise operations on arrays without expanding them into separate records.

The core mechanism behind iterative expressions is the `[]` operator appended to an array, which can be referenced by a field name or any array expression in general. Writing `myArray[]` tells DQL to iterate over each element of `myArray`. You can also access nested fields within arrays of records using the syntax `myArray[][fieldName]`, which iterates over each record in the array and extracts the specified field. Similarly, you can also use nested arrays and iterate along one dimension such as with `myArray[][0]`.

DQL provides iterative functions such as `iAny()` and `iCollectArray()`, that consume the per-element results. `iIndex()` is a companion function available in any iterative expression that returns the 0-based integer index of the current element.

When DQL encounters an iterative expression, it follows these steps:

1.

2.
- Identify all `[]` references to determine which arrays drive the iteration.
3.

4.
- Determine the iteration length by the size of the array(s) referenced by `[]`. If multiple arrays are referenced, they must all have the same length, otherwise the result is `null`.
5.

6.
- Evaluate the expression for each index by substituting the `i`-th element of each `[]` referenced array.
7.

8.
- Process results: pass the per-index results to the enclosing iterative function, or `iCollectArray()` if no iterative function is present.
9.

##### Implicit wrapping

When an iterative expression appears outside of an explicit iterative function, such as `iAny()` or `iCollectArray()`, DQL implicitly wraps it in `iCollectArray()`. This means the per-element results are automatically collected into a new array.

In other words, these two statements are equivalent:

```
| fieldsAdd a[] * b[]

```

```
| fieldsAdd iCollectArray(a[] * b[])

```

Both evaluate `a[i] * b[i]` for each index `i` and collect the results into an array. This implicit wrapping allows you to write concise element-wise expressions directly in DQL without always spelling out `iCollectArray(...)`.

##### Element-wise evaluation

When arrays are referenced with `[]`, DQL performs element-wise operations. The implicit `iCollectArray()` wrapping applies in the following example as well:

```
data record(a = array(1, 2, 3), b = array(10, 20, 30)),
     record(a = array(1, 2, 3), b = array(10, 20)),
     record(a = array(1, 2, 3), b = null)
| fieldsAdd a[] * b[]

```

Query result:

| a |  | b |  | a[] * b[] |  | `[1, 2, 3]` |  | `[10, 20, 30]` |  | `[10, 40, 90]` |  | `[1, 2, 3]` |  | `[10, 20]` |  | `null` |  | `[1, 2, 3]` |  | `null` |  | `null` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

The iterative expression evaluates to `null` for records where `a` and `b` are not both arrays of equal size.

### iAny

Checks an iterative boolean expression. Returns `true` if the expression evaluated to `true` for at least one element, `false` if it was never `true` (non-boolean values are treated as `false`), or `null` if all elements are `null`.

##### Example 1: Check for any array element to match a condition

```
data record(a = array(1, 2, 3)),
     record(a = array(4, 5, 6))
| fieldsAdd iAny(a[] >= 4)

```

Query result:

| a |  | iAny(a[] >= 4) |  | `[1, 2, 3]` |  | `false` |  | `[4, 5, 6]` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2: Evaluate an array of records

```
data record(a = array(record(b = 1), record(b = 2), record(b = 3))),
     record(a = array(record(b = 4), record(b = 5), record(b = 6)))
| fieldsAdd iAny(a[][b] >= 4)

```

Query result:

| a |  | iAny(a[][b] >= 4) |  | [**b:** `1`, **b:** `2`, **b:** `3`] |  | `false` |  | [**b:** `4`, **b:** `5`, **b:** `6`] |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 3: Find out if any or all elements do not match a condition

```
data record(technologies = array("Java", "Python")),
     record(technologies = array("Go", "Rust")),
     record(technologies = array(null, null))
| fieldsAdd no_java      = not iAny(technologies[] == "Java"),
            any_but_java = iAny(not technologies[] == "Java")

```

Query result:

| technologies |  | no_java |  | any_but_java |  | `[Java, Python]` |  | `false` |  | `true` |  | `[Go, Rust]` |  | `true` |  | `true` |  | `[null, null]` |  | `null` |  | `null` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

When all array elements are `null`, both expressions return `null`. `iAny` cannot resolve to `true` or `false` without at least one definitive value. Consequently, records with fully `null` arrays will never pass a `filter iAny(...)` regardless of where `not` is placed.

##### Example 4: Check if all elements of an array are inside another array

This pattern uses double negation: `not in(needle[], haystack)` is `true` for each element of `needle` that is absent from `haystack`. `iAny(...)` returns `true` if at least one element is missing. Negating the whole result with `not` means the expression is `true` only when no element is missing — that is, all elements of `needle` are contained in `haystack`.

```
data record(needle = array(1, 2), haystack = array(1, 2, 3)),
     record(needle = array(3, 4), haystack = array(1, 2, 3))
| fieldsAdd not iAny(not in(needle[], haystack))

```

Query result:

| needle |  | haystack |  | not iAny(not in(needle[], haystack)) |  | `[1, 2]` |  | `[1, 2, 3]` |  | `true` |  | `[3, 4]` |  | `[1, 2, 3]` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### iCollectArray

Collects the results of an iterative expression into a new array. Returns `null` if the expression can't be evaluated (for example, when referenced arrays differ in length or any referenced array is `null`).

##### Example 1: Collect per-element results into a new array

```
data record(a = array(1, 2, 3), b = array(10, 20, 30))
| fieldsAdd iCollectArray(a[] + b[])

```

Query result:

| a |  | b |  | iCollectArray(a[] + b[]) |  | `[1, 2, 3]` |  | `[10, 20, 30]` |  | `[11, 22, 33]` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2: Process fields from an array of records

```
data record(services = array(record(name = "auth",    latency = 12),
                             record(name = "gateway", latency = 8),
                             record(name = "cache",   latency = 5)))
| fieldsAdd total_latency = arraySum(iCollectArray(services[][latency]))
| fieldsAdd service_names = iCollectArray(services[][name])

```

Query result:

| services |  | total_latency |  | service_names |  | [**name:** `auth` **latency:** `12`, **name:** `gateway` **latency:** `8`, **name:** `cache`, **latency:** `5`] |  | `25` |  | `[auth, gateway, cache]` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

For `total_latency` it is important to place `iCollectArray()` inside `arraySum(...)`. Otherwise `iCollectArray()` would be implicitly added enclosing `arraySum()`. For `service_names`, explicitly adding `iCollectArray(...)` is optional.

##### Example 3: Element-wise operation on two arrays with `null` fallback

```
data record(a = array(1, 2, 3), b = array(10, 20, 30)),
     record(a = array(1, 2, 3), b = null)
| fieldsAdd c = if(isNotNull(b), iCollectArray(a[] * b[]), else: a)

```

Query result:

| a |  | b |  | c |  | `[1, 2, 3]` |  | `[10, 20, 30]` |  | `[10, 40, 90]` |  | `[1, 2, 3]` |  | `null` |  | `[1, 2, 3]` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

It is important to add `iCollectArray()` explicitly within the `if(...)` function. Otherwise, the whole `if()` function gets evaluated repeatedly, and the iterative expression evaluates to `null` when `a` or `b` are not arrays or are not the same size.


### iIndex

Returns the 0-based integer index of the current element in the enclosing iterative expression. Use it to pair each array element with its position or to compute index-dependent transformations.

`iIndex()` only works in expressions where at least one iterative expression (`[]`) is present.

##### Example 1: Pair each element with its index

```
data record(a = array(2, 3, 7, 7, 1))
| fieldsAdd a_indexed = record(value = a[], index = iIndex())

```

Query result:

| a |  | a_indexed |  | `[2, 3, 7, 7, 1]` |  | [**index:** `0` **value:** `2`, **index:** `1` **value:** `3`, **index:** `2` **value:** `7`, **index:** `3` **value:** `7`, **index:** `4` **value:** `1`] |
| --- | --- | --- | --- | --- | --- | --- |

##### Example 2: Expand an array with its indices

```
data record(a = array(2, 3, 7, 7, 1))
| fields a = record(value = a[], index = iIndex())
| expand a
| fields index = a[index], value = a[value]

```

Query result:

| index |  | value |  | `0` |  | `2` |  | `1` |  | `3` |  | `2` |  | `7` |  | `3` |  | `7` |  | `4` |  | `1` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Operators for subqueries

### in

The `in` comparison operator evaluates the occurrence of a value returned by the left side's expression within a list of values returned by the right side's DQL subquery.

**Syntax**

`expression in [execution block]`

**Usage and constraints**

| Name |  | Type |  | Mandatory |  | Constraints |  | Description |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| left side |  | expression |  | yes |  | Either a field identifier or an expression. |  | The element to be found in the list returned by the right side's subquery. |  | right side |  | execution block |  | yes |  | It has to return a single field providing a list of values. |  | The DQL Subquery which returns the list of values to compare against. |

**Example**

This example shows how to use the `in` keyword for filtering a host metric for the host's attribute:

```
timeseries avg(dt.host.cpu.usage), filter:dt.entity.host in [fetch dt.entity.host
 | fieldsAdd tags
 | expand tags
 | filter tags == "ServiceNow" | fields id]

```

## Time alignment

The `@` operator aligns a timestamp to the provided time unit. It rounds down the timestamp to the beginning of the time unit.

#### Syntax

`[timestamp|duration|calendarDuration] @ unit`

#### Left side

On the left side of the `@` operator, you can use a `timestamp` expression, a `duration` expression, or a calendar duration.

If you use the `@` operator without an expression on the left side, the operator will use the timestamp expression `now()` and will align the current time to the time unit. For example, `@h` is the beginning of the current hour, and equivalent to `now()@h`. Expressions of type `duration` and calendar durations are considered as an offset to `now()`.

For example, `-2M@..`. is equivalent to `(now() - 2M)@...`.

#### Right side

The time unit can be any DQL supported [duration unit](/platform/grail/dynatrace-query-language/data-types#duration) including `s` (second), `m` (minute), `h` (hour), or a calendar duration unit like `d` (day), `w` (week), `M` (month), `q` (quarter), and `y` (year).

Duration units (`h`, `m`, `s`, `ms`, `us`, and `ns`) allow to add a factor, for example, `@3h`.

Leaving the factor out is equivalent to setting it to `1`. Note the following constraints when adding such factor:

- `h` supports all divisors of `24`: `1h`, `2h`, `3h`, `4h`, `6h`, `8h`, `12h`, `24h`. `@24h` is similar to `@1d` but might differ in the case of daylight-saving times.

- `m` and `s` support all divisors of `60`: `1m`, `2m`, `3m`, `4m`, `5m`, `6m`, `10m`, `12m`, `15m`, `20m`, `30m`, `60m`, and equivalently for `s`.

- `ms`, `us`, and `ns` support all divisors of `1000`.

By default, the week unit `w` uses the first day of the week as defined by your configured locale.
To explicitly specify the first day of the week, you can use the following time units:

- `w0` (Sunday)

- `w1` (Monday)

- `w2` (Tuesday)

- `w3` (Wednesday)

- `w4` (Thursday)

- `w5` (Friday)

- `w6` (Saturday)

- `w7` (Sunday)

For example, `@w1` means midnight of Monday of the current week.

##### Examples

For the following examples, the current time is Wednesday, 04 September 2024, 14:47:05+0200.

| Time modifier |  | Description |  | Resulting time |
| --- | --- | --- | --- | --- |
| `-2h@h` |  | 2 hours ago, aligned to the hour |  | Wednesday, 04 September 2024, 12:00:00+0200 |
| `-1d@d` |  | Yesterday, aligned to the day |  | Tuesday, 03 September 2024, 00:00:00+0200 |
| `-7d@d` |  | 7 days ago, aligned to the day |  | Wednesday, 28 August 2024, 00:00:00+0200 |
| `@w0` |  | Start of this week, from Sunday |  | Sunday, 01 September 2024, 00:00:00+0200 |
| `@w1` |  | Start of this week, from Monday |  | Monday, 02 September 2024, 00:00:00+0200 |
| `@M` |  | Start of this month |  | Sunday, 01 September 2024, 00:00:00+0200 |
| `-1M@M` |  | Start of last month |  | Thursday, 01 August 2024, 00:00:00+0200 |
| `@q` |  | Start of this quarter |  | Monday, 01 July 2024, 00:00:00+0200 |
| `@y` |  | Start of this year |  | Monday, 01 January 2024, 00:00:00+0100 |

## Search

You can use the `~` operator in expressions to match the value of an expression against a given search string. The performed comparison is case-insensitive and supports pattern matching using wildcards. The `~` operator returns a `boolean` value: `true` in case of a match, and `false` otherwise.

#### Syntax

`expression ~ "string literal"`

#### Left side

You can use any expression on the left side of the `~` operator. For details on how different data types work with this operator, see the [Returns](#search-returns) section.

#### Right side

The string literal to search for. It can be one of the following:

-

A search string without a wildcard (`*`). For example:

```
content ~ "error"

```

-

A search string with wildcard (`*`) characters. For example:

```
user ~ "*dynatrace.com"

```

A search string supports a maximum of 64 wildcard characters. Consecutive wildcards (for example, `**`) aren't supported.

#### Returns

##### Search strings without wildcards

The `~` operator searches the value as a string token inside a string. Its behavior depends on the data type of the expression on the left side:

-

If the expression is of type `string`, the operator searches the value as a token inside the string. It's case-insensitive. For example, `"Hello World"` matches `~"world"`, but `"HelloWorld"` doesn't.

-

If the expression is of type `long`, `double`, `smartscape ID`, `IP address`, or `UID`, the operator only matches if the string representation of its value is equal to the search string. For example, the IP address `192.0.0.1` matches `~"192.0.0.1"`, but not `~"192"`.

-

If the expression is of type `array`, each element is checked. The operator matches if at least one of the elements in the array does.

-

If the expression is of type `record`, the operator matches if any field name or value matches.

-

If the expression is of type `boolean`, `timestamp`, `duration`, or `binary`, the result is always false.

| Expression type |  | Expression value |  | Operation |  | Result |  | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| String |  | `"Hello WORLD!"` |  | `~"world"` |  | `true` |  |  |
| String |  | `"helloWorld"` |  | `~"World"` |  | `false` |  | `helloWorld` is one token since there are no separators. |
| String |  | `"192.168.0.7"` |  | `~"192"` |  | `true` |  | As it’s a string, the field has four tokens. |
| IP |  | `192.168.0.7` |  | `~"192"` |  | `false` |  | Only strings are tokenized. |
| IP |  | `192.168.0.7` |  | `~"192.168.0.7"` |  | `true` |  | The value is auto-converted, so there's an exact match. |
| Long |  | `12` |  | `~"12"` |  | `true` |  | The value is auto-converted, so there's an exact match. |
| UID |  | `uuid(1,2)` |  | `~"00000000-0000-0001-0000-000000000002"` |  | `true` |  | The value is not tokenized, but can be auto-converted. |
| Smartscape ID |  | `smartscapeId("HOST", 1)` |  | `~"HOST-0000000000000001"` |  | `true` |  | The value is auto-converted. |
| Smartscape ID |  | `smartscapeId("HOST", 1)` |  | `~"host-0000000000000001"` |  | `false` |  | For a Smartscape ID, the check is case-sensitive. |
| Smartscape ID |  | `smartscapeId("HOST", 1)` |  | `~"HOST"` |  | `false` |  | The value isn't tokenized. |
| Record |  | `record(firstName="John",lastName="Doe")` |  | `~"john"` |  | `true` |  | Search also works in nested fields. |
| Record |  | `record(firstName="John",lastName="Doe")` |  | `~"lastName"` |  | `true` |  | Search also works in the names of nested fields. |
| Record |  | `record(firstName="John",lastName="Doe")` |  | `~"name"` |  | `false` |  | `firstName` and `lastName` are one token since they don't contain separators. |
| Record |  | `record(first name="John",last name="Doe")` |  | `~"name"` |  | `true` |  | Search also works in the names of nested fields. |
| Array |  | `array(1,2,3,5,8,13)` |  | `~"3"` |  | `true` |  | One element of the array is 3, which can be auto-converted to match `~"3"`. |
| Boolean |  | `true` |  | `~"true"` |  | `false` |  | Booleans aren't supported. |
| Duration |  | `1h` |  | `~"1h"` |  | `false` |  | Durations aren't supported. |

##### Search strings with wildcards

The `~` operator searches the pattern in the tokens of a string. Its behavior depends on the data type of the expression on the left side:

- If the expression is of type `string`, the result is true if at least one of the tokens matches the pattern.

- If the expression is of type `array`, the result is true if one of the elements of the array matches the pattern.

- If the expression is of type `record`, the result is true if the name or value of a nested field matches the pattern.

- If the expression is of any other type (`long`, `double`, `smartscapeId`, `IP address`, `UID`, `boolean`, `timestamp`, `duration`, or `binary`) patterns aren't supported and the result is always `false`.

| Expression type |  | Expression value |  | Operation |  | Result |  | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| String |  | `"AuthenticationError"` |  | `~"*error"` |  | `true` |  |  |
| String |  | `"There was an AuthenticationError"` |  | `~"authentication*"` |  | `true` |  |  |
| String |  | `"There was an NoAuthenticationError"` |  | `~"authentication*"` |  | `false` |  |  |
| String |  | `"helloWorld"` |  | `~"*ow*"` |  | `true` |  |  |
| String |  | `"hello world"` |  | `~"*ow*"` |  | `false` |  |  |
| String |  | `"192.168.0.7"` |  | `~"192.168.*"` |  | `true` |  | It matches as it's a string and not an IP address. |
| Record |  |  |  |  |  |  |  |  |
| `record(firstName="John",lastName="Doe")` |  |  |  |  |  |  |  |  |
| `~"*name"` |  | `true` |  | The string matches the name of the nested field in the record. |  |  |  |  |
| Record |  | `record(firstName="John",lastName="Doe")` |  | `~"*do*"` |  | `true` |  | The string matches the record. |
| Array |  | `array("hello", "world", "myCustomName")` |  | `~"my*"` |  | `true` |  | The string matches within the array. |
| IP |  | `192.168.0.7` |  | `~"192*"` |  | `false` |  | Only strings allow patterns. |
| Long |  | `192` |  | `~"1*"` |  | `false` |  | Only strings allow patterns. |
| Smartscape ID |  | `smartscapeId("HOST", 1)` |  | `~"HOST*"` |  | `false` |  | Only strings allow patterns. |
| Boolean |  | `true` |  | `~"t*"` |  | `false` |  | Only strings allow patterns. |
| Duration |  | `1h` |  | `~"*h"` |  | `false` |  | Only strings allow patterns. |
