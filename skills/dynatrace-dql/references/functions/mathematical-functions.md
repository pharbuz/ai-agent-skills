> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions)

# Mathematical functions

Functions executing mathematical calculations.

## abs

Returns the absolute value of `numeric_expression`. Returns NULL if `numeric_expression` evaluates to NULL.

#### Syntax

`abs(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | double, long, duration |  | The numeric expression for which to calculate the absolute value. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `double`, `long`, or `duration`.

#### Examples

##### Example 1

```
data record(x = -42.13),
     record(x = 0),
     record(x = 6.8545)
| fieldsAdd abs(x)

```

Query result:

| x |  | abs(x) |  | `-42.13` |  | `42.13` |  | `0` |  | `0` |  | `6.8545` |  | `6.8545` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## acos

Computes arc cosine of `expression`. The returned angle is in the range `0.0` through pi. Returns `null` if `expression` evaluates to NULL.

#### Syntax

`acos(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the acos. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -1),
     record(x = 0),
     record(x = 1)
| fieldsAdd acos(x)

```

Query result:

| x |  | acos(x) |  | `-1` |  | `3.1416` |  | `0` |  | `1.5708` |  | `1` |  | `0` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## asin

Computes arc sine of `expression`. The returned angle is in the range `-pi/2` through `pi/2`. Returns `null` if `<expression>` evaluates to NULL.

#### Syntax

`asin(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the asin. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -1),
     record(x = 0),
     record(x = 1)
| fieldsAdd asin(x)

```

Query result:

| x |  | asin(x) |  | `-1` |  | `-1.5708` |  | `0` |  | `0` |  | `1` |  | `1.5708` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## atan

Computes the arc tangent of `expression`. The returned angle is in the range `-p/2` through `pi/2`. Returns `null` if `expression` evaluates to NULL.

#### Syntax

`atan(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the atan. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -1),
     record(x = 0),
     record(x = 1)
| fieldsAdd atan(x)

```

Query result:

| x |  | atan(x) |  | `-1` |  | `-0.7854` |  | `0` |  | `0` |  | `1` |  | `0.7854` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## atan2

Computes the angle theta from the conversion of rectangular coordinates (x, y) to polar coordinates (r, theta). Returns `null` if either of the expressions evaluates to NULL.

#### Syntax

`atan2(ordinate, abscissa)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| ordinate |  | double, long |  | The ordinate coordinate. |  |  |
| abscissa |  | double, long |  | The abscissa coordinate. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = 1, y = 1),
     record(x = 2, y = 3),
     record(x = 4, y = 5)
| fieldsAdd atan2(x, y)

```

Query result:

| x |  | y |  | atan2(x, y) |  | `1` |  | `1` |  | `0.7854` |  | `2` |  | `3` |  | `0.588` |  | `4` |  | `5` |  | `0.6747` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## bin

Rounds values down to a multiple of a given numeric `bin` size.

Used frequently in combination with `summarize , by: ....`. If it encounters a scattered set of values, they will be grouped into a smaller set of specific values.

#### Syntax

`bin(expression, interval)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | timestamp, long, double, duration |  | The expression that should be aligned. |  |  |
| interval |  | duration, double, long |  | The interval by which to align the expression. Constraints: statically evaluated. |  |  |
| at |  | timestamp, number, duration |  | The offset to which each interval should be shifted. Default: 0. Constraints: The offset to which each interval should be shifted. |  |  |

#### Returns

The data type of the returned value is `double`, `long`, `duration`, or `timestamp`.

#### Examples

##### Example 1

```
data record(x = -42.13),
     record(x = 0),
     record(x = 6.8545),
     record(x = 27)
| fieldsAdd bin(x, 10), bin(x, 10, at:5)

```

Query result:

| x |  | bin(x, 10) |  | bin(x, 10, at:5) |  | `-42.13` |  | `-50` |  | `-45` |  | `0` |  | `0` |  | `-5` |  | `6.8545` |  | `0` |  | `5` |  | `27` |  | `20` |  | `25` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400")),
     record(timestamp = toTimestamp("2022-12-24T18:13:23.672-0400")),
     record(timestamp = toTimestamp("2023-01-27T23:21:11.459-0400"))
| fieldsAdd bin(timestamp, 1m), bin(timestamp, 1d)

```

Query result:

| timestamp |  | bin(timestamp, 1m) |  | bin(timestamp, 1d) |  | `2019-08-01T13:30:00.000Z` |  | `2019-08-01T13:30:00.000Z` |  | `2019-08-01T00:00:00.000Z` |  | `2022-12-24T22:13:23.672Z` |  | `2022-12-24T22:13:00.000Z` |  | `2022-12-24T00:00:00.000Z` |  | `2023-01-28T03:21:11.459Z` |  | `2023-01-28T03:21:00.000Z` |  | `2023-01-28T00:00:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 3

