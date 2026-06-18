> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/data-types](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/data-types)

# DQL data types

The Dynatrace Query Language operates with strongly typed data: the functions and operators accept only declared types of data. The type is assigned to data during parsing or by using casting functions. DQL also recognizes value types expressed in literal notation (for example, using constant values in functions).

## Primitive types

### Boolean

Boolean has only two possible values: `true` and `false`.

-

**Literal notation**

A Boolean value can be expressed using either uppercase or lowercase letters: `true`, `TRUE`, `false`, `FALSE`

-

**Converting to Boolean**

- Converts string values `true`, `TRUE` to a `true` Boolean value, and other values to `false`.

- Converts numeric value `0` to Boolean `false`. Converts other numeric values to Boolean `true`.

```
...
| fields toBoolean("true"), toBoolean("TrUe"), toBoolean("1"), toBoolean(3), toBoolean("test"), toBoolean(0)

```

-

**Expressions**

```
boolean_expr1 AND boolean_expr2
boolean_expr1 OR boolean_expr2
boolean_expr1 XOR boolean_expr2
NOT boolean_expr

```

### Long

The signed long has a minimum value of -2^63 and a maximum value of 2^63-1.

-

**Literal notation**

LONG can be expressed in decimal or hexadecimal notation:

**decimal:** `-9223372036854775808` to `9223372036854775807`

**hexadecimal:** `0x0` to `0xFFFFFFFFFFFFFFFF`

-

**Converting to Long**

```
..
| fields toLong("83457264009472472"), toLong(30), toLong(25.34)

```

### Double

Double-precision 64-bit IEEE 754 floating point.

-

**Literal notation**

**decimal:** `2.34`
**scientific:** `2.4e2`

-

**Converting to Double**

Converts numeric values and expressions to a double value.

```
...
| fields toDouble("1234.5"), toDouble(4+3/2)

```

### Timestamp

A reference to a point in time with the precision of a nanosecond.

The primary usage for time expressions is the specification of a custom query timeframe in the DQL query string:

```
fetch logs, from:-2h, to:-20m

```

**Functions and comparison**

```
...
| fields time = toTimestamp("2022-08-01T12:00:00+01:00")
| fieldsAdd time == now(), time > now()-10d, newTime = time + 3d

```

### Timeframe

A specific time frame with a start time and an end time as timestamps with nanosecond precision.
To execute the full query result including nanoseconds, change the visualization of the data in Notebooks to raw.

```
data record(tf = timeframe(from:now()-2h, to:now()))
| fields tf, tf[start], tf[end]

```

### Duration

A duration between two timestamps, consisting of an amount and a time unit.

```
...
| fields duration = 1s

```

**Time literals**

The following time literals can be used to express durations:

- `ns`: nanoseconds

- `ms`: milliseconds

- `s`: seconds

- `m`: minutes

- `h`: hours

- `d`: days

- `w`: weeks

- `M`: months

- `q`: quarters

- `y`: years

When you use `d` in calculations, it is treated as a calendar day, otherwise it represents a duration of `24h`.

**Calendar durations**

You can use calendar durations (`d`, `w`, `M`, `q` and `y`) in calculations as shown in the example below, but not as field values.

```
fetch logs, from: now()-1M+2w

```

**Creating a duration**

In many cases, a parsed numeric value semantically represents a duration. The `duration()` function allows the creation of a field of type `duration` with the intended unit using the available time literals.

```
...
| fields     dur = 62
| fieldsAdd  dur_ms = duration(dur, unit:"ms")
| fieldsAdd  dur_ms > 50ms

```

**Converting to duration**

Converting a nanoseconds value to a `duration`:

```
...
...
| fields     dur = toDuration(62*1000000000*60*60*24)
| fieldsAdd  dur > 60d

```

Converting the period between timestamp1 and timestamp2 to a `duration`:

To illustrate, we calculate the age of the latest log message seen from a specific host.

```
...
...
fetch       logs
| filter    dt.entity.host == "HOST-DD5679D1A0C6426C"
| sort      timestamp desc
| limit     1
| fields    timestamp, age_message = now()-timestamp

```

### String

Sequence of characters with a specified character set.

- **Literal notation**

Enclose the string in double quotes. Escape double quote in the string with a backslash `\` if needed. A string can contain single quotes.

Optionally, you can enclose strings in triple quotes, such as """someString""".

- Inside triple quotes, no escaping is necessary.

- Triple quotes are not allowed as part of the string. In such a scenario, you can use the standard strings or the [concat](/platform/grail/dynatrace-query-language/functions/string-functions#concat) function.

- **Converting to String**

All DQL datatypes can be converted to a string:

```
...
| fields toString(toBoolean(1)), toString(array(1,2,3)), toString(1), toString(toTimestamp(now())), toString(toIpAddress("192.168.0.1"))

```

### IpAddress

Represents an IPv4 or IPv6 address.

### UID

A data type that is used to represent 64-bit identifiers and 128-bit identifiers.

You can use the following DQL functions to create `UID` data:

- [uid64](/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uid64)

- [uid128](/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uid128)

- [toUid](/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toUid)

## Complex types

### Array

A data structure that contains a sequence of values, each identified by index.

-

**Accessing array elements**

```
...
| fieldsAdd int_array = array(1,2,2,3,4,5)
| fields first_element = int_array[0], fifth_element = int_array[4]

```

-

**Comparing arrays**

Only the equals operator `==` can be directly used on arrays.

```
...
| ...
| fields a=array(1,2), b=array(1,2,3), c=array("a","b"), d=toArray("c,d")
| fields a == b, arraySize(b) > arraySize(c)

```

See the complete list of [DQL array functions](/platform/grail/dynatrace-query-language/functions#array-functions) for further information.

### Record

A set of key-value pair data whose value can be any DQL data type.

-

**Accessing RECORD Elements**

Data elements can be accessed by the key:

```
...
| fields person = record({name="john", age=33, address=record({city="Atlanta", pcode="30308"})})
| fields person[name], person[address][pcode]

```

-

**Converting to RECORD**

The function `record(expression,...)` converts one or more expressions returning any data type to `RECORD`:

```
...
| fields t = record(a=1+2,b=3,c=toString(timestamp))

```

Parsing JSON or key-value pair strings results in `RECORD` data.

```
STRUCTURE{matcher_expr, ...}:fieldname
JSON{matcher_expr, ...}:fieldname
KVP{matcher_expr, ...}:fieldname
$subpattern:fieldname

```

-

**Parsing Key-value pair data**

```
...
| fields str = "name=\"john\"; age=33; city=\"Atlanta\""
| parse str, "KVP{LD:key'='(LONG:valueLong | STRING:valueStr)'; '?}:person"
| fields person[name], person[age], person[city]

```

-

**Parsing JSON data**

```
...
| fields str = "{\"type\":\"update\",\"host\":\"CI_preprod_1\",\"version\":\"10.2.2367\"}"
| parse str,"JSON:event"
| fields event[type], event[host], event[version]

```
