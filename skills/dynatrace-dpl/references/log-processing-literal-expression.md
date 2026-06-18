> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-literal-expression](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-literal-expression)

# DPL Literal Expressions

**"…" or '...'**

Literals are expressed as strings enclosed in single or double-quotes.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| String |  | default value: `{1,1}` - requires matching minimum 1 and maximum 1 times |  |  |

In case the constant contains a single quote or double quote you may either use the other for enclosing (i.e: use double quotes for enclosing if the string contains a single quote or vice versa).

Alternatively, you can escape it with a preceding backslash character `\` (0x5c ASCII).

Constants are usually less interest for analytical purposes, hence in most cases, they are just matched - i.e values not exported for the query.

#### Example

Matching one or more characters 'a'.

```
a
aa

```

Pattern:

```
"a"+ EOL

```