In this example, we align the `timestamp` to noon.

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd bin(timestamp, 1d, at: 12h)

```

Query result:

| timestamp |  | bin(timestamp, 1d, at:12h) |  | `2019-08-01T13:30:00.000Z` |  | `2019-08-01T12:00:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- |

## ceil

Calculates the smallest (closest to negative infinity) `double` value greater than or equal to the `numeric_expression`; is equal to a mathematical integer. Returns `null` if `numeric_expression` evaluates to NULL. The return type is of the same type as the input parameter.

#### Syntax

`ceil(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression to be rounded up. |  |  |

#### Returns

The data type of the returned value is `double` or `long`.

#### Examples

##### Example 1

```
data record(x = -0.5),
     record(x = 0),
     record(x = 0.5)
| fieldsAdd ceil(x)

```

Query result:

| x |  | ceil(x) |  | `-0.5` |  | `0` |  | `0` |  | `0` |  | `0.5` |  | `1` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## cos

Computes the trigonometric cosine of an angle `expression` (in radians). Returns `null` if `expression` evaluates to NULL.

#### Syntax

`cos(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the sin. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -pi()),
     record(x = 0),
     record(x = pi())
| fieldsAdd cos(x)

```

Query result:

| x |  | cos(x) |  | `-3.1416` |  | `-1` |  | `0` |  | `1` |  | `3.1416` |  | `-1` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## cosh

Computes the hyperbolic cosine of an angle `<expression>`. Returns `null` if `<expression>` evaluates to NULL.

#### Syntax

`cosh(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the cosh. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -1),
     record(x = 0),
     record(x = 1)
| fieldsAdd cosh(x)

```

Query result:

| x |  | cosh(x) |  | `-1` |  | `1.5431` |  | `0` |  | `1` |  | `1` |  | `1.5431` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## cbrt

Calculates the real cubic root of a numeric expression.

#### Syntax

`cbrt (numeric_expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression for which to calculate the real cubic root. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -8),
     record(x = -42.13),
     record(x = 0),
     record(x = 6.8545)
| fieldsAdd cbrt(x)

```

Query result:

| x |  | cbrt(x) |  | `-8` |  | `-2` |  | `-42.13` |  | `-3.4796` |  | `0` |  | `0` |  | `6.8545` |  | `1.8996` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## degreeToRadian

Converts the numeric expression of an angle in degrees to an approximately equivalent angle as expressed in radians. Returns `null` if `numeric_expr` evaluates to NULL.

#### Syntax

`degreeToRadian(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The angle to be converted from radians to degrees. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(degree = 90),
     record(degree = 180)
| fieldsAdd degreeToRadian(degree)

```

Query result:

| degree |  | degreeToRadian(degree) |  | `90` |  | `1.5708` |  | `180` |  | `3.1416` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## e

Returns Euler’s number.

#### Syntax

`e()`

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record()
| fieldsAdd e()

```

Query result:

| e() |  | `2.7183` |
| --- | --- | --- |

## exp

Calculates the exponential function `e^x`, where `e` is the Euler's number and `x` is a numeric expression.

#### Syntax

`exp(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, duration, long |  | The numeric expression for which to calculate the exponential function. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = 1),
     record(x = 4)
| fieldsAdd exp(x)

```

Query result:

| x |  | exp(x) |  | `1` |  | `2.7183` |  | `4` |  | `54.5982` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## floor

Calculates the largest (closest to positive infinity) `double` value less than or equal to the `numeric_expression`; and is equal to a mathematical integer. Returns NULL if `numeric_expression` evaluates to NULL. The return type is of the same type as the input parameter.

#### Syntax

`floor(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression to be rounded down. |  |  |

#### Returns

The data type of the returned value is `double` or`long`.

#### Examples

##### Example 1

```
data record(x = -0.5),
     record(x = 0),
     record(x = 0.5)
| fieldsAdd floor(x)

```

Query result:

| x |  | floor(x) |  | `-0.5` |  | `-1` |  | `0` |  | `0` |  | `0.5` |  | `0` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## hypotenuse

Returns `sqrt(x^2 + y^2)`. Returns `null` if `expression` evaluates to NULL.

#### Syntax

`hypotenuse(x, y)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| x |  | double, long |  | Length of the first of the catheti. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = 1, y = 2),
     record(x = 3, y = 4),
     record(x = 5, y = 6)
| fieldsAdd hypotenuse(x, y)

