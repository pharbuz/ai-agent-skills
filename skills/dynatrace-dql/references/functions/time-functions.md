> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/time-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/time-functions)

# Time functions

Time functions return the decimal number for a particular time value, calculate the number of time units (days, months, years) between two dates, and allow to determine timestamps and timeframes, among others.

## duration

Creates a `duration` from the given amount and time unit.

#### Syntax

`duration(value, unit)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | value |  | long, double |  | The numeric value for the duration. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| unit |  | string |  | The time unit of the duration. |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `duration`.

#### Examples

##### Example 1

```
data record(value = 1000, unit = "ns"),
     record(value = 60, unit = "s"),
     record(value = 1000 * 60 * 60 * 24, unit = "ms"),
     record(value = 24, unit = "h")
| fieldsAdd duration(value, unit)

```

Query result:

| value |  | unit |  | duration(value, unit) |  | `1,000` |  | `ns` |  | `1 µs` |  | `60` |  | `s` |  | `1 min` |  | `86,400,000` |  | `ms` |  | `1 D` |  | `24` |  | `h` |  | `1 D` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## formatTimestamp

Formats the timestamp according to a format string (using the defined interval).

Timestamps according to the ISO 8601 standard can be parsed and converted to the timestamp datatype.

All letters `A` to `Z` and `a` to `z` are reserved as pattern letters.
Any non-letter characters, other than `[`, `]`, `{`, `}`, `#` and the single quote will be output directly. However, it is recommended to use single quotes around all characters that you want to output directly to ensure that future changes do not affect your query. Unrecognized pattern letters result in an error. See [Java DateTime Formatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) for the list of supported patterns and symbols.

#### Syntax

`formatTimestamp(timestamp [, interval] [, format] [, timezone] [, locale])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The timestamp expression that should be formatted. |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| interval |  | duration |  | The duration expression used to align the timestamp. The value must be constant. |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| format |  | string |  | The formatting pattern. The value must be constant. The default value is `"yyyy-mm-dd't'hh:mm:ss.sssssssss"`. |  |  |  |  |  |  |
| timezone |  | string |  | The timezone used to format the timestamp. The value must be a string literal. Timezones are based on the IANA Time Zone Database (TZDB). For details see [Java ZoneId](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html). |  |  |  |  |  |  |
| locale |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |
| The locale used to format the timestamp. The value must be a string literal. Locales use the ISO-639 language code with an optional ISO-3166 country code separated by a hyphen-minus. |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd formatted = formatTimestamp(timestamp, format:"MM-dd-yyyy"),
            year      = formatTimestamp(timestamp, format:"y"),
            month     = formatTimestamp(timestamp, format:"M"),
            week      = formatTimestamp(timestamp, format:"w"),
            dayofWeek = formatTimestamp(timestamp, format:"E", locale:"en-US"),
            hour      = formatTimestamp(timestamp, format:"H"),
            time      = formatTimestamp(timestamp, format:"HH:mm, VV"),
            timeET    = formatTimestamp(timestamp, format:"HH:mm, VV", timezone:"US/Eastern")

```

Query result:

| timestamp |
| --- |
| formatted |
| year |
| month |
| week |
| dayofWeek |
| hour |
| time |
| timeET |
| `2019-08-01T13:30:00.000Z` |
| `08-01-2019` |
| `2019` |
| `8` |
| `31` |
| `Thu` |
| `15` |
| `15:30, Europe/Berlin` |
| `09:30, US/Eastern` |

## getDayOfMonth

Extracts the day of the month from a timestamp.

#### Syntax

`getDayOfMonth(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression from which the day of the month will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| timezone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getDayOfMonth(timestamp)

```

Query result:

