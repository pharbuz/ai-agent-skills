> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-array](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-array)

# DPL Array

**ARRAY { matcher_expr … }**

The ARRAY allows parsing repeated sequences of variable number data elements, specified by a pattern supplied as an argument.

The specified pattern is applied repeatedly until:

- an unmatch occurs, or

- the maximum number of matches has been reached.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| array |  | no default value, must be explicitly set. The array can hold a maximum of 32768 elements. |  |  |

Array captures exported data elements in array data type. You must assign an export name to ARRAY to make exported members visible for the query.

#### Example

Consider data where each line has integers, separated by forward slash "/" (i.e an array), where:

- There is no separator after the last integer.

- The number of integers can be different on each line but has to be no less than 3 and no more than 5. Additionally, the integers may be omitted (missing) in the array.

```
101/102/103
201//203//205
/302/303/304

```

In the pattern, we define an ARRAY (lines 1 and 4). It matches for an integer (which can be missing since the quantifier '*' allows to match zero times) followed by a forward slash (which can also be missing by applying optional modifier '?', to match the last element of the array). The array has a quantifier expression on line 4, specifying min 3 and max 5 elements to be matched and it also assigns the export name to array expression. Out record ends with an EOL matching with line feed:

```
ARRAY{
    INT*:i
    '/'?
}{3,5}:int_array
EOL;

```

Parsing results with line 1 evaluated to an array with 3 members, line 2 array with five members and line 3 array with four members (note NULL values for missing integers).int_array`[101, 102, 103]``[201, null ,203, null, 205]``[null, 302, 303, 304]`
