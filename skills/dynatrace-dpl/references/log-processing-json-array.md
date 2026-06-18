> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-json-array](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-json-array)

# DPL JSON Arrays

**JSON_ARRAY**

[JSON syntax](https://tools.ietf.org/html/rfc8259) allows constructing arrays in a variety of ways. They can range from very simple primitive type members to very complex nested object members. A JSON array can contain members of a different type. And it is perfectly valid that they can appear also outside of a JSON object. JSON_ARRAY is meant to handle all of them.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| variant_array (default) or array (depending on `typed` configuration parameter setting) |  | none |  |  |

The easiest is to use without any parameters. It will enumerate all array elements, transform them to Log processing data types from their declared Json type and returns parsed elements as variant_array object.

#### Example

Consider the following array with different type elements:

```
[5,null,2.2,"17.9","5\u0037\u0037\u0037\u0037\u00372"]

```

Pattern:

```
JSON_ARRAY:array

```

Resulting variant_array holds all parsed array elements:namevaluetype`array[0]``5``VARIANT<LONG>``array[1]``null``VARIANT``array[2]``2.2``VARIANT<DOUBLE>``array[3]``17.9``VARIANT<STRING>``array[4]``5777772``VARIANT<STRING>`

### Controlling Output Type and Conversion

**JSON_ARRAY{ type }**

Converts all array elements to explicitly set type.

When conversion fails the entire output will be set to NULL.

Configuration parameter `typed=true` will change the output to array.

Conversion to explicit types allows you to use array expressions in accessing array elements in query statements (variant types require using casting-functions).

#### Example

```
[223423,-343.8e7,null,"3.14"]

```

Following pattern attempts converting all array elements to double, with output set to array:

```
JSON_ARRAY{ DOUBLE }(typed=true):double_arr

```

The result (double-click on the resultset row to see the details).namevaluetype`double_arr[0]``223423.0``DOUBLE``double_arr[1]``-3.438E9``DOUBLE``double_arr[2]``NULL``DOUBLE``double_arr[3]``3.14D``DOUBLE`

### Parsing Large Arrays

Sometimes you may encounter datasets, where Json formatted records are members of an array. Attempting to parse such datasets using JSON_ARRAY makes no sense because:

- you want to get records as rows in a resultset, but JSON_ARRAY returns one array object in one resultset row

- the number of records most likely exceeds the capacity of JSON_ARRAY (even when using **maxlen** configuration parameter)

Instead, you should treat such datasets as a list of JSON objects separated by a comma and ignore the square brackets of enclosing array.

It is highly recommended using JSON object semantic validation to define the array member object. This avoids unmatched objects near the border of chunks of input data.

#### Example

Consider an array with a large number of JSON objects as elements:

```
[{"id":"1","a":[3,6],"b":{"foo":"bar"}},{"id":"2","a":[30,2673,1]},{"id":"256000","a":[256,1193,2],"b":{"foo":"nobar"}}]

```

Following pattern parses Json object records by ignoring the encapsulating array.

```
(BOF '[')?
JSON_OBJECT{INT+:id}(greedy='others'):record ','?
(']' EOF)?

```

where:

1.

2.
- Matches opening square brackets at the beginning of the file. The sequence is made optional, to allow pattern match for bytes in the middle of a file.
3.

4.
- Extracts Json object to resultset field `record`, followed by a comma (optional since the last object has no trailing comma). Note that the `id` is made mandatory to avoid data loss . Other members are extracted automatically into `others` field.
5.

6.
- Matches closing brackets at the end of a file. The sequence is made optional, to allow pattern match for bytes in the middle of a file.
7.

Result:record`{id=1 others={'a':[3,6],'b':{'foo':'bar'}}}``{id=2 others={'a':[30,2673,1]}}`…`{id=256000 others={'a':[256,1193,2],'b':{'foo':'nobar'}}}`

Log processing splits input data into 64Mb chunks and processes them in parallel. To guarantee non-duplication of parsed fields the pattern must match the smallest size of data block within its maximum length. I.e - a pattern which matches data block of certain size must not match a smaller data block inside it.

This condition is almost always satisfied, except when JSON is used **in automatic extraction mode**, either alone (when parsing concatenated_json) or with optional matchers (comma-separated list of JSON objects). Then the pattern may also match embedded objects within a JSON object.

To avoid this happening use JSON object semantic validation - to distinguish the largest extracted JSON object from its embedded objects, declare a minimum set of its top-level members as mandatory. The rest of the members can be extracted automatically by specifying `greedy` parameter to JSON matcher. See the example above.
