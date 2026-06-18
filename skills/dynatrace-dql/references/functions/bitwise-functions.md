> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions)

# Bitwise functions

Bitwise operations performing on long expressions.

## bitwiseAnd

Calculates the bitwise `and` between two long expressions.

#### Syntax

`bitwiseAnd(long expression, long expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| firstExpression |  | long |  | The first long expression for the binary operation. |  |  |
| secondExpression |  | long |  | The second long expression for the binary operation. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 0, b = 0),
     record(a = 0, b = 1),
     record(a = 1, b = 0),
     record(a = 1, b = 1),
     record(a = 12, b = 10)
| fieldsAdd bitwiseAnd(a, b)

```

Query result:

| a |  | b |  | bitwiseAnd(a, b) |  | `0` |  | `0` |  | `0` |  | `0` |  | `1` |  | `0` |  | `1` |  | `0` |  | `0` |  | `1` |  | `1` |  | `1` |  | `12` |  | `10` |  | `8` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## bitwiseCountOnes

Counts the bits assigned to one of the long expressions.

#### Syntax

`bitwiseCountOnes(long expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | long |  | The long expression whose bits will be inverted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 0),
     record(a = 1),
     record(a = -1),
     record(a = 9223372036854775807),
     record(a = -9223372036854775807),
     record(a = 12)
| fieldsAdd bitwiseCountOnes(a)

```

Query result:

| a |  | bitwiseCountOnes(a) |  | `0` |  | `0` |  | `1` |  | `1` |  | `-1` |  | `64` |  | `9,223,372,036,854,776,000` |  | `63` |  | `-9,223,372,036,854,776,000` |  | `2` |  | `12` |  | `2` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## bitwiseNot

Inverts the bits included in the long expression.

#### Syntax

`bitwiseNot(long expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | long |  | The long expression whose bits will be inverted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 0),
     record(a = 1),
     record(a = -1),
     record(a = 9223372036854775807),
     record(a = -9223372036854775808),
     record(a = 12)
| fieldsAdd bitwiseNot(a)

```

Query result:

| a |  | bitwiseNot(a) |  | `0` |  | `-1` |  | `1` |  | `-2` |  | `-1` |  | `0` |  | `9,223,372,036,854,776,000` |  | `-9,223,372,036,854,776,000` |  | `-9,223,372,036,854,776,000` |  | `9,223,372,036,854,776,000` |  | `12` |  | `-13` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## bitwiseShiftLeft

Shifts the long expressions by the number of given bits to the left.

#### Syntax

`bitwiseShiftLeft(long expression, long expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | long |  | The long expression that will be bitwise shifted to the left. |  |  |
| numberOfBits |  | long |  | The number of bits by which the expression will be shifted left. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 0, bits = 1),
     record(a = 1, bits = 1),
     record(a = 1, bits = 2),
     record(a = 9223372036854775807, bits = 1),
     record(a = -9223372036854775808, bits = 1)
| fieldsAdd bitwiseShiftLeft(a, bits)

```

Query result:

| a |  | bits |  | bitwiseShiftLeft(a, bits) |  | `0` |  | `1` |  | `0` |  | `1` |  | `1` |  | `2` |  | `1` |  | `2` |  | `4` |  | `9,223,372,036,854,776,000` |  | `1` |  | `-2` |  | `-9,223,372,036,854,776,000` |  | `1` |  | `0` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## bitwiseShiftRight

Shifts the long expression by number of given bits to the right. It has an optional parameter `ignoreSign`, that defines, if the sign bit should be ignored. If the parameter is false, it can be compared to `>>` in Java, otherwise to `>>>`.

#### Syntax

`bitwiseShiftRight(long expression, long expression, ignoreSign: boolean)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | long |  | The long expression that will be bitwise shifted right. |  |  |
| numberOfBits |  | long |  | The number of bits by which the expression will be shifted right. |  |  |
| ignoreSign |  | boolean expression |  | The boolean expression that indicates if the sign bit should be ignored (treated like any bit) while shifting, If false, the sign bit is preserved and just the other bits are shifted. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 0, bits = 1),
     record(a = 1, bits = 1),
     record(a = 1, bits = 2),
     record(a = 9223372036854775807, bits = 1),
     record(a = -9223372036854775808, bits = 1),
     record(a = -1, bits = 2)
| fieldsAdd bitwiseShiftRight(a, bits, ignoreSign: false),
            bitwiseShiftRight(a, bits, ignoreSign: true)

```

Query result:

| a |  | bits |  | bitwiseShiftRight(a, bits, ignoreSign:FALSE) |  | bitwiseShiftRight(a, bits, ignoreSign:TRUE) |  | `0` |  | `1` |  | `0` |  | `0` |  | `1` |  | `1` |  | `0` |  | `0` |  | `1` |  | `2` |  | `0` |  | `0` |  | `9,223,372,036,854,776,000` |  | `1` |  | `4,611,686,018,427,388,000` |  | `4,611,686,018,427,388,000` |  | `-9,223,372,036,854,776,000` |  | `1` |  | `-4,611,686,018,427,388,000` |  | `4,611,686,018,427,388,000` |  | `-1` |  | `2` |  | `-1` |  | `4,611,686,018,427,388,000` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## bitwiseOr

Calculates the bitwise `or` between two long expressions.

#### Syntax

`bitwiseOr(long expression, long expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| firstExpression |  | long |  | The first long expression for the binary operation. |  |  |
| secondExpression |  | long |  | The second long expression for the binary operation. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 0, b = 0),
     record(a = 0, b = 1),
     record(a = 1, b = 0),
     record(a = 1, b = 1),
     record(a = 12, b = 10)
| fieldsAdd bitwiseOr(a, b)

```

Query result:

| a |  | b |  | bitwiseOr(a, b) |  | `0` |  | `0` |  | `0` |  | `0` |  | `1` |  | `1` |  | `1` |  | `0` |  | `1` |  | `1` |  | `1` |  | `1` |  | `12` |  | `10` |  | `14` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## bitwiseXor

Calculates the bitwise `xor` between two long expressions.

#### Syntax

`bitwiseXor(long expression, long expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| firstExpression |  | long |  | The first long expression for the binary operation. |  |  |
| secondExpression |  | long |  | The second long expression for the binary operation. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 0, b = 0),
     record(a = 0, b = 1),
     record(a = 1, b = 0),
     record(a = 1, b = 1),
     record(a = 12, b = 10)
| fieldsAdd bitwiseXor(a, b)

```

Query result:

| a |  | b |  | bitwiseXor(a, b) |  | `0` |  | `0` |  | `0` |  | `0` |  | `1` |  | `1` |  | `1` |  | `0` |  | `1` |  | `1` |  | `1` |  | `0` |  | `12` |  | `10` |  | `6` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
