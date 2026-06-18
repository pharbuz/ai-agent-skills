> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-enum](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-enum)

# DPL Enum

**ENUM { string=integer , … }**

Enum constructor allows matching for a set of predefined strings and converts them into respectively assigned integer values. The strings and respective integer values are declared as series of key-value pairs, separated by commas and enclosed in curly brackets.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| integer |  | none |  |  |

#### Example 23.

Suppose we have data with username, login result and comment fields:

```
Alice;success;all good
Bob;Wrong password;attempts left 2
Oscar;tech error;
Mallory;;doodaloo

```

Pattern. Line 3 maps login result strings (case-insensitively) to integer values:

```
LD:username ';'
ENUM{''=-3, 'success'=0, 'Wrong password'=1, 'tech error'=2}(cis=true):result ';'
LD*:comment
EOL;

```

Result:usernameresultcomment`Alice``0``all good``Bob``1``attempts left 2``Oscar``2``Mallory``-3``doodaloo`