```

Query result:

| x |  | y |  | hypotenuse(x, y) |  | `1` |  | `2` |  | `2.2361` |  | `3` |  | `4` |  | `5` |  | `5` |  | `6` |  | `7.8102` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## log

Calculates the natural logarithm (the base is `e`, the Euler's number) of a numeric expression.

#### Syntax

`log(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression for which to calculate the natural logarithm (base e). |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = e()),
     record(x = 0),
     record(x = 1),
     record(x = 6.8545)
| fieldsAdd log(x)

```

Query result:

| x |  | log(x) |  | `2.7183` |  | `1` |  | `0` |  | *null* |  | `1` |  | `0` |  | `6.8545` |  | `1.9249` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## log1p

Calculates log(1+x), where `log` is the natural logarithm and `x` is a numeric expression.

#### Syntax

`log1p(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression for which to add one and calculate the natural logarithm (base e). |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = 0),
     record(x = 6.8545)
| fieldsAdd log1p(x)

```

Query result:

| x |  | log1p(x) |  | `0` |  | `0` |  | `6.8545` |  | `2.0611` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## log10

Calculates the decadic (common) logarithm (the base is 10) of a numeric expression.

#### Syntax

`log10(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression for which to calculate the decadic logarithm (base 10). |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = 6.8545),
     record(x = 100)
| fieldsAdd log10(x)

```

Query result:

| x |  | log10(x) |  | `6.8545` |  | `0.836` |  | `100` |  | `2` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## pi

Returns the constant value of PI (Archimedes’ number).

#### Syntax

`pi()`

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record()
| fieldsAdd pi()

```

Query result:

| pi() |  | `3.1416` |
| --- | --- | --- |

## power

Raises a numeric expression to a given power.

#### Syntax

`power(base, exponent)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| base |  | double, long |  | The numeric expression acting as the base of the power calculation. |  |  |
| exponent |  | double, long |  | The numeric expression acting as the exponent of the power calculation. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(base = 2, exponent = 4),
     record(base = 3, exponent = 5)
| fieldsAdd power(base, exponent)

```

Query result:

| base |  | exponent |  | power(base, exponent) |  | `2` |  | `4` |  | `16` |  | `3` |  | `5` |  | `243` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## radianToDegree

Converts the numeric expression of an angle in radians to an approximately equivalent angle as expressed in degrees. Returns `null` if `numeric_expr` evaluates to NULL.

#### Syntax

`radianToDegree(numeric_expr)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The angle to be converted from radians to degrees. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(radian = pi() / 2),
     record(radian = pi())
| fieldsAdd radianToDegree(radian)

```

Query result:

| radian |  | radianToDegree(radian) |  | `1.5708` |  | `90` |  | `3.1416` |  | `180` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## random

Creates a random double value. Generated values aren't deterministic. The value range of the generated double value is between 0.0 (inclusive) and 1.0 (exclusive).

#### Syntax

`random()`

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record()
| fieldsAdd random()

```

Query result:

| random() |  | `0.563` |
| --- | --- | --- |

## range

Aligns the given value/timestamp to value range based on the provided alignment parameter. The `range` function is similar to the `bin` function, but produces a range instead, then provides information about the start and the end of the bin the value is aligned to.

#### Syntax

`range(expression, interval [, at])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expressions |  | expressions |  | The numeric, timestamp or duration expression that should be aligned into bins. |  |  |
| interval |  | expression |  | The size of bins produced and the values that are aligned to it. Constraints: numeric_expression, duration_expression. |  |  |
| at |  | expression |  | The starting value for the first bin that is produced. Default: 0, EPOCH. |  |  |

#### Returns

The data type of the returned value is `record`.

#### Examples

##### Example 1

```
data record(x = -42.13),
     record(x = 0),
     record(x = 6.8545),
     record(x = 27)
| fieldsAdd range(x, 10),
            range(x, 10, at: 5)

```

Query result:

| x |  | range(x, 10) |  | range(x, 10, at:5) |  | `-42.13` |  | **start**: `-50`**end**: `-40` |  | **start**: `-45`**end**: `-35` |  | `0` |  | **start**: `0`**end**: `10` |  | **start**: `-5`**end**: `5` |  | `6.8545` |  | **start**: `0`**end**: `10` |  | **start**: `5`**end**: `15` |  | `27` |  | **start**: `20`**end**: `30` |  | **start**: `25`**end**: `35` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400")),
     record(timestamp = toTimestamp("2022-12-24T18:13:23.672-0400")),
     record(timestamp = toTimestamp("2023-01-27T23:21:11.459-0400"))
| fieldsAdd range(timestamp, 1m),
            range(timestamp, 1d)

