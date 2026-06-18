> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-lines-strings](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-lines-strings)

# DPL Lines and Strings

## Line Breaks

**EOL; LF**

Matches the single line feed character (ASCII 0xa).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| none |  | default value: `{1,1}` - requires matching minimum 1 and maximum 1 bytes |  | none |

**CR**

Matches single carriage return character (ASCII 0xd).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| none |  | default value: `{1,1}` - requires matching minimum 1 and maximum 1 bytes |  | none |

**EOLWIN**

Matches two characters: line feed followed by the carriage return (ASCII 0xd 0xa)

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| none |  | default value: `{2,2}` - requires matching minimum 2 and maximum 2 bytes |  | none |

## Line Data

**LD, LDATA**

Matches any characters until the next non-optional matcher in the scope of a line.

LD must always be followed by a non-optional matcher expression

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | default value: `{1,4096}` - requires matching minimum 1 and maximum 4096 bytes |  |  |

#### Example 1

Parsing lines ending with single line-feed character (i.e a *NIX text file). Note that line endings are marked with 'n' for clarity:

```
Red fox jumps over lazy dog\n
\n
The end\n

```

The following pattern extracts the content of the entire line - i.e matches any character until the line-feed:

```
LD:line EOL

```

Results in the first and third lines being parsed out. The second line fails to parse because LD matcher encountered an end of line before required minimum matching count (default 1):line`Red fox jumps over lazy dog``The end`

#### Example 2

Extracting username field from a CSV file:

```
2016-01-03 00:13:28,110.188.4.216,forerequest,200
2016-01-06 06:35:24,48.242.116.66,unrioting,200
2016-01-05 11:49:01,223.11.158.94,ribassano,404

```

```
TIMESTAMP:date_time ','
IPADDR:ip           ','
LD:username         ','
LD EOL;

```

where:

1.

2.
- extracts time and date, followed by field separator ','
3.

4.
- extracts ip-address, followed by field separator ','
5.

6.
- extracts username by matching any characters until field separator ','
7.

8.
- matches but does not extract any character for the rest of the line
9.

Results:date_timeipusername`2016-01-03 00:13:28 +0000``110.188.4.216``forerequest``2016-01-06 06:35:24 +0000``48.242.116.66``unrioting``2016-01-05 11:49:01 +0000``223.11.158.94``ribassano`

## Multiline Data

**DATA**

Matches any characters until the next non-optional matcher of pattern expression.

DATA must always be followed by a non-optional matcher expression.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | default value: `{1,4096}` - requires matching minimum 1 and maximum 4096 bytes |  |  |

#### Example

Parsing stack trace records, laid over multiple lines and terminated by an empty line - i.e two consecutive line breaks:

```
$25
```

```
DATA:record (EOL EOL)

```

## Quoted Strings

**SQS**

Matches string enclosed between single quotes (ASCII 0x27). Any single quote inside the string must be escaped by backslash character "".

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | default value: `{1,4096}` - requires matching minimum 1 and maximum 4096 bytes |  |  |

#### Example

```
'Ay caramba!'

'Homer said: d\'oh!'

```

```
SQS:sq_string EOL

```

Result:sq_string`Ay caramba!``Homer said: d'oh!`

Parsing the empty second line fails since SQS expects by default at least one character matching.

**DQS**

Matches string enclosed between double-quote characters (ASCII 0x22).
Any double quote inside the string must be escaped by a backslash character (ASCII 0x5c).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | default value: `{1,4096}` - requires matching minimum 1 and maximum 4096 bytes |  |  |

#### Example

```
"Red fox jumps over lazy dog"
"Red fox jumps over "lazy" dog"

```

```
DQS:dq_string EOL

```

Result:dq_string`Red fox jumps over lazy dog``Red fox jumps over ''lazy'' dog`

**CSVSQS**

Matches string enclosed between single quotes (ASCII 0x27). Any single quote inside the string must be escaped by single quote character (CSV
style).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | default value: `{1,4096}` - requires matching minimum 1 and maximum 4096 bytes |  |  |

#### Example

```
'Red fox jumps over lazy dog'
'Red fox jumps over ''lazy'' dog'

```

```
CSVSQS:csvsq_string EOL

```

Result:csvsq_string`Red fox jumps over lazy dog``Red fox jumps over 'lazy' dog`

**CSVDQS**

Matches string enclosed between double-quote characters (ASCII 0x22). Any double quote inside the string must be escaped by double-quote character (CSV style).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | default value: `{1,4096}` - requires matching minimum 1 and maximum 4096 bytes |  |  |

#### Example

```
"Red fox jumps over lazy dog"
"Red fox jumps over ""lazy"" dog"

```

```
CSVSQS:csvsq_string EOL

```

Result:csvsq_string`Red fox jumps over lazy dog``Red fox jumps over ''lazy'' dog`

## Character Group

**`[ char ... ]`**

