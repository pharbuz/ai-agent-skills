> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-smartscape](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-smartscape)

# DPL Smartscape ID

**SMARTSCAPEID**

The SMARTSCAPEID matches a string representation of a Smartscape ID and creates a Smartscape ID parser.

The matcher identifies the patterns that consist of:

- A string from 1 to 255 symbols long. Accepted symbols: `A-Za-z_:0-9`.

- A dash `-`.

- A numeric hexadecimal that must be 16 symbols long.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| SMARTSCAPEID |  | none |  | none |

### Example

```
There is a CONTAINER-00009B6550330A1F Smartscape ID in this text.

```

Pattern:

```
LD SMARTSCAPEID:SmartscapeId

```

Parsing results: a Smartscape ID parsed from the string.

| SmatscapeId |  | CONTAINER-00009B6550330A1F |
| --- | --- | --- |
