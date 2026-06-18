> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/string-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/string-functions)

# String functions

String functions allow you to create expressions that manipulate text strings in a variety of ways.

All string matching functions are case-sensitive per default. If otherwise required, the `caseSensitive` parameter provides the ability to change the behavior.

```
...
| fieldsAdd str_found = contains(content, "FlushCommand", caseSensitive:false)

```

## concat

Concatenates the expressions into a single string.

#### Syntax

`concat(expression, … [, delimiter: ])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | double, long, string |  | A numeric or string expressions that should be concatenated with others. |  |  |
| delimiter |  | string |  | Constant string to be inserted between each concatenated value. Default: `""` (empty string). |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(a = "DQL", b = "is", c = "awesome!")
| fieldsAdd concat(a, b, c, delimiter: " ")

```

Query result:

| a |  | b |  | c |  | concat(a, b, c, delimiter: " ") |  | `DQL` |  | `is` |  | `awesome!` |  | `DQL is awesome!` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## contains

Searches the string expression for a substring. Returns `true` if the substring was found, `false` otherwise.

#### Syntax

`contains(expression, substring [, caseSensitive])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The field or expression to check. |  |  |
| substring |  | string |  | The substring that should be contained. |  |  |
| caseSensitive |  | boolean |  | Whether the search should be done in a case-sensitive way. The default value is `true`. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd contains(content, "DQL"),
            contains(content, "dql", caseSensitive: false),
            contains(content, "Query")

```

Query result:

| content |  | contains(content, "DQL") |  | contains(content, "dql", caseSensitive:FALSE) |  | contains(content, "Query") |  | `DQL is awesome!` |  | `true` |  | `true` |  | `false` |  | `Dynatrace Query Language` |  | `false` |  | `false` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## decodeUrl

Returns a URL-decoded string.

#### Syntax

`decodeUrl(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression that will be decoded. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "https%3A%2F%2Fwww.dynatrace.com%2Fplatform%2Fgrail"),
     record(content = "https://www.dynatrace.com/platform/grail")
| fieldsAdd decodeUrl(content)

```

Query result:

| content |  | decodeUrl(content) |  | `https%3A%2F%2Fwww.dynatrace.com%2Fplatform%2Fgrail` |  | `https://www.dynatrace.com/platform/grail` |  | `https://www.dynatrace.com/platform/grail` |  | `https://www.dynatrace.com/platform/grail` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## encodeUrl

Encodes a URL string by replacing characters that aren't numbers or letters with percentage symbols and hexadecimal numbers.

#### Syntax

`encodeUrl(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression that will be encoded. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "https://www.dynatrace.com/platform/grail")
| fieldsAdd encodeUrl(content)

```

Query result:

| content |  | encodeUrl(content) |  | `https://www.dynatrace.com/platform/grail` |  | `https%3A%2F%2Fwww.dynatrace.com%2Fplatform%2Fgrail` |
| --- | --- | --- | --- | --- | --- | --- |

## endsWith

Checks if a string expression ends with a suffix. Returns `true` if does, `false` otherwise.

#### Syntax

`endsWith(expression, suffix [, caseSensitive])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression that will be checked. |  |  |
| suffix |  | string |  | The suffix string with which the expression should end. |  |  |
| caseSensitive |  | boolean |  | Whether the check should be done in a case-sensitive way. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd endsWith(content, "awesome!"),
            endsWith(content, "AWESOME!", caseSensitive: false),
            endsWith(content, "Language")

```

Query result:

| content |  | endsWith(content, "awesome!") |  | endsWith(content, "AWESOME!", caseSensitive:FALSE) |  | endsWith(content, "Language") |  | `DQL is awesome!` |  | `true` |  | `true` |  | `false` |  | `Dynatrace Query Language` |  | `false` |  | `false` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## escape

Returns an escaped string.

1.

2.
- Single and double quotes are escaped. Backticks are not escaped.
3.

| Input |  | Output |  | `"` |  | `\"` |  | `'` |  | `\'` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

1.

2.
- Backslashes are escaped.
3.

