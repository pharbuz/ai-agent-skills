> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions)

# Conversion and casting functions

Conversion functions convert the expression or value from one data type to another type.

## Converting data types

Functions prefixed with `as(Type)` ensure that a value is of a target type. If the data type is incompatible, they return `null`. These functions are applicable after parsing.

```
...
| parse content, "LD'DQL 'KVP{LD:key'='(LONG:valueLong| BOOLEAN:valueBoolean| [!;]*:valueStr)';'?}:q"
| fields timestamp, asLong(q[workTime])

```

### Casting input data type to the target data type matrix

The `as*T` will try to cast the input to `T` but won't perform any conversions, it will cause an exception for strongly typed fields (marked as  ) and null for incompatible data types (empty cell).

`asT(arg) => if(typeOf(arg) == ’T’, arg)`

| as*T |
| --- |
| asNumber |
| asInteger |
| asLong |
| asDouble |
| asString |
| asBoolean |
| asTimestamp |
| asDuration |
| asTimeframe |
| asGeopoint |
| asIpAddress |
| asSummaryStats |
| asBinary |
| asArray |
| asRecord |
| `Integer` |
| `Integer` |
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
|  |
|  |
| `Long` |
| `Long` |
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
|  |
|  |
| `Double` |
| `Double` |
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
|  |
|  |
| `String` |
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
|  |
|  |
|  |
| `Boolean` |
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
|  |
|  |
|  |
| `Timestamp` |
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
|  |
|  |
|  |
| `Duration` |
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
|  |
|  |
|  |
| `Timeframe` |
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
|  |
|  |
|  |
| `Geopoint` |
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
|  |
|  |
|  |
| `IpAddress` |
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
|  |
|  |
|  |
| `Binary` |
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
|  |
|  |
|  |
| `Array` |
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
|  |
|  |
|  |
| `Record` |
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
|  |
|  |
|  |
| `V<Integer>` |
| `V<Integer>` |
|  |
| `V<Long>` |
| `V<Long>` |
|  |
| `V<Double>` |
| `V<Double>` |
|  |
| `V<String>` |
|  |
| `V<Boolean>` |
|  |
| `V<Timestamp>` |
|  |
| `V<Duration>` |
|  |
| `V<Timeframe>` |
|  |
| `V<Geopoint>` |
|  |
| `V<IpAddress>` |
|  |
| `V<SummaryStats>` |
|  |
| `V<Binary>` |
|  |
| `V<Array>` |
|  |
| `V<Record>` |
| `V<Record>` |

## asArray

Returns array value if the value is `array`, otherwise, returns `null`.

#### Syntax

`asArray(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | array |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = "DQL is awesome!"),
     record(a = 3.14)
| fieldsAdd type(a), asArray(a)

```

Query result:

| a |
| --- |
| type(a) |
| asArray(a) |
| `[2, 3, 7, 7, 1]` |
| `array` |
| `[2, 3, 7, 7, 1]` |
| `DQL is awesome!` |
| `string` |
| *null* |
| `3.14` |
| `double` |
| *null* |

## asBinary

Returns binary value (byte array) if the value is `binary`, otherwise, returns `null`.

#### Syntax

`asBinary(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | binary |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `binary`.

#### Examples

##### Example 1

```
data record(a = 3.14),
     record(a = "dynatrace"),
     record(a = true),
     record(a = decodeBase64ToBinary("ZHluYXRyYWNl"))
| fieldsAdd type(a), asBinary(a)

```

Query result:

| a |
| --- |
| type(a) |
| asBinary(a) |
| `3.14` |
| `double` |
| *null* |
| `dynatrace` |
| `string` |
| *null* |
| `true` |
| `boolean` |
| *null* |
| `ZHluYXRyYWNl` |
| `binary` |
| `ZHluYXRyYWNl` |

## asBoolean

Returns boolean value if the value is `boolean`, otherwise, returns `null`.

#### Syntax

`asBoolean(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | boolean |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = true),
     record(a = "true"),
     record(a = 1)
| fieldsAdd type(a), asBoolean(a)

