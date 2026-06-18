> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers)

# DPL Modifiers

## Lookaround

The term "look around" means to "peek" either forward or backward from the current position in the input stream **without moving forward**. This allows conditional matching data at current position, based on what data is preceding or following:

| Modifier |  | Description |  | `>>` |  | **positive look ahead** - returns true if bytes forward from the current position match |
| --- | --- | --- | --- | --- | --- | --- |
| `!>>` |  | **negative look ahead** - returns true if bytes forward from the current position do not match |  |  |  |  |
| `<<` |  | **positive look behind** - returns true if up to 64 bytes backwards from the current position match |  |  |  |  |
| `!<<` |  | **negative look behind** - returns true if up to 64 bytes backwards from the current position do not match |  |  |  |  |

The modifier must be placed immediately before the matcher.

When look around is applied to multiple matchers (i.e a sub-pattern) then they must be enclosed in parenthesis.

#### Example

Conditional matching with look-behind. Suppose we need to extract from each line an address, whose last octet value is greater than 50:

```
1.2.3.4
1.2.3.40
1.2.3.55

```

Pattern:

```
IPADDR:ip_addr <<INT(min=50) EOL

```

The engine starts matching with `IPADDR:ip_addr` matcher from the first position in data. It does match '1.2.3.4' and the pointer is moved forward accordingly pointing at the line feed now. The engine proceeds with the next matcher, the look behind `INT` with a minimum value of 50. It encounters the value 4 (the last octet of IP address) but since it is less than the specified minimum, the match is discarded. The engine proceeds with the next matcher, `EOL` that does successfully match with the currently pointed line feed character. At this point, the pattern gets restarted from the beginning. The same cycle is repeated for the second row, which will also get discarded (the IP-address' last octet value 40 is less than the specified minimum). Only the IP-address in the
last row will be matched and made available for query:ip_addr`1.2.3.55`

For more realistic examples of using lookaround modifier see parsing multiline records examples.

## Configuration

Configuration is the way of telling execution-specific input parameters to a matcher, specified in the form of one or more key-value pair(s), enclosed in parentheses and separated by a comma:

```
MATCHER_EXPR '(' param_name '=' value [, ...] ')'

```

where value is a constant value (integer, string, float, …), or a matcher expression, enclosed in curly brackets
The configuration is optional and specific to matchers.

#### Example

When parsing date-time fields with the omitted timezone you can supply TIMESTAMP matcher with a configuration item specifying the timezone where parsed time string belongs:

```
TIMESTAMP(timezone='PST')

```

## Quantifier

Now and then you might encounter a record with repeating elements. When the number of elements is not fixed then we need a dynamic way of resolving it. This is what quantifiers are about: to match a variable number of repeating data elements within predefined limits.

The following table lists quantifier syntax and descriptions:

| Quantifier |  | Description |
| --- | --- | --- |
| `{ min, max }` |  | specifies repetition with minimum = min times, maximum = max times |
| `{ min, }` |  | specifies repetition with minimum = min times, maximum = 4096 times |
| `{ ,max }` |  | specifies repetition with minimum = 0 times, maximum = max times |
| `{ val }` |  | specifies the exact number of repetitions |
| `*` |  | specifies repetition with min 0 times and max 4096 times (i.e same as {0,} ) |
| `+` |  | specifies repetition with at least 1 times and max 4096 times (i.e same as {1,} ) |

#### Example

Parsing a username that can contain numbers, lower and uppercase letters and which must be at least 1 character long. When using a matcherdef-chargroup we must apply '+' quantifier, since by default it matches only one character.

```
[a-zA-Z0-9]+:username

```

## Optional Modifier

Irregularities in logs are very common. Even when the structure of records is defined, one may still have to deal with missing fields in the record. This can be handled by making a matcher optional in the pattern expression.

Syntax: place a question mark after the quantifier (and before the export_name):

```
MATCHER_EXPR '?'

```

It's important to note that there are two different situations with missing data:

1.

2.
- the field is there but **field value** is missing (the separator is still in place, line 2 in the example below)
3.

4.
- the **field value and following separator** both are missing (line 3 in the example below).
5.

From the parser standpoint, these are different: on line 2 the username field contains no value, in line 3 the username field is omitted completely. optional_modifier can handle both. Using a quantifier that allows repetitions the minimum zero times lets you parse the second line (i.e zero matches is allowed), but it fails on the third line.

#### Example

Note that in the first record all fields are present, in the second username value is missing and in the third, the username field is missing altogether.

```
14/Mar/2016:23:37:06 +0200,INFO,mary01,200
14/Mar/2016:23:37:07 +0200,INFO,,200
14/Mar/2016:23:37:13 +0200,INFO,500

```

```
(                   //a sequence_group of the following matchers:
 HTTPDATE:datetime
 UPPER:severity
 ALNUM?:user        //optional_modifier allows the engine to continue parsing when a field is missing
 INT:response
)(fs=',')           //separated by a comma
EOL;

```

Results:datetimeseverityuserresponse`2016-03-14 23:37:06 +0200``INFO``mary01``200``2016-03-14 23:37:07 +0200``INFO``NULL``200``2016-03-14 23:37:13 +0200``INFO``NULL``500`

## Export Name

Not all data in your source data stream is interesting or useful. For instance, field separators are not necessary when analyzing the content of a CSV file (although the parser engine needs to know where they are). To tell the parsing engine which elements should be made available to the query layer, an export_name must be assigned to the respective matcher. The assigned name becomes the name of the field you can refer to in the query. It will also be the name of the respective column heading of the resultset.

Export name is a string which:

- is preceded by a `:` (colon) symbol

- must begin with an upper or lowercase letter and

- is at least one character long and

- may contain only lower or uppercase letters and numbers

When adding a dot (`.`) to an export name, the name must be in quotes.

The export name is always the last item in the matcher expression (after matcherconf, quantifier and optional_modifier).

Any matcher output can be exported, including all matcher groups:

- chargroup,

- sequence group and

- alternatives group. Matched data is exported as STRING.

#### Example

Suppose our data record has only one field which may consist of either ipv4, ipv6 or domain name in it. We parse this field using alternatives group.

```
192.168.0.1
0000:0000:0000:0159:0000:0000:0000:0016
www.example.com

```

```
(                           // alternatives group:
  IPADDR:"ip.address" |     // IP address (IPv4, IPv6) or
  [ a-zA-Z0-9.-]*:fqdn      // FQDN
):remote                    // exporting group output as 'remote'
EOL

```

Each exported member of an alternative group will have value only when matched. By also exporting the output of the group, we will have the field 'remote 'which always has a value:ip.addressfqdnremote`192.168.0.1``NULL``192.168.0.1``::159:0:0:0:16``NULL``0000:0000:0000:0159:0000:0000:0000:0016``NULL``www.example.com``www.example.com`

To make the members of a composite data entity (a structure, array or JSON) visible to the query layer, the entity itself must be exported.
See STRUCTURE, ARRAY and JSON for details.
