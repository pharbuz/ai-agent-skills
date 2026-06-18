> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-structure](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-structure)

# DPL Structure

**STRUCTURE { matcher_expr … }**

The STRUCTURE allows capturing any sequence of matchers in tuple data type.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| tuple |  | none |  | none |

You must assign an export name to STRUCTURE to make exported members visible for the query layer.

#### Example

Consider the following data, where we have an integer and string value, separated by a comma on each line:

```
1,red fox jumps
2,over lazy dog

```

Pattern:

```
STRUCTURE{ INT:i ',' LD:string }:struct EOL;

```

Parsing results with integer and string values extracted:struct`{i=1 string='red fox jumps '}``{i=2 string='over lazy dog'}`
