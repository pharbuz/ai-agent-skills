> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-key-value-pairs](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-key-value-pairs)

# DPL Key-Value Pairs

**KVP{ matcher_expr … }**

Parses a list of unordered, variable-length key-value pairs according to the supplied pattern.

The pattern must export the following fields:

- one field named `key`

- one or more fields, with the name beginning with `value`

The specified pattern is applied repeatedly until:

- an unmatch occurs, or

- the maximum number of matches has been reached.

The pattern should describe the **whole** sequence of key-value pairs: i.e the matchers for the key and value, the separator between key and value, as well as separator between the pairs. Special attention must be paid for matching the last key-value pair - usually, it is not followed by a separator.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| default 128, max 32768 key-value pairs. |  |  |  |  |

#### Example

Parsing simple key-value pairs, separated by single space. Key names consist of single lowercase letter and all values are integer numbers.

```
a=1 b=2
a=4 b=8

```

Pattern:

```
KVP{
 [a-z]:key    //key consists of single lowercase letter and
 '='          //is followed by separator '='
 INT:value    //value is integer
 ' '?         //followed by single space, except after last pair (hence optional modifier applied)
}:attr        //export resulting VARIABLE_OBJECT structure under name 'attr'
EOL           //record ends with line break

```

Note that the last pair on the line does not have trailing space. To match we must declare the space separating the pairs as optional. After the last pair is matched the next iteration encounters unmatch (line feed is not matching our key definition), hence KVP stops matching and the engine continues with next matcher in the pattern - the EOL. This matches our line break and the record is complete.

Result (double-click on the resultset row to see the details):attr`{"a":1,"b":2}``{"a":4,"b":8}`
