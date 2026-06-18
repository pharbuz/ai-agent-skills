> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-grammar](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-grammar)

# DPL Grammar

| Matcher |  | Description |
| --- | --- | --- |
| `ENUM{ string=integer, ...}` |  | enum value matcher. See: [DPL Enum](/platform/grail/dynatrace-pattern-language/log-processing-enum) |
| `JSON`, `JSON_OBJECT{ jsonFields ... }` |  | JSON matcher. See: [DPL JSON Objects](/platform/grail/dynatrace-pattern-language/log-processing-json-object) |
| `JSON_ARRAY`, `JSON_ARRAY{jsonValueType}` |  | JSON array matcher.See: [DPL JSON Arrays](/platform/grail/dynatrace-pattern-language/log-processing-json-array) |
| `JSON_VALUE`,`JSON_VALUE{jsonValueType}` |  | JSON value matcher. See: [DPL JSON Values](/platform/grail/dynatrace-pattern-language/log-processing-json-value) |
| `KVP{patternExprs}` |  | Key-value pair matcher. See: [DPL Key-Value Pairs](/platform/grail/dynatrace-pattern-language/log-processing-key-value-pairs) |
| `ARRAY{patternExprs}` |  | Array matcher. See: [DPL Array](/platform/grail/dynatrace-pattern-language/log-processing-array) |
| `STRUCTURE{patternExprs}` |  | Structure matcher. See: [DPL Structure](/platform/grail/dynatrace-pattern-language/log-processing-structure) |
| `DATA` |  | Multiline data matcher. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `LDATA`, `LD` |  | Line data matcher. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `(patternExpr | ...)` |  | Alternatives group. See: [DPL Alternatives Group](/platform/grail/dynatrace-pattern-language/log-processing-alternatives-group) |
| `(patternExpr, ...)` |  | Sequence group. See: [DPL Sequence Group](/platform/grail/dynatrace-pattern-language/log-processing-sequence-group) |
| `EOL`, `LF` |  | Matches Line Feed character. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `EOLWIN`, `WINEOL` |  | Matches Line Feed, Carriage Return characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `CR` |  | Matches single Carriage Return character. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `UPPER` |  | Matches uppercase characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `LOWER` |  | Matches lowercase characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `ALPHA` |  | Matches alphabetic characters `a-z; A-Z`. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `DIGIT` |  | Matches digits. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `XDIGIT` |  | Matches digits in hexadecimal notation. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `ALNUM` |  | Matches alphanumeric characters `a-z; A-Z; 0-9`. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `PUNCT` |  | Matches punctuation and symbol characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `BLANK` |  | Matches space and tab characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `SPACE` |  | Matches whitespace characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `NSPACE` |  | Matches all characters except whitespace. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `GRAPH` |  | Matches visible characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `PRINT` |  | Matches printable characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `WORD` |  | Matches words. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `ASCII` |  | Matches all ASCII characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `CNTRL` |  | Matches control characters. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `TIME`, `TIMESTAMP` |  | Matches time and date. See: [DPL Time and Date](/platform/grail/dynatrace-pattern-language/log-processing-time-date) |
| `JSONTIMESTAMP` |  | Matches timestamp in the form of `yyyy-MM-ddTHH:mm:ss.SSSZ`. See: [DPL Time and Date](/platform/grail/dynatrace-pattern-language/log-processing-time-date) |
| `ISO8601` |  | Matches timestamp in the form of `yyyy-MM-ddTHH:mm:ssZ`. See: [DPL Time and Date](/platform/grail/dynatrace-pattern-language/log-processing-time-date) |
| `HTTPDATE` |  | Matches timestamp in the form of `dd/MMM/yyyy:HH:mm:ss Z`. See: [DPL Time and Date](/platform/grail/dynatrace-pattern-language/log-processing-time-date) |
| `BOOLEAN`, `BOOL` |  | Matches case insensitive strings `true` and `false`. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `FLOAT` |  | Matches floating point numbers. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `CFLOAT` |  | Matches floating point numbers with separator comma. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `DOUBLE` |  | Matches floating point numbers. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `CDOUBLE` |  | Matches floating point numbers with separator comma. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `INT`, `INTEGER` |  | Matches integral numbers. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `HEXINT` |  | Matches integral numbers in hexadecimal notation. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `LONG` |  | Matches integral numbers. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `HEXLONG` |  | Matches integral numbers in hexadecimal notation. See: [DPL Numeric Data](/platform/grail/dynatrace-pattern-language/log-processing-numeric) |
| `CREDITCARD` |  | Matches valid credit card numbers. See: [DPL Credit Card Data](/platform/grail/dynatrace-pattern-language/log-processing-credit-card) |
| `SMARTSCAPEID` |  | Matches and parses a Smartscape ID from a string. See: [DPL Smartscape ID](/platform/grail/dynatrace-pattern-language/log-processing-smartscape) |
| `IPADDR` |  | Matches IPv4 and IPV6 addresses. See: [DPL Network Data](/platform/grail/dynatrace-pattern-language/log-processing-network) |
| `IPV4`, `IPV4ADDR` |  | Matches IPv4 addresses. See: [DPL Network Data](/platform/grail/dynatrace-pattern-language/log-processing-network) |
| `IPV6`, `IPV6ADDR` |  | Matches IPv6 address. See: [DPL Network Data](/platform/grail/dynatrace-pattern-language/log-processing-network) |
| `STRING` |  | Matches single or double quoted strings or character groups (excluding the first 32 symbols of the ASCII table). See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `SQS` |  | Matches single quoted string. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `DQS` |  | Matches double quoted string. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `CSVSQS` |  | Matches single quoted string with csv escaping. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `CSVDQS` |  | Matches double quoted string with csv escaping. See: [DPL Lines and Strings](/platform/grail/dynatrace-pattern-language/log-processing-lines-strings) |
| `<<` |  | Look behind. See: [DPL Modifiers](/platform/grail/dynatrace-pattern-language/log-processing-modifiers) |
| `>>` |  | Look ahead. See: [DPL Modifiers](/platform/grail/dynatrace-pattern-language/log-processing-modifiers) |
| `!<<` |  | Negative look behind. See: [DPL Modifiers](/platform/grail/dynatrace-pattern-language/log-processing-modifiers) |
| `!>>` |  | Negative look ahead. See: [DPL Modifiers](/platform/grail/dynatrace-pattern-language/log-processing-modifiers) |
