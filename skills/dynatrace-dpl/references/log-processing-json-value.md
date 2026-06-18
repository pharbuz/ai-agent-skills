> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-json-value](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-json-value)

# DPL JSON Values

**JSON_VALUE**

Parses JSON elements like an array, string, number, boolean, null which are not enclosed in a JSON object. This is perfectly valid and allowed by [JSON Grammar](https://tools.ietf.org/html/rfc8259#page-5)).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| variant (default) or explicitly selected conversion type |  | none |  |  |

#### Example

Here we have two JSON values in separate lines: a number and a string.

```
33
"::1"

```

The number on line 1 is parsed automatically. The string on line 2 is explicitly converted to ipaddr:

```
JSON_VALUE{}:auto EOL JSON_VALUE{IPADDR}:ip

```

Here's the result (double-click on the resultset row to see the details):namevaluetype`auto``33``VARIANT<LONG>``ip``::1``IPADDR`