```

Query result:

| timestamp |  | range(timestamp, 1m) |  | range(timestamp, 1d) |  | `2019-08-01T13:30:00.000Z` |  | **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T13:31:00.000Z` |  | **start**: `2019-08-01T00:00:00.000Z`**end**: `2019-08-02T00:00:00.000Z` |  | `2022-12-24T22:13:23.672Z` |  | **start**: `2022-12-24T22:13:00.000Z`**end**: `2022-12-24T22:14:00.000Z` |  | **start**: `2022-12-24T00:00:00.000Z`**end**: `2022-12-25T00:00:00.000Z` |  | `2023-01-28T03:21:11.459Z` |  | **start**: `2023-01-28T03:21:00.000Z`**end**: `2023-01-28T03:22:00.000Z` |  | **start**: `2023-01-28T00:00:00.000Z`**end**: `2023-01-29T00:00:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 3

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd bin(timestamp, 1d, at: 12h)

```

Query result:

| timestamp |  | bin(timestamp, 1d, at:12h) |  | `2019-08-01T13:30:00.000Z` |  | `2019-08-01T12:00:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- |

## round

Rounds any numeric value to the specified number of decimal places. If you don't specify the number of decimal places, it rounds to the nearest integer.
The return type is of the same type as the input parameter.

#### Syntax

`round(expression [, decimals])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | Numeric expression to be rounded. |  |  |
| decimals |  | long |  | Number of places after the decimal point. |  |  |

#### Returns

The data type of the returned value is `double` or `long`.

#### Examples

##### Example 1

```
data record(x = -0.5),
     record(x = 0),
     record(x = 0.5),
     record(x = 0.55)
| fieldsAdd round(x),
            round(x, decimals: 1)

```

Query result:

| x |  | round(x) |  | round(x, decimals:1) |  | `-0.5` |  | `0` |  | `-0.5` |  | `0` |  | `0` |  | `0` |  | `0.5` |  | `1` |  | `0.5` |  | `0.55` |  | `1` |  | `0.6` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## signum

Returns the `signum` (sign) result of an argument. It returns one of four possible values: `-1` (if `numeric_expression` evaluates to a value less than `0`), `0` (if `numeric_expression` evaluates to `0`), `1` (if `numeric_expression` evaluates to a value greater than `0`), or `null` (if `numeric_expression` evaluates to NULL).
The return type is of the same type as the input parameter.

#### Syntax

`signum(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression for which to calculate the signum. |  |  |

#### Returns

The data type of the returned value is `double` or `long`.

#### Examples

##### Example 1

```
data record(x = -42.13),
     record(x = 0),
     record(x = 6.8545)
| fieldsAdd signum(x)

```

Query result:

| x |  | signum(x) |  | `-42.13` |  | `-1` |  | `0` |  | `0` |  | `6.8545` |  | `1` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## sin

Computes the trigonometric sine of angle `<expression>` (in radians). Returns `null` if `<expression>` evaluates to NULL.

#### Syntax

`sin(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the sin. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -pi() / 2),
     record(x = 0),
     record(x = pi() / 2)
| fieldsAdd sin(x)

```

Query result:

| x |  | sin(x) |  | `-1.5708` |  | `-1` |  | `0` |  | `0` |  | `1.5708` |  | `1` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## sinh

Computes the hyperbolic sine of `<expression>`. Returns `null` if `<expression>` evaluates to NULL.

#### Syntax

`sinh(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the sinh. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -1),
     record(x = 0),
     record(x = 1)
| fieldsAdd sinh(x)

```

Query result:

| x |  | sinh(x) |  | `-1` |  | `-1.1752` |  | `0` |  | `0` |  | `1` |  | `1.1752` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## sqrt

Computes the positive square root of a numeric expression.

#### Syntax

`sqrt(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression for which to calculate the square root. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = 4),
     record(x = 81),
     record(x = -14)
| fieldsAdd sqrt(x)

```

Query result:

| x |  | sqrt(x) |  | `4` |  | `2` |  | `81` |  | `9` |  | `-14` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## tan

Computes the trigonometric tangent of angle `expression` (in radians). Returns `null` if `expression` evaluates to NULL.

#### Syntax

`tan(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the tan. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -pi() / 4),
     record(x = 0),
     record(x = pi() / 4)
| fieldsAdd tan(x)

```

Query result:

| x |  | tan(x) |  | `-0.7854` |  | `-1` |  | `0` |  | `0` |  | `0.7854` |  | `1` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## tanh

Computes the hyperbolic tangent of `expression`. Returns `null` if `expression` evaluates to NULL.

#### Syntax

`tanh(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long |  | The numeric expression, angle in radians for which to calculate the tanh. |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(x = -1),
     record(x = 0),
     record(x = 1)
| fieldsAdd tanh(x)

```

Query result:

| x |  | tanh(x) |  | `-1` |  | `-0.7616` |  | `0` |  | `0` |  | `1` |  | `0.7616` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