| Input |  | Output |  | `\` |  | `\\` |
| --- | --- | --- | --- | --- | --- | --- |

1.

2.
- ASCII characters backspace, form feed, new line, carriage return, horizontal tabs are escaped.
3.

| Input |  | Output |  | `<backspace>` |  | `\b` |  | `<form feed>` |  | `\f` |  | `<new line>` |  | `\n` |  | `<carriage return>` |  | `\r` |  | `<horizontal tab>` |  | `\t` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

1.

2.
- ASCII characters within the range 0x20 - 0x7e (printable ASCII characters), that are not covered by any of the above rules, stay as they are.
3.

| Input |  | Output |  | `a` |  | `a` |  | `1` |  | `1` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

1.

2.
-

All other ASCII characters are represented as `\xhh`. This applies to the following characters

- characters within the range 0x00 - 0x07

- character 0x0b (vertical tab)

- characters within the range 0x0e - 0x1f

- character 0x7f

3.

| Input |  | Output |  | `<vertical tab>` |  | `\x0b` |
| --- | --- | --- | --- | --- | --- | --- |

1.

2.
- All characters in extended ASCII space (0x80-0xff) and Unicode characters outside of the ASCII space are represented as `\uhhhh`.
3.

| Input |  | Output |  | `ö` |  | `\u00f6` |
| --- | --- | --- | --- | --- | --- | --- |

#### Syntax

`escape(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string expression |  | The string expression that will be escaped. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = """"foo@bar.com""")
| fieldsAdd escape(content)

```

Query result:

| content |
| --- |
| escape(content) |
| `"foo@bar.com` |
| `\"foo@bar.com` |

## getCharacter

Returns the character at a given position from a string expression. Negative values for the position parameter are counted from the end of the string. If a position refers to a position outside the string, the function returns NULL.

#### Syntax

`getCharacter(expression, position)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  |  |  |  |
| position |  | long |  | The position at which to get the character. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd getCharacter(content, 1),
            getCharacter(content, 17),
            getCharacter(content, -1)

```

Query result:

| content |  | getCharacter(content, 1) |  | getCharacter(content, 17) |  | getCharacter(content, -1) |  | `DQL is awesome!` |  | `Q` |  | *null* |  | `!` |  | `Dynatrace Query Language` |  | `y` |  | `a` |  | `e` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## indexOf

Returns the index of the first occurrence of a substring in a string expression.
Starts to search forward from a given index. Negative values for the `from` parameter are counted from the end of the string.
The default value for `from` is `0` (the search from the start of the string).
The search is case-sensitive.
If the defined substring is not found, the function returns `-1`.

#### Syntax

`indexOf(expression, substring [, from])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression in which the substring is searched for. |  |  |
| substring |  | string |  | The substring expression to search for in the expression. |  |  |
| from |  | long |  | The index from which to start the forward search for the first occurrence of the substring within the expression. Negative values are counted from the end of the string. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd indexOf(content, "a"),
            indexOf(content, "a", from: 10),
            indexOf(content, "Query")

```

Query result:

| content |  | indexOf(content, "a") |  | indexOf(content, "a", from:10) |  | indexOf(content, "Query") |  | `DQL is awesome!` |  | `7` |  | `-1` |  | `-1` |  | `Dynatrace Query Language` |  | `3` |  | `17` |  | `10` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## jsonField

Parses a JSON string and extracts one value selected by its name.

#### Syntax

`jsonField(expression, fieldName [, seek])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The JSON string that should be parsed. |  |  |
| fieldName |  | string |  | The string literal with the key to be extracted. |  |  |
| seek |  | boolean |  | Flag indicating if the function should search for the first valid JSON object in the expression. The default value is `false`. |  |  |

#### Returns

The data type of the returned value is `long`, `double`, `boolean`, `string`, `array` or `record`.

#### Examples

##### Example 1

```
data record(content = """{
    "name":"John",
    "children":["Mallory", "Mary"],
    "address":{"city":"Boston", "zip":"02210"}
  }""")
| fieldsAdd jsonField(content, "name")

```

Query result:

| content |  | jsonField(content, "name") |  | `{"name":"John", "children":["Mallory", "Mary"], "address":{"city":"Boston", "zip":"02210"}}` |  | `John` |
| --- | --- | --- | --- | --- | --- | --- |

##### Example 2

```
data record(content = """JSON: {"name": "John"} ...""")
| fieldsAdd jsonField(content, "name", seek:false)
| fieldsAdd jsonField(content, "name", seek:true)

```

Query result:

| content |  | jsonField(content, "name", seek:FALSE) |  | jsonField(content, "name", seek:TRUE) |  | `JSON: {"name": "John"} ...` |  | `null` |  | `John` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## jsonPath

Parses a JSON string and extracts one value selected by a JSONPath expression.

#### Syntax

`jsonPath(expression, jsonPath [, seek])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The JSON string that should be parsed. |  |  |
| jsonPath |  | string |  | The string literal with the JSONPath expression of the value to be extracted. |  |  |
| seek |  | boolean |  | Flag indicating if the function should search for the first valid JSON object in the expression. The default value is `false`. |  |  |