```

Query result:

| a |  | type(a) |  | asBoolean(a) |  | `true` |  | `boolean` |  | `true` |  | `true` |  | `string` |  | *null* |  | `1` |  | `long` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## asDouble

Returns `double` value if the value is `double`, otherwise, returns `null`.

#### Syntax

`asDouble(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | double |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(a = 3),
     record(a = 3.14),
     record(a = "3.14")
| fieldsAdd type(a), asDouble(a)

```

Query result:

| a |  | type(a) |  | asDouble(a) |  | `3` |  | `long` |  | *null* |  | `3.14` |  | `double` |  | `3.14` |  | `3.14` |  | `string` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## asDuration

Returns duration value if the value is `duration`, otherwise, returns `null`.

#### Syntax

`asDuration(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | duration |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `duration`.

#### Examples

##### Example 1

```
data record(a = 15s),
     record(a = 3.14),
     record(a = timeframe(from: "2019-08-01T09:30:00.000-0400", to: "2019-08-01T16:00:00.000-0400")),
     record(a = "42"),
     record(a = "42s")
| fieldsAdd type(a), asDuration(a)

```

Query result:

| a |
| --- |
| type(a) |
| asDuration(a) |
| `15 s` |
| `duration` |
| `15 s` |
| `3.14` |
| `double` |
| *null* |
| **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T20:00:00.000Z` |
| `timeframe` |
| *null* |
| `42` |
| `string` |
| *null* |
| `42s` |
| `string` |
| *null* |

## asIp

You can use this function to cast to an IP address.

#### Syntax

`asIp(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string expression, ip address |  | The expression to cast an expression to an IP address. |  |  |

#### Returns

The data type of the returned value is `ip`.

#### Examples

##### Example 1

```
data record(a = ip("127.0.0.1")),
     record(a = "10.0.0.1")
| fieldsAdd type(a), asIp(a)

```

Query result:

| a |  | type(a) |  | asIp(a) |
| --- | --- | --- | --- | --- |
| `127.0.0.1` |  | `ip` |  | `127.0.0.1` |
| `10.0.0.1` |  | `string` |  | *null* |

## asLong

Returns `long` value if the value is `long`, otherwise `null`.

#### Syntax

`asLong(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | long |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 3),
     record(a = 3.14),
     record(a = "3")
| fieldsAdd type(a), asLong(a)

```

Query result:

| a |  | type(a) |  | asLong(a) |  | `3` |  | `long` |  | `3` |  | `3.14` |  | `double` |  | *null* |  | `3` |  | `string` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## asNumber

Returns the same value if the value is `integer`, `long`, `double`, otherwise, returns `null`.

#### Syntax

`asNumber(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | double, long |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `double` or `long`.

#### Examples

##### Example 1

```
data record(a = 3),
     record(a = 3.14),
     record(a = "3.14")
| fieldsAdd type(a), asNumber(a)

```

Query result:

| a |  | type(a) |  | asNumber(a) |  | `3` |  | `long` |  | `3` |  | `3.14` |  | `double` |  | `3.14` |  | `3.14` |  | `string` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## asRecord

Returns record value if the value is `record`, otherwise, returns `null`.

#### Syntax

`asRecord(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | record |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `record`.

#### Examples

##### Example 1

```
data record(a = record(b = 3)),
     record(a = 3.14),
     record(a = "3"),
     record(a = array(2, 3, 7, 7, 1))
| fieldsAdd type(a), asRecord(a)

```

Query result:

| a |
| --- |
| type(a) |
| asRecord(a) |
| **b**: `3` |
| `record` |
| **b**: `3` |
| `3.14` |
| `double` |
| *null* |
| `3` |
| `string` |
| *null* |
| `[2, 3, 7, 7, 1]` |
| `array` |
| *null* |

## asString

Returns string value if the value is `string`, otherwise, returns `null`.

#### Syntax

`asString(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | string |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(a = array(1, 2, 3)),
     record(a = 3.14),
     record(a = "DQL is awesome!"),
     record(a = record(content = "A nested record"))
| fieldsAdd type(a), asString(a)

```

Query result:

| a |
| --- |
| type(a) |
| asString(a) |
| `[1, 2, 3]` |
| `array` |
| *null* |
| `3.14` |
| `double` |
| *null* |
| `DQL is awesome!` |
| `string` |
| `DQL is awesome!` |
| **content**: `A nested record` |
| `record` |
| *null* |

## asTimeframe

Returns `timeframe` value if the value is `timeframe`, otherwise returns `null`.

#### Syntax

`asTimeframe(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | timeframe |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `timeframe`.

#### Examples

##### Example 1

```
data record(timeframe = timeframe(from: "2019-08-01T09:30:00.000-0400", to: "2019-08-01T16:00:00.000-0400")),
     record(timeframe = timeframe(from: - 24h, to: - 2h)),
     record(timeframe = "2019-08-01T15:30:00.000-0400/2019-08-01T22:00:00.000-0400")
| fieldsAdd type(timeframe), asTimeframe(timeframe)

```

Query result:

| timeframe |  | type(timeframe) |  | asTimeframe(timeframe) |  | **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T20:00:00.000Z` |  | `timeframe` |  | **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T20:00:00.000Z` |  | **start**: `2023-11-16T10:05:42.927Z`**end**: `2023-11-17T08:05:42.927Z` |  | `timeframe` |  | **start**: `2023-11-16T10:05:42.927Z`**end**: `2023-11-17T08:05:42.927Z` |  | `2019-08-01T15:30:00.000-0400/2019-08-01T22:00:00.000-0400` |  | `string` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## asTimestamp

Returns `timestamp` value if the value is `timestamp`, otherwise, returns `null`.

Alternatively use the [toTimestamp](#toTimestamp) function to convert a `long`, `double` or `string` value to a value of type `timestamp`.

#### Syntax

`asTimestamp(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | timestamp |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

##### Example 1

```
data record(timestamp = timestamp(2019, 8, 1, 13, 30, 0)),
     record(timestamp = 1564666200000000000),
     record(timestamp = "2019-08-01T09:30:00.000-0400")
| fieldsAdd type(timestamp), asTimestamp(timestamp)

```

Query result:

| timestamp |  | type(timestamp) |  | asTimestamp(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `timestamp` |  | `2019-08-01T13:30:00.000Z` |  | `1,564,666,200,000,000,000` |  | `long` |  | *null* |  | `2019-08-01T09:30:00.000-0400` |  | `string` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## asUid

Returns a `uid` value if the value is `uid`, otherwise returns `null`.

#### Syntax

`asUid(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | uid |  | The value to cast. |  |  |

#### Returns

The data type of the returned value is `uid`.

#### Examples

##### Example 1

```
data record(a = uid64(123)), record(a = 123)
| fields asUid(a)

```

Query result:

| asUid(a) |  | asUid(a) |  | `000000000000007b` |  | `null` |
| --- | --- | --- | --- | --- | --- | --- |

## decode

The decode function allows encoding binary data and strings into a string representation, and the opposite way. There are two types of decode functions, BASE64 and BASE16.

#### Syntax

`decodeBase64ToBinary(expression)`

`decodeBase64ToString(expression)`

`decodeBase16ToBinary(expression)`

`decodeBase16ToString(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | An encoded string that needs to be decoded to a plain string or binary. Retrieves `null` if the encoding format does not match the outcome format. |  |  |

#### Returns

The data type of the returned value is `binary` or `string`.

#### Examples

##### Example 1

```
data record(content = "RFFMIGlzIGF3ZXNvbWUh"),
     record(content = "RHluYXRyYWNlIFF1ZXJ5IExhbmd1YWdl")
| fieldsAdd decodeBase64ToString(content)

```

Query result:

| content |  | decodeBase64ToString(content) |  | `RFFMIGlzIGF3ZXNvbWUh` |  | `DQL is awesome!` |  | `RHluYXRyYWNlIFF1ZXJ5IExhbmd1YWdl` |  | `Dynatrace Query Language` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

```
data record(content = "44514c20697320617765736f6d6521"),
       record(content = "44796e617472616365205175657279204c616e6775616765")
| fieldsAdd decodeBase16ToString(content)

```

Query result:

| content |  | decodeBase16ToString(content) |  | `44514c20697320617765736f6d6521` |  | `DQL is awesome!` |  | `44796e617472616365205175657279204c616e6775616765` |  | `Dynatrace Query Language` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## encode

The encode function allows encoding binary data and strings into a string representation, and the opposite way. There are two types of encode functions, BASE64 and BASE16.

#### Syntax

`encodeBase64(expression)`

`encodeBase16(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, binary |  | A string or binary expression to encode. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd encodeBase16(content),
            encodeBase64(content)

```

Query result:

| content |  | encodeBase16(content) |  | encodeBase64(content) |  | `DQL is awesome!` |  | `44514c20697320617765736f6d6521` |  | `RFFMIGlzIGF3ZXNvbWUh` |  | `Dynatrace Query Language` |  | `44796e617472616365205175657279204c616e6775616765` |  | `RHluYXRyYWNlIFF1ZXJ5IExhbmd1YWdl` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## getHighBits

Extracts the most significant bits of an expression. It accepts `uid` or `ip` expression types. For all other types, it returns `null`.

#### Syntax

`getHighBits(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | uid, ip address |  | The expression from which the most significant bits should be extracted. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = uid64(123)),
     record(a = uid128(123, 456)),
     record(a = uuid(123, 456)),
	   record(a = ip("127.0.0.1")),
	   record(a = ip("192.168.0.1")),
     record(a = ip("2001:0db8:0000:0000:0000:8a2e:0370:7334")),
     record(a = ip("::1")),
	   record(a = 1),
	   record(a = true),
	   record(a = "foo")
| fields a, getHighBits(a)

```

Query result:

| a |  | getHighBits(a) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `000000000000007b` |  | `0` |  | `000000000000007b00000000000001c8` |  | `123` |  | `00000000-0000-007b-0000-0000000001c8` |  | `123` |  | `127.0.0.1` |  | `0` |  | `192.168.0.1` |  | `0` |  | `2001:0db8::8a2e:0370:7334` |  | `2306139568115548160` |  | `::0001` |  | `0` |  | `1` |  | ***null*** |  | `true` |  | ***null*** |  | `foo` |  | ***null*** |

## getLowBits

Extracts the least significant bits of an expression. It accepts `uid` or `ip` expression types. For all other types, it returns `null`.

#### Syntax

`getLowBits(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | uid, ip address |  | The expression from which to extract the least significant bits. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = uid64(123)),
     record(a = uid128(123, 456)),
     record(a = uuid(123, 456)),
	   record(a = ip("127.0.0.1")),
	   record(a = ip("192.168.0.1")),
     record(a = ip("2001:0db8:0000:0000:0000:8a2e:0370:7334")),
     record(a = ip("::1")),
	   record(a = 1),
	   record(a = true),
	   record(a = "foo")
| fields a, getLowBits(a)

```

Query result:

| a |  | getLowBits(a) |  | `000000000000007b` |  | `123` |  | `000000000000007b00000000000001c8` |  | `456` |  | `00000000-0000-007b-0000-0000000001c8` |  | `456` |  | `127.0.0.1` |  | `2130706433` |  | `192.168.0.1` |  | `-1062731775` |  | `2001:0db8::8a2e:0370:7334` |  | `151930230829876` |  | `::0001` |  | `1` |  | `1` |  | ***null*** |  | `true` |  | ***null*** |  | `foo` |  | ***null*** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## hexStringToNumber

Converts a hexadecimal string to a number.

#### Syntax

`hexStringToNumber(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string expression |  | The string expression that will be converted to a number. |  |  |

#### Returns

The data type of the returned value is `double` or `long`.

#### Examples

##### Example 1

```
data record(a = "0x7f"),
     record(a = "100"),
     record(a = "0X80000000")
| fieldsAdd hexStringToNumber(a)

```

Query result:

| a |  | hexStringToNumber(a) |  | `0x7f` |  | `127` |  | `100` |  | `256` |  | `0X80000000` |  | `2,147,483,648` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## isUid128

Tests if a `uid` value is of subtype `uid128`.

#### Syntax

`isUid128(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | uid |  | The uid expression that will be checked if it is of subtype uid128. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = uid64(123)),
     record(a = toUid("000000000000007c")),
     record(a = uid128(123, 456)),
     record(a = toUid("000000000000007c00000000000001c8")),
     record(a = uuid(123, 456)),
     record(a = toUid("00000000-0000-007c-0000-0000000001c8"))
| fieldsAdd isUid128(a)

```

Query result:

| a |  | isUid128(a) |  | `000000000000007b` |  | `false` |  | `000000000000007c` |  | `false` |  | `000000000000007b00000000000001c8` |  | `true` |  | `000000000000007c00000000000001c8` |  | `true` |  | `00000000-0000-007b-0000-0000000001c8` |  | `false` |  | `00000000-0000-007c-0000-0000000001c8` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## isUid64

Tests if a `uid` value is of subtype `uid64`.

#### Syntax

`isUid64(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | uid |  | The uid expression that will be checked if it is of subtype uid64. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = uid64(123)),
     record(a = toUid("000000000000007c")),
     record(a = uid128(123, 456)),
     record(a = toUid("000000000000007c00000000000001c8")),
     record(a = uuid(123, 456)),
     record(a = toUid("00000000-0000-007c-0000-0000000001c8"))
| fieldsAdd isUid64(a)

```

Query result:

| a |  | isUid64(a) |  | `000000000000007b` |  | `true` |  | `000000000000007c` |  | `true` |  | `000000000000007b00000000000001c8` |  | `false` |  | `000000000000007c00000000000001c8` |  | `false` |  | `00000000-0000-007b-0000-0000000001c8` |  | `false` |  | `00000000-0000-007c-0000-0000000001c8` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## isUuid

Tests if a `uid` value is of subtype `uuid`.

#### Syntax

`isUuid(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | uid |  | The uid expression that will be checked if it is of subtype uuid. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = uid64(123)),
     record(a = toUid("000000000000007c")),
     record(a = uid128(123, 456)),
     record(a = toUid("000000000000007c00000000000001c8")),
     record(a = uuid(123, 456)),
     record(a = toUid("00000000-0000-007c-0000-0000000001c8"))
| fieldsAdd isUuid(a)

```

Query result:

| a |  | isUuid(a) |  | `000000000000007b` |  | `false` |  | `000000000000007c` |  | `false` |  | `000000000000007b00000000000001c8` |  | `false` |  | `000000000000007c00000000000001c8` |  | `false` |  | `00000000-0000-007b-0000-0000000001c8` |  | `true` |  | `00000000-0000-007c-0000-0000000001c8` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## numberToHexString

Converts a number to a hexadecimal string.

#### Syntax

`numberToHexString(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | numeric expression |  | The numeric expression that will be converted to a hexadecimal string. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(a = 127),
     record(a = 256),
     record(a = 2147483648)
| fieldsAdd numberToHexString(a)

```

Query result:

| a |  | numberToHexString(a) |  | `127` |  | `7f` |  | `256` |  | `100` |  | `2,147,483,648` |  | `80000000` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## toArray

Returns the value if it is an `array`. Otherwise, converts a value to the single element array holding that value.

#### Syntax

`toArray(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(a = array(2, 3, 7, 7, 1)),
     record(a = "DQL is awesome!"),
     record(a = 3.14)
| fieldsAdd type(a), toArray(a)

```

Query result:

| a |  | type(a) |  | toArray(a) |  | `[2, 3, 7, 7, 1]` |  | `array` |  | `[2, 3, 7, 7, 1]` |  | `DQL is awesome!` |  | `string` |  | `[DQL is awesome!]` |  | `3.14` |  | `double` |  | `[3.14]` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## toBoolean

Converts a value to Boolean if the value is of a suitable type. If the argument is an array, the element at position 0 is converted.

Use [`asBoolean(value)`](/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asBoolean) function to return if the value is `boolean` or `variant<boolean>`, otherwise `null`.

Converts string values `true` or `TRUE` to a Boolean `true`.The comparison is case insensitive. Converts other values to Boolean `false`. Converts numeric value 0 to Boolean `false`. Converts other numeric values to Boolean `true`.

#### Syntax

`toBoolean(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | boolean, double, long, string, array |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = true),
     record(a = "true"),
     record(a = "yes"),
     record(a = 0),
     record(a = 1),
     record(a = 2)
| fieldsAdd type(a), toBoolean(a)

```

Query result:

| a |  | type(a) |  | toBoolean(a) |  | `true` |  | `boolean` |  | `true` |  | `true` |  | `string` |  | `true` |  | `yes` |  | `string` |  | *null* |  | `0` |  | `long` |  | `false` |  | `1` |  | `long` |  | `true` |  | `2` |  | `long` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

You can use iterative expressions to convert all elements of an array.

```
data record(a = array(true, "false", null, 0, 1, -0.5, -1))
| fieldsAdd toBoolean(a[])

```

Query result:

| a |  | toBoolean(a[]) |  | `[true, "false", null, 0, 1, -0.5, -1]` |  | `[true, false, null, false, true, false, true]` |
| --- | --- | --- | --- | --- | --- | --- |

## toDouble

Converts a value to `double` if the value is of a suitable type. If the argument is an `array`, the element at position 0 is converted.

Use [`asDouble(value)`](/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asDouble) function to return if the value is `double` or `variant<double>`, otherwise `null`.

#### Syntax

`toDouble(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | double, long, string, boolean, ip, timestamp, duration, array |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `double`.

#### Examples

##### Example 1

```
data record(a = 3),
     record(a = 3.14),
     record(a = "3.14"),
     record(a = true),
     record(a = toTimestamp("2019-08-01T09:30:00.000-0400")),
     record(a = 15s),
     record(a = ip("10.0.0.1"))
| fieldsAdd type(a), toDouble(a)

```

Query result:

| a |  | type(a) |  | toDouble(a) |  | `3` |  | `long` |  | `3` |  | `3.14` |  | `double` |  | `3.14` |  | `3.14` |  | `string` |  | `3.14` |  | `true` |  | `boolean` |  | `1` |  | `2019-08-01T13:30:00.000Z` |  | `timestamp` |  | `1,564,666,200,000,000,000` |  | `15 s` |  | `duration` |  | `15,000,000,000` |  | `10.0.0.1` |  | `ip` |  | `167,772,161` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

You can use iterative expressions to convert all elements of an array.

```
data record(a = array("0.85", -1.5, 3, "1A3", false, "false", true, "true", 1.6e-3))
| fieldsAdd toDouble(a[])

```

Query result:

| a |  | toDouble(a[]) |  | `["0.85", -1.5, 3, "1A3", false, "false", true, "true", 0.0016]` |  | `[0.85, -1.5, 3, null, 0, null, 1, null, 0.0016]` |
| --- | --- | --- | --- | --- | --- | --- |

## toDuration

Converts a value to `duration` if the value is of a suitable type. If the argument is an `array`, the element at position 0 is converted.

#### Syntax

`toDuration(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | duration, double, long, string, timeframe, array |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `duration`.

#### Examples

##### Example 1

```
data record(a = 15s),
     record(a = 3.14),
     record(a = timeframe(from: "2019-08-01T09:30:00.000-0400", to: "2019-08-01T16:00:00.000-0400")),
     record(a = "42"),
     record(a = "42s")
| fieldsAdd type(a), toDuration(a)

```

Query result:

| a |  | type(a) |  | toDuration(a) |  | `15 s` |  | `duration` |  | `15 s` |  | `3.14` |  | `double` |  | `3 ns` |  | **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T20:00:00.000Z` |  | `timeframe` |  | `6.5 h` |  | `42` |  | `string` |  | `42 ns` |  | `42s` |  | `string` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

You can use iterative expressions to convert all elements of an array.

```
data record(a = array(15s, 3.14, "42"))
| fieldsAdd toDuration(a[])

```

Query result:

| a |  | toDuration(a[]) |  | `[15s, 3.14, "42"]` |  | `[15s, 3ns, 42ns]` |
| --- | --- | --- | --- | --- | --- | --- |

## toIp

You can use this function to convert an expression to an IP address.

#### Syntax

`toIp(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string expression, ip address |  | The expression to convert an expression to an IP address. |  |  |

#### Returns

The data type of the returned value is `ip`.

#### Examples

##### Example 1

```
data record(a = ip("127.0.0.1")),
     record(a = "10.0.0.1"),
     record(a = "300.0.0.1"),
     record(a = 1234567890)
| fieldsAdd type(a), toIp(a)

```

Query result:

| a |  | type(a) |  | toIp(a) |  | `127.0.0.1` |  | `ip` |  | `127.0.0.1` |  | `10.0.0.1` |  | `string` |  | `10.0.0.1` |  | `300.0.0.1` |  | `string` |  | *null* |  | `1,234,567,890` |  | `long` |  | `73.150.2.210` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

You can use iterative expressions to convert all elements of an array.

```
data record(a = array("127.0.0.1", "10.0.0.1", "192.168.0.1"))
| fieldsAdd toIp(a[])

```

Query result:

| a |  | toIp(a[]) |  | `["127.0.0.1", "10.0.0.1", "192.168.0.1"]` |  | `[127.0.0.1, 10.0.0.1, 192.168.0.1]` |
| --- | --- | --- | --- | --- | --- | --- |

## toLong

Converts a value to `long` if the value is of a suitable type. If the argument is an `array`, the element at position 0 is converted.

#### Syntax

`toLong(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | long, double, string, boolean, ip, timestamp, duration, array |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = 3),
     record(a = 3.14),
     record(a = "3"),
     record(a = true),
     record(a = false),
     record(a = ip("10.0.0.1")),
     record(a = 15s),
     record(a = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd type(a), toLong(a)

```

Query result:

| a |  | type(a) |  | toLong(a) |  | `3` |  | `long` |  | `3` |  | `3.14` |  | `double` |  | `3` |  | `3` |  | `string` |  | `3` |  | `true` |  | `boolean` |  | `1` |  | `false` |  | `boolean` |  | `0` |  | `10.0.0.1` |  | `ip` |  | `167,772,161` |  | `15 s` |  | `duration` |  | `15,000,000,000` |  | `2019-08-01T13:30:00.000Z` |  | `timestamp` |  | `1,564,666,200,000,000,000` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

You can use iterative expressions to convert all elements of an array.

```
data record(a = array(3, 3.14, "3", true, false))
| fieldsAdd toLong(a[])

```

Query result:

| a |  | toLong(a[]) |  | `[3, 3.14, "3", true, false]` |  | `[3, 3, 3, 1, 0]` |
| --- | --- | --- | --- | --- | --- | --- |

## toString

Returns the string representation of a value.

#### Syntax

`toString(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | double, boolean, timestamp, timeframe, duration, ip, array, record |  | Parameter that should be transformed into text form. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(a = array(1, 2, 3)),
     record(a = true),
     record(a = 3),
     record(a = 3.14),
     record(a = 5m),
     record(a = toIp("127.0.0.1")),
     record(a = "DQL is awesome!"),
     record(a = timeframe(from: now() - 5m, to: now())),
     record(a = toTimestamp("2019-08-01T09:30:00.000-0400")),
     record(a = record(content = "A nested record"))
| fieldsAdd type(a), toString(a)

```

Query result:

| a |  | type(a) |  | toString(a) |  | `[1, 2, 3]` |  | `array` |  | `[1, 2, 3]` |  | `true` |  | `boolean` |  | `true` |  | `3` |  | `long` |  | `3` |  | `3.14` |  | `double` |  | `3.14` |  | `5 min` |  | `duration` |  | `"05:00.000000000"` |  | `127.0.0.1` |  | `ip` |  | `"127.0.0.1"` |  | `DQL is awesome!` |  | `string` |  | `DQL is awesome!` |  | **start**: `2023-11-17T10:00:43.724Z`**end**: `2023-11-17T10:05:43.724Z` |  | `timeframe` |  | `"2023-11-17T10:00:43.724031180 +0000/2023-11-17T10:05:43.724031180 +0000"` |  | `2019-08-01T13:30:00.000Z` |  | `timestamp` |  | `"2019-08-01T13:30:00.000000000 +0000"` |  | **content**: `A nested record` |  | `record` |  | `{"content":"A nested record"}` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## toTimeframe

Converts a value to `timeframe` if the value is of a suitable type. If the argument is an `array`, the element at position 0 is converted.

#### Syntax

`toTimeframe(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | timeframe, string, array |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `timeframe`.

#### Examples

##### Example 1

```
data record(timeframe = timeframe(from: "2019-08-01T09:30:00.000-0400", to: "2019-08-01T16:00:00.000-0400")),
     record(timeframe = timeframe(from: - 24h, to: - 2h)),
     record(timeframe = "2019-08-01T09:30:00.000-0400/2019-08-01T16:00:00.000-0400")
| fieldsAdd type(timeframe), toTimeframe(timeframe)

```

Query result:

| timeframe |  | type(timeframe) |  | toTimeframe(timeframe) |  | **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T20:00:00.000Z` |  | `timeframe` |  | **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T20:00:00.000Z` |  | **start**: `2023-11-16T10:05:43.784Z`**end**: `2023-11-17T08:05:43.784Z` |  | `timeframe` |  | **start**: `2023-11-16T10:05:43.784Z`**end**: `2023-11-17T08:05:43.784Z` |  | `2019-08-01T09:30:00.000-0400/2019-08-01T16:00:00.000-0400` |  | `string` |  | **start**: `2019-08-01T13:30:00.000Z`**end**: `2019-08-01T20:00:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

You can use iterative expressions to convert all elements of an array.

```
data record(a = array("2019-08-01T09:30:00.000-0400/2019-08-01T16:00:00.000-0400",
                      "2019-08-01T15:30:00.000-0400/2019-08-01T22:00:00.000-0400"))
| fieldsAdd toTimeframe(a[])

```

Query result:

| a |  | toTimeframe(a[]) |  | `["2019-08-01T09:30:00.000-0400/2019-08-01T16:00:00.000-0400", "2019-08-01T15:30:00.000-0400/2019-08-01T22:00:00.000-0400"]` |  | [**start**:`2019-08-01T13:30:00.000Z` **end**:`2019-08-01T20:00:00.000Z`, **start**:`2019-08-01T19:30:00.000Z` **end**:`2019-08-02T02:00:00.000Z`] |
| --- | --- | --- | --- | --- | --- | --- |

## toTimestamp

Converts a value to `timestamp` if the value is of a suitable type. If the argument is an ARRAY, the element at position 0 is converted.

Use [`asTimestamp(<value>)`](/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asTimestamp) function to return if the value is `timestamp` or `variant<timestamp>`, otherwise `null`.

#### Syntax

`toTimestamp(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | timestamp, double, long , string, array |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400")),
     record(timestamp = 1564666200000000000),
     record(timestamp = "2019-08-01T09:30:00.000-0400")
| fieldsAdd type(timestamp), toTimestamp(timestamp)

```

Query result:

| timestamp |  | type(timestamp) |  | toTimestamp(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `timestamp` |  | `2019-08-01T13:30:00.000Z` |  | `1,564,666,200,000,000,000` |  | `long` |  | `2019-08-01T13:30:00.000Z` |  | `2019-08-01T09:30:00.000-0400` |  | `string` |  | `2019-08-01T13:30:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

You can use iterative expressions to convert all elements of an array.

```
data record(a = array(toTimestamp("2019-08-01T09:30:00.000-0400"),
                                              1564666200000000000,
                                  "2019-08-01T09:30:00.000-0400"))
| fieldsAdd toTimestamp(a[])

```

Query result:

| a |  | toTimestamp(a[]) |  | `[2019-08-01T13:30:00.000Z, 1564666200000000000, "2019-08-01T09:30:00.000-0400"]` |  | `[2019-08-01T13:30:00.000Z, 2019-08-01T13:30:00.000Z, 2019-08-01T13:30:00.000Z]` |
| --- | --- | --- | --- | --- | --- | --- |

## toUid

Converts a value to `uid` if the value is of a suitable type.

#### Syntax

`toUid(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | number, string, uid, array |  | Any convertible value. If the argument is an `array`, the element at position 0 is converted. |  |  |

#### Returns

The data type of the returned value is `uid`.

#### Examples

##### Example 1

```
data record(a = "550e8400-e29b-41d4-a716-446655440000", b = 123, c = uid64(456), d=array(123))
| fields toUid(a), toUid(b), toUid(c), toUid(d)

```

Query result:

| toUid(a) |  | toUid(b) |  | toUid(c) |  | toUid(d) |  | `550e8400-e29b-41d4-a716-446655440000` |  | `000000000000007bt` |  | `00000000000001c8` |  | `000000000000007b` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

You can use iterative expressions to convert all elements of an array.

```
data record(a = array("550e8400-e29b-41d4-a716-446655440000", "000000000000007c"))
| fieldsAdd toUid(a[])

```

| a |  | toUid(a[]) |  | `["550e8400-e29b-41d4-a716-446655440000", "000000000000007c"]` |  | `[550e8400-e29b-41d4-a716-446655440000, 000000000000007c]` |
| --- | --- | --- | --- | --- | --- | --- |

## type

Returns the type of a value as a `string`.

#### Syntax

`type(expression [, withSubtype])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  |  |  |  |
|  |  |  |  |  |  |  |
| withSubtype |  | boolean |  |  |  |  |
| Whether the subtype information should be included. |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(a = array(1, 2, 3)),
     record(a = true),
     record(a = 3),
     record(a = 3.14),
     record(a = 5m),
     record(a = toIp("127.0.0.1")),
     record(a = toIp("2001:0db8:0000:0000:0000:8a2e:0370:7334")),
     record(a = "DQL is awesome!"),
     record(a = timeframe(from: now() - 5m, to: now())),
     record(a = toTimestamp("2019-08-01T09:30:00.000-0400")),
     record(a = record(content = "A nested record")),
     record(a = uid64(123)),
     record(a = uid128(123, 456)),
     record(a = uuid(123, 456))
| fieldsAdd type(a), type(a, withSubtype:true)

```

Query result:

| a |  | type(a) |  | type(a, withSubtype:TRUE) |  | `[1, 2, 3]` |  | `array` |  | `array` |  | `true` |  | `boolean` |  | `boolean` |  | `3` |  | `long` |  | `long` |  | `3.14` |  | `double` |  | `double` |  | `5 min` |  | `duration` |  | `duration` |  | `127.0.0.1` |  | `ip` |  | `ip/ipv4` |  | `2001:0db8::8a2e:0370:7334` |  | `ip` |  | `ip/ipv6` |  | `DQL is awesome!` |  | `string` |  | `string` |  | **start**: `2025-01-10T10:31:17.840Z` **end**: `2025-01-10T10:36:17.840Z` |  | `timeframe` |  | `timeframe` |  | `2019-08-01T13:30:00.000Z` |  | `timestamp` |  | `timestamp` |  | **content**: `A nested record` |  | `record` |  | `record` |  | `000000000000007b` |  | `uid` |  | `uid/uid64` |  | `000000000000007b00000000000001c8` |  | `uid` |  | `uid/uid128` |  | `00000000-0000-007b-0000-0000000001c8` |  | `uid` |  | `uid/uuid` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## uid128

Creates a `uid` of subtype `uid128` from two `long` expressions.

#### Syntax

`uid128(mostSignificantBits, leastSignificantBits)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| mostSignificantBits |  | long |  | The first `long` expression for the most significant bits of a `uid128`. |  |  |
| leastSignificantBits |  | long |  | The second `long` expression for the least significant bits of a `uid128`. |  |  |

#### Returns

The data type of the returned value is `uid`.

#### Examples

##### Example 1

```
data record(a = 123, b = 456)
| fields uid128(a, b)

```

Query result:

| uid128(a, b) |  | `000000000000007b00000000000001c8` |
| --- | --- | --- |

## uid64

Creates a `uid` of subtype `uid64` from a `long` expression.

#### Syntax

`uid64(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | long |  | The `long` expression for a `uid64`. |  |  |

#### Returns

The data type of the returned value is `uid`.

#### Examples

##### Example 1

```
data record(a = 123)
| fields uid64(a)

```

Query result:

| uid64(a) |  | `000000000000007b` |
| --- | --- | --- |

## uuid

Creates a `uid` of subtype `uuid` from two `long` expressions.

#### Syntax

`uuid(mostSignificantBits, leastSignificantBits)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| mostSignificantBits |  | long |  | The first `long` expression for the most significant bits of a `uuid`. |  |  |
| leastSignificantBits |  | long |  | The second `long` expression for the least significant bits of a `uuid`. |  |  |

#### Returns

The data type of the returned value is `uid`.

#### Examples

##### Example 1

```
data record(a = 123, b = 456)
| fields uuid(a, b)

```

Query result:

| uuid(a, b) |  | `00000000-0000-007b-0000-0000000001c8` |
| --- | --- | --- |

## smartscapeId

Creates a smartscapeId from the given string and long expression.

#### Syntax

`smartscapeId(type, numericId)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| type |  | string |  | The type of smartscapeId as `string`. |  |  |
| numericId |  | long |  | The numeric id of smartscapeId as `long`. |  |  |

#### Returns

The data type of the returned value is `smartscapeId`.

#### Examples

##### Example 1

```
data record(a = "HOST", b = 123)
| fields smartscapeId(a, b)

```

Query result:

| smartscapeId(a, b) |  | `HOST-000000000000007B` |
| --- | --- | --- |

## asSmartscapeId

Returns smartscapeId value if the value is `smartscapeId`, otherwise returns `null`.

#### Syntax

`asSmartscapeId(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | string, smartscapeID |  | The expression to cast as a smartscapeId. |  |  |

#### Returns

The data type of the returned value can be `smartscapeId` or `null`.

#### Examples

##### Example 1

```
data record(a = "SERVICE-00590715D82398FE"),
     record(a = toSmartscapeId("SERVICE-00590715D82398FE")),
     record(a = 1)
| fieldsAdd type(a), asSmartscapeId(a)

```

Query result:

| a |  | type(a) |  | asSmartscapeId(a) |  | `SERVICE-00590715D82398FE` |  | `string` |  | *null* |  | `SERVICE-00590715D82398FE` |  | `smartscape_id` |  | `SERVICE-00590715D82398FE` |  | `1` |  | `long` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## toSmartscapeId

Converts a value to `smartscapeId` if the value is of a suitable type. If the argument is an `array`, only the element at position 0 is converted.

#### Syntax

`toSmartscapeId(value)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| value |  | string, array |  | The expression to convert to a `smartscapeId` if possible. |  |  |

#### Returns

The data type of the returned value is `smartscapeId`.

#### Examples

##### Example 1

```
data record(a = "SERVICE-02E04D7E459555EC", b = array("DISK-000392498B505BD0"))
| fields toSmartscapeId(a), toSmartscapeId(b)

```

Query result:

| toSmartscapeId(a) |  | toSmartscapeId(b) |  | `SERVICE-02E04D7E459555EC` |  | `DISK-000392498B505BD0` |
| --- | --- | --- | --- | --- | --- | --- |