| timestamp |  | getDayOfMonth(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `1` |
| --- | --- | --- | --- | --- | --- | --- |

## getDayOfWeek

Extracts the day of the week from a timestamp.
The `getDayOfWeek` function always uses UTC as its timezone.
The week starts on Monday and ends on Sunday.

The numeric values represent the following days:

- `1` - Monday

- `2` - Tuesday

- `3` - Wednesday

- `4` - Thursday

- `5` - Friday

- `6` - Saturday

- `7` - Sunday

#### Syntax

`getDayOfWeek(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression from which the day of the week will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| timezone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getDayOfWeek(timestamp)

```

Query result:

| timestamp |  | getDayOfWeek(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `4` |
| --- | --- | --- | --- | --- | --- | --- |

## getDayOfYear

Extracts the day of the year from a timestamp.

#### Syntax

`getDayOfYear(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression from which the day of the year will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| timezone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getDayOfYear(timestamp)

```

Query result:

| timestamp |  | getDayOfYear(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `213` |
| --- | --- | --- | --- | --- | --- | --- |

## getEnd

Extracts the end timestamp from a timeframe.

#### Syntax

`getEnd(timeframe)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timeframe |  | timeframe |  | The timeframe expression from which the end timestamp will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

#### Example 1

```
data record(timeframe = timeframe(from:"2019-08-01T09:30:00.000-0400", to:"2019-08-01T09:35:00.000-0400"))
| fieldsAdd getEnd(timeframe)

```

Query result:

| timeframe |  | getEnd(timeframe) |  | **start:** `2019-08-01T13:30:00.000Z`**end:** `2019-08-01T13:35:00.000Z` |  | `2019-08-01T13:35:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- |

## getHour

Extracts the hour from a timestamp.

#### Syntax

`getHour(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression from which the hour will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| timezone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getHour(timestamp)

```

Query result:

| timestamp |  | getHour(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `13` |
| --- | --- | --- | --- | --- | --- | --- |

## getMinute

Extracts the minute from a timestamp.

#### Syntax

`getMinute(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp expression |  | The timestamp expression from which the minute will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| timezone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getMinute(timestamp)

```

Query result:

| timestamp |  | getMinute(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `30` |
| --- | --- | --- | --- | --- | --- | --- |

## getMonth

Extracts the month from a timestamp.

#### Syntax

`getMonth(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| timestamp |  | timestamp |  | The timestamp expression from which the month will be extracted. |  |  |
| timezone |  | string |  | The timezone that should be used. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getMonth(timestamp)

```

Query result:

| timestamp |  | getMonth(timestamp) |  | `2019-08-01T15:30:00.000Z` |  | `8` |
| --- | --- | --- | --- | --- | --- | --- |

## getStart

Extracts the start timestamp from a timeframe.

#### Syntax

`getStart(timeframe)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timeframe |  | timeframe |  | The timeframe expression from which the start timestamp will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

##### Example 1

```
data record(timeframe = timeframe(from:"2019-08-01T09:30:00.000-0400", to:"2019-08-01T09:35:00.000-0400"))
| fieldsAdd getStart(timeframe)

```

Query result:

| timeframe |  | getStart(timeframe) |  | **start:** `2019-08-01T13:30:00.000Z`**end:** `2019-08-01T13:35:00.000Z` |  | `2019-08-01T13:30:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- |

## getSecond

Extracts the second from a timestamp.

#### Syntax

`getSecond(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression from which the second will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| timezone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getSecond(timestamp)

```

Query result:

| timestamp |  | getSecond(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `0` |
| --- | --- | --- | --- | --- | --- | --- |

## getYear

Extracts the year from a timestamp.

#### Syntax

`getYear(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression from which the year will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| timezone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getYear(timestamp)

```

Query result:

| timestamp |  | getYear(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `2,019` |
| --- | --- | --- | --- | --- | --- | --- |

## getWeekOfYear

Extracts the week of the year from a timestamp.

#### Syntax

`getWeekOfYear(timestamp [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression from which the week of the year will be extracted. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| timezone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd getWeekOfYear(timestamp)

```

Query result:

| timestamp |  | getWeekOfYear(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `31` |
| --- | --- | --- | --- | --- | --- | --- |

## now

Returns the current time as a fixed timestamp of the query start.

#### Syntax

`now()`

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

##### Example 1

```
data record()
| fieldsAdd now()

```

Query result:

| now() |  | `2023-11-16T08:38:38.360Z` |
| --- | --- | --- |

## timeframe

Creates a `timeframe` structure from the given start and end timestamps.

#### Syntax

`timeframe(from [, to])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | from |  | string, timestamp, duration |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |
| to |  | duration, string, timestamp |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `timeframe`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd timeframe(from:timestamp - 5m, to: timestamp)

```

Query result:

| timestamp |  | timeframe(from:timestamp - 5m, to:timestamp) |  | `2019-08-01T13:30:00.000Z` |  | **start**: `2019-08-01T13:25:00.000Z`**end**: `2019-08-01T13:30:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- |

## timestamp

Creates a `timestamp` using provided values in mandatory parameters.

#### Syntax

`timestamp(year, month, day, hour, minute, second [, millis] [, micros] [, nanos] [, timezone])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | year |  | long |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |
| month |  | long |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| day |  | long |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| hour |  | long |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| minute |  | long |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| second |  | long |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| millis |  | long |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| micros |  | long |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| nanos |  | long |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| timezone |  |  |  |  |  |  |  |  |  |  |
| string |  |  |  |  |  |  |  |  |  |  |
| The timezone that should be used. |  |  |  |  |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

##### Example 1

```
data record()
| fieldsAdd timestamp(year:2019, month:8, day:1, hour:13, minute:30, second:0, timezone:"UTC")

```

Query result:

| timestamp(2019, 8, 1, 13, 30, 0, timezone:"UTC") |  | `2019-08-01T13:30:00.000Z` |
| --- | --- | --- |

## timestampFromUnixMillis

Creates a `timestamp` from the given milliseconds since Unix epoch.

#### Syntax

`timestampFromUnixMillis(millis)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | millis |  | long |  | Milliseconds since unix start time. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

##### Example 1

```
data record(millis = 1564666200000)
| fieldsAdd timestampFromUnixMillis(millis)

```

Query result:

| millis |  | timestampFromUnixMillis(millis) |  | `1,564,666,200,000` |  | `2019-08-01T13:30:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- |

## timestampFromUnixNanos

Creates a `timestamp` from the given nanoseconds since Unix epoch.

#### Syntax

`timestampFromUnixNanos(nanos)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | nanos |  | long |  | Nanoseconds since unix start time. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

##### Example 1

```
data record(nanos = 1564666200000000000)
| fieldsAdd timestampFromUnixNanos(nanos)

```

Query result:

| nanos |  | timestampFromUnixNanos(nanos) |  | `1,564,666,200,000,000,000` |  | `2019-08-01T13:30:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- |

## timestampFromUnixSeconds

Creates a `timestamp` from the given seconds since Unix epoch.

#### Syntax

`timestampFromUnixSeconds(seconds)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | seconds |  | long |  | Seconds since unix start time. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `timestamp`.

#### Examples

##### Example 1

```
data record(seconds = 1564666200)
| fieldsAdd timestampFromUnixSeconds(seconds)

```

Query result:

| seconds |  | timestampFromUnixSeconds(seconds) |  | `1,564,666,200` |  | `2019-08-01T13:30:00.000Z` |
| --- | --- | --- | --- | --- | --- | --- |

## unixMillisFromTimestamp

Converts a timestamp into milliseconds.

#### Syntax

`unixMillisFromTimestamp(timestamp)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression which will be converted to milliseconds since epoch. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd unixMillisFromTimestamp(timestamp)

```

Query result:

| timestamp |  | unixMillisFromTimestamp(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `1,564,666,200,000` |
| --- | --- | --- | --- | --- | --- | --- |

## unixNanosFromTimestamp

Converts a timestamp into nanoseconds.

#### Syntax

`unixNanosFromTimestamp(timestamp)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression which will be converted to nanoseconds since epoch. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd unixNanosFromTimestamp(timestamp)

```

Query result:

| timestamp |  | unixNanosFromTimestamp(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `1,564,666,200,000,000,000` |
| --- | --- | --- | --- | --- | --- | --- |

## unixSecondsFromTimestamp

Converts a timestamp into seconds.

#### Syntax

`unixSecondsFromTimestamp(timestamp)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | timestamp |  | timestamp |  | The timestamp expression which will be converted to seconds since epoch. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(timestamp = toTimestamp("2019-08-01T09:30:00.000-0400"))
| fieldsAdd unixSecondsFromTimestamp(timestamp)

```

Query result:

| timestamp |  | unixSecondsFromTimestamp(timestamp) |  | `2019-08-01T13:30:00.000Z` |  | `1,564,666,200` |
| --- | --- | --- | --- | --- | --- | --- |