#### Returns

The data type of the returned value is `long`, `double`, `boolean`, `string`, `array` or `record`.

#### Examples

##### Example 1

```
data record(content = """{
    "name":"John",
    "children":["Mallory", "Mary"],
    "address":{"city":"Boston", "zip":"02210"}
  }""")
| fieldsAdd jsonPath(content, "$.children[0]")
| fieldsAdd jsonPath(content, "$.address.city")
| fieldsAdd jsonPath(content, "$['address']['zip']")

```

Query result:

| content |  | jsonPath(content, "$.children[0]") |  | jsonPath(content, "$.address.city") |  | jsonPath(content, "$['address']['zip']") |  | `{"name":"John", "children":["Mallory", "Mary"], "address":{"city":"Boston", "zip":"02210"}}` |  | `Mallory` |  | `Boston` |  | `02210` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

```
data record(content = """JSON: {"name": "John"} ...""")
| fieldsAdd jsonPath(content, "$.name", seek:false)
| fieldsAdd jsonPath(content, "$.name", seek:true)

```

Query result:

| content |  | jsonPath(content, "$.name", seek:FALSE) |  | jsonPath(content, "$.name", seek:TRUE) |  | `JSON: {"name": "John"} ...` |  | `null` |  | `John` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## lastIndexOf

Returns the index of the last occurrence of a substring in a string expression. Starts to search backward from a given index. Negative values for the from parameter are counted from the end of the string. The default value for from is -1 (search from the end of the string). The search is case-sensitive. If the substring is not found, the function returns `-1`.

#### Syntax

`lastIndexOf(expression, substring [, from])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression in which the substring is searched for. |  |  |
| substring |  | string |  | The substring expression to search for in the expression. |  |  |
| from |  | long |  |  |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd lastIndexOf(content, "a"),
            lastIndexOf(content, "a", from: 10),
            lastIndexOf(content, "Query")

```

Query result:

| content |  | lastIndexOf(content, "a") |  | lastIndexOf(content, "a", from:10) |  | lastIndexOf(content, "Query") |  | `DQL is awesome!` |  | `7` |  | `7` |  | `-1` |  | `Dynatrace Query Language` |  | `21` |  | `6` |  | `10` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## levenshteinDistance

Computes the Levenshtein distance between two input strings.

#### Syntax

`levenshteinDistance(expression, expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| first expression |  | string |  | The first string expression to compute the Levenshtein distance from. |  |  |
| second |  | string |  | The second string expression to compute the Levenshtein distance from. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = "DQL is awesome!", b = "Grail is awesome!"),
     record(a = "Dynatrace Query Language", b = "DQL"),
     record(a = "Dynatrace Query Language", b = "dynatrace query language")
| fieldsAdd levenshteinDistance(a, b)

```

Query result:

| a |  | b |  | levenshteinDistance(a, b) |  | `DQL is awesome!` |  | `Grail is awesome!` |  | `5` |  | `Dynatrace Query Language` |  | `DQL` |  | `21` |  | `Dynatrace Query Language` |  | `dynatrace query language` |  | `3` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## like

Tests if a string expression matches a pattern. If the pattern does not contain percent signs, `like()` acts as the `==` operator (equality check). A percent character in the pattern `(%)` matches any sequence of zero or more characters. An underscore in the pattern `(\_)` matches a single character.

#### Syntax

`like(expression, pattern)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  |  |  |  |
| pattern |  | string |  |  |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd like(content, "%DQL%"),
            like(content, "D%L%"),
            like(content, "D_L%")

```

Query result:

| content |  | like(content, "%DQL%") |  | like(content, "D%L%") |  | like(content, "D_L%") |  | `DQL is awesome!` |  | `true` |  | `true` |  | `true` |  | `Dynatrace Query Language` |  | `false` |  | `true` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## lower

Converts a string to lowercase.

#### Syntax

`lower(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression to convert to lowercase. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd lower(content)

```

Query result:

| content |  | lower(content) |  | `DQL is awesome!` |  | `dql is awesome!` |  | `Dynatrace Query Language` |  | `dynatrace query language` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## matchesPattern

Tests if a string expression matches the DPL pattern and returns `true` if it does, otherwise, returns `false`.

#### Syntax

`matchesPattern(expression, pattern)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | A field or string expression to test. |  |  |
| pattern |  | string |  | The matching pattern. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "2023-11-01 12:52:12 : 766"),
     record(content = "2023-11-01 12:53:00:123"),
     record(content = "2023-11-01 12:55:59 : 192.168.0.1")
| fieldsAdd matchesPattern(content, "TIME ' : ' LONG"),
            matchesPattern(content, "TIME ' : ' IP")

```

