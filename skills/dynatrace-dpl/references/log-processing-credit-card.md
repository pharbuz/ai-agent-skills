> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-credit-card](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-credit-card)

# DPL Credit Card Data

Matches valid credit card numbers (i.e with valid Luhn checksum) in all varieties: lengths (depending on the credit card scheme), formattings (continuous, space-delimited), encodings (when submitted in the URL).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| long |  | none |  | none |

### Example

```
378282246310005
3782 822463 10005
38520000023236
4917%206100%200000%200000%20003

```

Pattern:

```
CREDITCARD:cc EOL;

```

Parsing results creditcard numbers in lines 1,2 and 4 parsed into long field `cc`. Parsing fails for line 3 due to invalid Luhn check digit.cc`378282246310005``378282246310005``NULL``4917610000000000003`