Matches a single character out of several in a defined group. Simply place the characters you want to match between square brackets.

Characters can also be expressed as ranges, for instance [0-9] matches any digit from 0 to 9. Negating is supported by placing a caret "^" or
an exclamation mark "!" before characters.

In case you want to match a square bracket character, it must be escaped by a preceding backslash character(0x5c ASCII ).

Use a quantifier if you want to match more than single characters.

The syntax is compatible with [Regular Expression Character Class](https://www.regular-expressions.info/charclass.html).

Character group allows matching strings with specific characters (as opposed to LD or DATA which matches any characters).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | default value: `{1,1}` - requires matching minimum 1 and maximum 1 bytes |  |  |

#### Example

Extracting username field, which is expected to consist of lowercase letters a to z and numbers, with minimum length of 4 characters and a maximum length of 15 characters:

```
2016-01-03 00:13:28,110.188.4.216,forerequest,200
2016-01-06 06:35:24,48.242.116.66,02rioting,200
2016-01-05 11:49:01,223.11.158.94,ribassano,404

```

```
TIMESTAMP:date_time           ','
IPADDR:ip                     ','
[{*}0-9{*}a-z]{4,15}:username ','
LD EOL;

```

where:

1.

2.
- extracts time and date, followed by field separator ','
3.

4.
- extracts ip-address, followed by field separator ','
5.

6.
- extracts username by matching characters a to z, min 4, max 10 times, followed by field separator ','
7.

8.
- matches but does not extract any character for the rest of the line
9.

Results in all lines parsed into fields `date_time, ip, username`.date_timeipusername`2016-01-03 00:13:28 +0000``110.188.4.216``forerequest``2016-01-06 06:35:24 +0000``48.242.116.66``02rioting``2016-01-05 11:49:01 +0000``223.11.158.94``ribassano`

## POSIX Character Classes

Match **one or more character** corresponding to any of the characters in its defined group.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | default value: `{1,4096}` - requires matching minimum 1 and maximum 1 bytes |  |  |

You may use both matcher or POSIX notation.

**ALNUM**

POSIX notation: `[:alnum:]`

Matches alphanumeric characters `a-z; A-Z; 0-9`

**ALPHA**

`[:alpha:]` Matches alphabetic characters `a-z; A-Z`

**BLANK**

`[:blank:]` Matches space (`0x20`) and tab (`0x9`) characters

**CNTRL**

`[:cntrl:]` Matches control characters in ASCII range: `0x1-0x1F; 0x7`

**DIGIT**

`[:digit:]` Matches digits in range of `0-9`

**GRAPH**

`[:graph:]` Matches visible characters in the ASCII code range
`0x21 - 0x7E`

**LOWER**

`[:lower:]` Matches lowercase letters `a-z`

**PRINT**

`[:print:]` Matches printable characters in the ASCII code range
`0x20 - 0x7E`

**PUNCT**

`[:punct:]` Matches punctuation and symbols
`!"#$%&'()*+,\-./:;<=>?@[]^_`{|}~|`

**SPACE**

`[:space:]` Matches all whitespace characters. In ASCII codes:
`0x20; 0x9; 0xA 0xB; 0xC; 0xD`

**NSPACE**

`[!:space:]` Matches all characters except whitespace.

**UPPER**

`[:upper:]` Matches uppercase letters `A-Z`

**XDIGIT**

`[:xdigit:]` Matches digits in hexadecimal notation `0x0 - 0xF`

**ASCII**

`[:ascii:]` Matches all ASCII characters in the range of `0x0 - 0x7F`

**WORD**

`[:word:]` Matches words: letters a-z; A-Z; numbers `0-9` and underscore
`_`

**`[:any:]`**

Matches any character in ASCII range `0x0 - 0xff`

#### Example

Extracting username field, which is expected to consist of
only lowercase letters a to z, with minimum length of 4 characters and a
maximum length of 15 characters:

```
2016-01-03 00:13:28,110.188.4.216,forerequest,200
2016-01-06 06:35:24,48.242.116.66,02rioting,200
2016-01-05 11:49:01,223.11.158.94,ribassano,404

```

```
TIMESTAMP:date_time  ','
IPADDR:ip            ','
LOWER{4,15}:username ','
LD EOL;

```

where:

1.

2.
- extracts time and date, followed by field separator ','
3.

4.
- extracts ip-address, followed by field separator ','
5.

6.
- extracts username by matching lowercase characters, min 4, max 10 times, followed by field separator ','
7.

8.
- matches but does not extract any character for the rest of the line
9.

Results in first and third lines parsed into fields `date_time, ip, username`. The second line fails to parse because of
username contains numbers.date_timeipusername`2016-01-03 00:13:28 +0000``110.188.4.216``forerequest``1970-01-01 00:00:00.000 +0000``255.255.255.255``2016-01-05 11:49:01 +0000``223.11.158.94``ribassano`