Query result:

| content |
| --- |
| matchesPattern(content, "TIME ' : ' LONG") |
| matchesPattern(content, "TIME ' : ' IP") |
| `2023-11-01 12:52:12 : 766` |
| `true` |
| `false` |
| `2023-11-01 12:53:00:123` |
| `false` |
| `false` |
| `2023-11-01 12:55:59 : 192.168.0.1` |
| `false` |
| `true` |

## matchesPhrase

Matches a phrase against the input string expression using token matchers.

#### Syntax

`matchesPhrase(expression, phrase [, caseSensitive] [, wildcard])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, array |  | The expression (string or array of strings) that should be checked. |  |  |
| phrase |  | string |  | The phrase to search for. |  |  |
| caseSensitive |  | boolean |  | Whether the match should be done case-sensitive. Default: `false`. |  |  |
| wildcard |  | string |  | A single character to use as the wildcard symbol. Default: `*`. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language"),
     record(content = array("DQL", "is", "awesome", "!", "Dynatrace Query Language"))
| fieldsAdd matchesPhrase(content, "DQL"),
            matchesPhrase(content, "Dyna"),
            matchesPhrase(content, "query"),
            matchesPhrase(content, "query", caseSensitive: true)

```

Query result:

| content |  | matchesPhrase(content, "DQL") |  | matchesPhrase(content, "Dyna") |  | matchesPhrase(content, "query") |  | matchesPhrase(content, "query", caseSensitive:TRUE) |  | `DQL is awesome!` |  | `true` |  | `false` |  | `false` |  | `false` |  | `Dynatrace Query Language` |  | `false` |  | `false` |  | `true` |  | `false` |  | `[DQL, is, awesome, !, Dynatrace Query Language]` |  | `true` |  | `false` |  | `true` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Pattern matching

The `matchesPhrase` function supports token matching using wildcards. To match any sequence of zero or more characters in a token, you can use a wildcard character (default: `*`) anywhere in the search phrase. Use the wildcard parameter to match literal `*` characters. A pattern supports a maximum of 64 wildcard characters. Consecutive wildcards (for example, `**`) aren't supported.

##### Example 2

```
data record(content = "Dynatrace Query Language"),
     record(content = "DQL is awesome!"),
     record(content = "D*L")
| fieldsAdd matchesPhrase(content, "Dyna*"),
            matchesPhrase(content, "D*L"),
            matchesPhrase(content, "D*L", wildcard:"%")

```

Query result:

| content |  | `matchesPhrase(content, "Dyna*")` |  | `matchesPhrase(content, "D*L")` |  | `matchesPhrase(content, "D*L", wildcard:"%")` |  | `Dynatrace Query Language` |  | `true` |  | `false` |  | `false` |  | `DQL is awesome!` |  | `false` |  | `true` |  | `false` |  | `D*L` |  | `false` |  | `true` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## matchesValue

Searches records for a specific value in a given attribute. Returns `true` or `false`.

#### Syntax

`matchesValue(expression, value, … [, caseSensitive] [, wildcard])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string, smartscapeId, array |  | The expression (string or array of strings) that should be checked. |  |  |
| value |  | string, array |  | The value to search for using patterns (supports an array of patterns or a list of patterns). |  |  |
| caseSensitive |  | boolean |  | Whether the match should be done case-sensitive (default: `false`). |  |  |
| wildcard |  | string |  | A single character to use as the wildcard symbol. Default: `*`. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

Values are matched case-insensitive by default:

```
data record(content = "User 'käärmanü' failed to login from 192.168.0.1")
| fieldsAdd matchesValue(content, "User*"),
            matchesValue(content, "user*"),
            matchesValue(content, "user*", caseSensitive: true)

```

Query result:

| content |  | matchesValue(content, "User*") |  | matchesValue(content, "user*") |  | matchesValue(content, "user*", caseSensitive:TRUE) |  | `User 'käärmanü' failed to login from 192.168.0.1` |  | `true` |  | `true` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

Only ASCII characters are matched case-insensitive:

```
data record(content = "Österreich")
| fieldsAdd matchesValue(content, "österreich"),
            matchesValue(content, "Österreich")

```

Query result:

| content |  | matchesValue(content, "österreich") |  | matchesValue(content, "Österreich") |  | `Österreich` |  | `false` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 3

The function handles values of arrays in "any-match" manner.

```
data record(technologies = array("Java11", "java17"))
| fieldsAdd matchesValue(technologies, "Java11"),
            matchesValue(technologies, "java"),
            matchesValue(technologies, "java*")

```

Query result:

| technologies |  | matchesValue(technologies, "Java11") |  | matchesValue(technologies, "java") |  | matchesValue(technologies, "java*") |  | `[Java11, java17]` |  | `true` |  | `false` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Pattern matching

The `matchesValue` function supports pattern matching using wildcards. To match any sequence of zero or more characters in the expression, you can use a wildcard character (default: `*`) anywhere in the pattern. Use the wildcard parameter to match literal `*` characters. A pattern supports a maximum of 64 wildcard characters. Consecutive wildcards (for example, `**`) aren't supported.

##### Example 4

Values are matched from the beginning. To match parts of the value, use `*` as wildcard symbol:

```
data record(content = "User 'käärmanü' failed to login from 192.168.0.1")
| fieldsAdd matchesValue(content, "192.168.0.1"),
            matchesValue(content, "*192.168.0.1"),
            matchesValue(content, "*failed to log*")

```

Query result:

| content |  | matchesValue(content, "192.168.0.1") |  | matchesValue(content, "*192.168.0.1") |  | matchesValue(content, "*failed to log*") |  | `User 'käärmanü' failed to login from 192.168.0.1` |  | `false` |  | `true` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Multi-pattern comparison

The `matchesValue()` function supports matching against multiple patterns. You can use it by either providing an array or a list of patterns with the `value` parameter. Only strings are supported as patterns. Other datatypes don't produce a match and are ignored. The `matchesValue()` function returns true if any of the patterns matches. In case none of the patterns produce a match, `false` is returned.

##### Example 5

```
data record(content = array("DQL", "is", "awesome", "!"))
| fieldsAdd matchesValue(content, array("Grail", "dql")),
            matchesValue(content, {"Grail", "dql"}),
            matchesValue(content, {"Grail", "dq*"}),
            matchesValue(content, {"Grail", "dq*"}, caseSensitive: true)

```

Query result:

| content |  | matchesValue(content, array("Grail", "dql")) |  | matchesValue(content, {"Grail", "dql"}) |  | matchesValue(content, {"Grail", "dq*"}) |  | matchesValue(caseSensitive:TRUE, content, {"Grail", "dq*"}) |  | `DQL, is, awesome, !` |  | `true` |  | `true` |  | `true` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## parse

Extracts a single value from a string as specified in the pattern or a record if there are multiple named matchers.

#### Syntax

`parse(expression, pattern)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | A field or string expression to parse. |  |  |
| pattern |  | string |  | The parse pattern. Must conform with patterns (see [DPL](/platform/grail/dynatrace-pattern-language)). |  |  |

#### Returns

The `parse` function returns a single value, which can be either of primitive type or a record. The result is of primitive type in case of a single named matcher in the DPL pattern. If there are multiple named matchers in the pattern, then the result is a record containing fields corresponding to the names of the matchers.
Fields created from the output of the `parse` function by default get the name of the named matcher in the DPL pattern. In case of multiple named matchers in the pattern, the default field name is `parsed_record`. You can also define alternative field names using an alias expression.

#### Examples

##### Example 1

```
data record(src = "1 2"),
     record(src = "45 46 47 48")
| fieldsAdd parse(src, "LONG:result"),
            value = parse(src, "LONG:result"),
            parse(src, "LONG:field1 ' ' LONG:field2")

```

Query result:

| src |
| --- |
| result |
| value |
| parsed_record |
| `1 2` |
| `1` |
| `1` |
| **field1**: `1`**field2**: `2` |
| `45 46 47 48` |
| `45` |
| `45` |
| **field1**: `45`**field2**: `46` |

## parseAll

Extracts several values from a string as specified in the pattern.
Unlike the [`parse`](/platform/grail/dynatrace-query-language/functions/string-functions#parse) function, `parseAll` returns an array all the time. The array can be empty if no patterns matched. A single element can be primitive type or a record.

#### Syntax

`parseAll(expression, pattern)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | A field or string expression to parse. |  |  |
| pattern |  | string |  | The parse pattern. Must conform with [DPL patterns](/platform/grail/dynatrace-pattern-language). |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(src = "1 2"),
     record(src = "45 46 47 48")
| fieldsAdd parseAll(src, "LONG:result"),
            value = parseAll(src, "LONG:result"),
            parseAll(src, "LONG:field1 ' ' LONG:field2")

```

Query result:

| src |
| --- |
| result |
| value |
| parsed_records |
| `1 2` |
| `[1, 2]` |
| `[1, 2]` |
| [**field1:** `1` **field2** `2`] |
| `45 46 47 48` |
| `[45, 46, 47, 48]` |
| `[45, 46, 47, 48]` |
| [**field1:** `45` **field2** `46`, **field1:** `47` **field2** `48`] |

## punctuation

Extracts punctuation characters out of an input string.

#### Syntax

`punctuation(expression, [, count] [, withSpace])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression from which the punctuation characters are extracted. |  |  |
| count |  | positive integer |  | The maximum number of returned punctuation characters. Default: `32`. |  |  |
| withSpace |  | boolean |  | Whether space characters should be included. Default: `false`. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

In this example, we extract the punctuation characters from each input string.

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language"),
     record(content = "${placeholder}")
| fieldsAdd punctuation(content),
            punctuation(content, count: 2),
            punctuation(content, count: 2, withSpace: true)

```

Query result:

| content |  | punctuation(content) |  | punctuation(content, count:2) |  | punctuation(content, count:2, withSpace:TRUE) |  | `DQL is awesome!` |  | `!` |  | `!` |  | `__` |  | `Dynatrace Query Language` |  | *empty string* |  | *empty string* |  | `__` |  | `$${placeholder}` |  | `$${}` |  | `$${` |  | `$${` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## replacePattern

Replaces each substring of a string that matches the DPL pattern with the given string. The pattern must be defined as a constant string expression. For additional details about pattern syntax, see the [DPL documentation](/platform/grail/dynatrace-pattern-language).

#### Syntax

`replacePattern(expression, pattern, replacement)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | A field or string expression to replace. |  |  |
| pattern |  | string |  | The replacing pattern. |  |  |
| replacement |  | string |  | The string that should replace the found substrings. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL 2019-08-01 09:30:00"),
     record(content = "Dynatrace Query L4nguage")
| fieldsAdd replacePattern(content, "TIME", "is awesome!"),
            replacePattern(content, "LONG", "a")

```

Query result:

| content |
| --- |
| replacePattern(content, "TIME", "is awsome!") |
| replacePattern(content, "LONG", "a") |
| `DQL 2019-08-01 09:30:00` |
| `DQL is awesome!` |
| `DQL aaa a:a:a` |
| `Dynatrace Query L4nguage` |
| `Dynatrace Query L4nguage` |
| `Dynatrace Query Language` |

## replaceString

Replaces each substring of a string with a given string. This function replaces only exactly matched substrings from the original string to the replacement. Matching is case-sensitive and doesn't use any wildcards. All found patterns will be replaced if they do not intersect. For instance, replacing `abcabca` in a string with `abca` pattern produces only one replacement. Only the first occurrence at the beginning of the string will be replaced.

#### Syntax

`replaceString(expression, substring, replacement)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The field or expression where substrings should be replaced. |  |  |
| substring |  | string |  | The substring that should be replaced. |  |  |
| replacement |  | string |  | The string that should replace the found substrings. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language"),
     record(content = "abcabca")
| fieldsAdd replaceString(content, "awesome", "simple"),
            replaceString(content, "abca", "xyz")

```

Query result:

| content |  | replaceString(content, "awesome", "simple") |  | replaceString(content, "abca", "xyz") |  | `DQL is awesome!` |  | `DQL is simple!` |  | `DQL is awesome!` |  | `Dynatrace Query Language` |  | `Dynatrace Query Language` |  | `Dynatrace Query Language` |  | `abcabca` |  | `abcabca` |  | `xyzbca` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## splitByPattern

Splits a string into an array at each occurrence of the DPL pattern.

#### Syntax

`splitByPattern(expression, pattern)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | A field or string expression to split. |  |  |
| pattern |  | string |  | The splitting pattern. Must conform with [DPL patterns](/platform/grail/dynatrace-pattern-language). |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(content = "one $1 two $4 three"),
     record(content = "foo $1000 bar"),
     record(content = "no separator"),
     record(content = "")
| fieldsAdd splitByPattern(content, " ' $' LONG ' ' ")

```

Query result:

| content |
| --- |
| splitByPattern(content, " ' $' LONG ' ' ") |
| `one $1 two $4 three` |
| `[one, two, three]` |
| `foo $1000 bar` |
| `[foo, bar]` |
| `no separator` |
| `[no separator]` |
| *empty string* |
| `[]` |

## splitString

Splits a string according to the parameters set.

Retrieves an array of substrings of the specified expression that are adjacent to occurrences of the given pattern.

Parameters are interpreted literally. For example, splitting `www.dynatrace.org` by `.` results in `www` and `dynatrace` and `org`.

Using an empty string as a pattern splits the string into one-byte substrings. For example, a split of four characters becomes an array of four strings having one byte each (splitting the `"1234"` expression results in `array("1", "2", "3", "4")`).

The non-ASCII characters are represented by multiple bytes. Splitting a string containing such characters by `""` breaks these bytes apart into separate invalid strings.

If the pattern is not found in the expression, it returns an array that contains only the input expression.

If the expression starts with one or more occurrences of the pattern, an empty string will be added for each occurrence. For example, `splitString("abc", "a")` results in `"", "bc"`. Analogically, empty strings are added if the pattern is found at the end of the expression.

An empty string is also added for adjacent occurrences of the pattern that do not border the start or end of the string. For example, `splitString("abbc", "b")` results in `"a", "", "c"`.

If the pattern is empty, it splits the expression into one-byte substrings. For example, `splitString("abc", "")` results in `"a", "b", "c"`.

#### Syntax

`splitString(expression, pattern)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression to split up into an array. |  |  |
| pattern |  | string |  | The pattern to split the string expression at, or the empty string to split into one-byte strings. |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd splitString(content, " "),
            splitString(content, "is"),
            splitString(content, ""),
            splitString(content, "XYZ")

```

Query result:

| content |  | splitString(content, " ") |  | splitString(content, "is") |  | splitString(content, "") |  | splitString(content, "XYZ") |  | `DQL is awesome!` |  | `[DQL, is, awesome!]` |  | `[DQL ,  awesome!]` |  | `[D, Q, L,  , i, s,  , a, w, e, s, o, m, e, !]` |  | `[DQL is awesome!]` |  | `Dynatrace Query Language` |  | `[Dynatrace, Query, Language]` |  | `[Dynatrace Query Language]` |  | `[D, y, n, a, t, r, a, c, e,  , Q, u, e, r, y,  , L, a, n, g, u, a, g, e]` |  | `[Dynatrace Query Language]` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## startsWith

Checks if a string expression starts with a prefix. Returns `true` if does, `false` otherwise.

#### Syntax

`startsWith(expression, prefix [, caseSensitive])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression that will be checked. |  |  |
| prefix |  | string |  | The prefix string with which the expression should start. |  |  |
| caseSensitive |  | boolean |  | Whether the check should be done in a case-sensitive way. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd startsWith(content, "D"),
            startsWith(content, "dql", caseSensitive: false)

```

Query result:

| content |  | startsWith(content, "D") |  | startsWith(content, "dql", caseSensitive:FALSE) |  | `DQL is awesome!` |  | `true` |  | `true` |  | `Dynatrace Query Language` |  | `true` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## stringLength

Returns the length of a string expression. Length is defined as the number of UTF-16 code units, which is often the same as the number of characters in the string. In some cases, the number of characters is smaller than the number of UTF-16 code units, for example when Combining Diacritical Marks are used, or if characters outside the Basic Multilingual Plane (BMP), such as Emoji, are present.

If your use case requires consistent length for the same characters, consider ingesting strings after Unicode normalization.

No specific normalization form is guaranteed for Dynatrace-provided strings.

#### Syntax

`stringLength(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression to get the number of UTF-16 code units for. |  |  |

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language"),
     record(content = "🐕‍🦺")
| fieldsAdd stringLength(content)

```

Query result:

| content |  | stringLength(content) |  | `DQL is awesome!` |  | `15` |  | `Dynatrace Query Language` |  | `24` |  | `🐕‍🦺` |  | `5` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## substring

Gets a code unit range using a start index (inclusive) and an end index (exclusive).

Returns an empty string if from `>=` to.

`Indexes >=0` are relative to the start of the string and address consecutive characters from left to right, starting from the index position.

`Indexes <=-1` are relative to the last character of the string and are used to address characters from the right side of an expression, for example, `-2` is the penultimate character.

`Positive indexes` beyond the bounds of the string are assigned to the string length.

`Negative indexes` beyond the bounds of the string are equal to `0`. For example, in the `321` string, the index `-4` is beyond the bounds of the string therefore it equals `0`. However, the index `-2` is located within the bounds of that string and extracts `21` if used as a `from` the index.

The returned substring never starts or ends with an incomplete UTF-16 surrogate pair. Instead of that, it starts or ends with a question mark. This safeguards against the creation of invalid Unicode strings.

#### Syntax

`substring(expression [, from] [, to])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression to get a substring of. |  |  |
| from |  | long |  | Index of first code unit to include in sub-string, inclusive, relative to start of `expression` if positive, relative to end if negative. Clamped at string bounds. |  |  |
| to |  | long |  | Index of last code unit to include in sub-string, exclusive, relative to start of `expression` if positive, relative to end if negative. Clamped at string bounds. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd substring(content, from: 4),
            substring(content, from: -2),
            substring(content, from: 4, to: 9),
            substring(content, from: -42, to: 42)

```

Query result:

| content |  | substring(content, from:4) |  | substring(content, from:-2) |  | substring(content, from:4, to:9) |  | substring(content, from:-42, to:42) |  | `DQL is awesome!` |  | `is awesome!` |  | `e!` |  | `is aw` |  | `DQL is awesome!` |  | `Dynatrace Query Language` |  | `trace Query Language` |  | `ge` |  | `trace` |  | `Dynatrace Query Language` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## trim

Removes leading and trailing whitespaces. Any code point <= ASCII 32 in decimal is considered a whitespace, where ASCII 32 is a blank space.

#### Syntax

`trim(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression to remove leading and trailing white-space from. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = " DQL is awesome!"),
     record(content = " Dynatrace Query Language ")
| fieldsAdd trim(content)

```

Query result:

| content |  | trim(content) |  | `" DQL is awesome!"` |  | `DQL is awesome!` |  | `" Dynatrace Query Language "` |  | `Dynatrace Query Language` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## unescape

Returns an unescaped string.

1.

2.
- Single quotes, double quotes and backticks are unescaped.
3.

| Input |  | Output |  | `\"` |  | `"` |  | `\'` |  | `'` |  | `\`` |  | ``` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

1.

2.
- Backslashes are unescaped.
3.

| Input |  | Output |  | `\\` |  | `\` |
| --- | --- | --- | --- | --- | --- | --- |

1.

2.
- ASCII characters bell, backspace, form feed, new line, carriage return, horizontal tab and vertical tab are unescaped.
3.

| Input |  | Output |  | `\a` |  | `<bell>` |  | `\b` |  | `<backspace>` |  | `\f` |  | `<form feed>` |  | `\n` |  | `<new line>` |  | `\r` |  | `<carriage return>` |  | `\t` |  | `<horizontal tab>` |  | `\v` |  | `<vertical tab>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

1.

2.
- `\xhh` within standard ASCII space (0x00 - 0x7f) is replaced by the related character.
3.

| Input |  | Output |  | `\x40` |  | `@` |  | `\x64` |  | `d` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

1.

2.
- `\xhh` within extended ASCII space (0x80 - 0xff) is interpreted as `\u00hh` and replaced by the related Unicode character.
3.

| Input |  | Output |  | `\xff` |  | `ÿ` |
| --- | --- | --- | --- | --- | --- | --- |

1.

2.
- `\uhhhh` is replaced by the related Unicode character.
3.

| Input |  | Output |  | `\u002e` |  | `.` |  | `\u0064` |  | `d` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Syntax

`unescape(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string expression |  | The string expression that will be unescaped. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = """"foo\x40bar\u002ecom""")
| fieldsAdd unescape(content)

```

Query result:

| content |
| --- |
| unescape(content) |
| `"foo\x40bar\u002ecom` |
| `"foo@bar.com` |

## unescapeHtml

Unescapes HTML in a string by replacing ASCII characters with HTML syntax.

#### Syntax

`unescapeHtml(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression that will be unescaped. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is &lt;bold&gt;awesome&lt;/bold&gt;!"),
     record(content = "&lt;a href=&quot;https://www.dynatrace.com/platform/grail&quot;&gt;Dynatrace Query Language&lt;/a&gt;")
| fieldsAdd unescapeHtml(content)

```

Query result:

| content |  | unescapeHtml(content) |  | `DQL is &lt;bold&gt;awesome&lt;/bold&gt;!` |  | `DQL is <bold>awesome</bold>!` |  | `&lt;a href=&quot;https://www.dynatrace.com/platform/grail&quot;&gt;Dynatrace Query Language&lt;/a&gt;` |  | `<a href="https://www.dynatrace.com/platform/grail">Dynatrace Query Language</a>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## upper

Converts a string to uppercase.

#### Syntax

`upper(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression to convert to uppercase. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),
     record(content = "Dynatrace Query Language")
| fieldsAdd upper(content)

```

Query result:

| content |  | upper(content) |  | `DQL is awesome!` |  | `DQL IS AWESOME!` |  | `Dynatrace Query Language` |  | `DYNATRACE QUERY LANGUAGE` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
