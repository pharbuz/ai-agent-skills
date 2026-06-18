> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-sequence-group](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-sequence-group)

# DPL Sequence Group

**'(' matcher_expr … ')'**

A sequence group glues matcher expressions together - i.e for a sequence group to match, all its members must match.

Sequence group member matching results are not visible outside of the group - i.e for other matcher expressions in a pattern only the resulting group matching result is visible.

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | none |  |  |

Sequence group is used when you want to match a subpattern independently of surrounding data elements, typically when performing conditional matching using matcherdef-ldata, matcherdef-data or with lookarounds.

#### Example

Parsing multiline records separated by an empty line (i.e a sequence of two consecutive line-feed characters). Suppose we have two records: one represented by strings in lines 1-3 and other on line 5:

```
aaaaaaaa
bbbbbbbb
cccccccc

dddddddd

```

To extract records as strings we need to use matcherdef-data to match strings until we encounter two consecutive line-feeds. If we do not enclose them in sequence group then matcherdef-data will consume all characters until it encounters first line-feed. The engine continues to look match for next line-feed but as it finds beginning character "b" of string on line 2, it will consider parsing failed and continue from the beginning of pattern again. As a result, only line 3 and line 5 will be extracted - not as we expected.

```
DATA:record EOL EOL;

```

record`NULL``cccccc``dddddd`

By simply enclosing two EOL expressions (matching line-feeds) in the sequence group changes the behavior to intended: now the matcherdef-data stops matching only when two consecutive line-feeds appears:

```
DATA:record (EOL EOL);

```

record`aaaaaa\\nbbbbb\\ncccccc``dddddd`

The sequence group should be used also in cases when data elements are expected to be present of absent collectively.

#### Example

Consider a simplified DNS server request log, consisting of timestamp, question, and optional DNS server IP-address enclosed in parenthesis. Suppose that the latter appears only when enabled in the server configuration (as it happens to be with BIND9), hence some logs may not have it:

```
2016-03-14 23:37:07;www.example.com (192.168.0.1)
2016-03-14 23:37:06;www.example.com

```

As the server is present or omitted together with enclosing parenthesis, we can use the sequence group to make them all optional:

```
TIMESTAMP:datetime ';'
LD:question
( '(' IPADDR:server ')' )?
EOL

```

Parsing results with matcherdef-data field evaluated to 192.168.0.1 for data in line 1 and NULL for data in line 2:datetimequestionserver`2016-03-14 23:37:07``www.example.com``192.168.0.1``2016-03-14 23:37:07``www.example.com``NULL`

When dealing with delimiter separated fields (such as CSV), the sequence group allows writing patterns in a more readable way. The sequence group recognizes and matches field separators defined by **fs** configuration parameter.

#### Example

Consider the following CSV fields: a sequence number, a username, and an ip-address.

```
1,alice,192.168.1.1
2,bob,10.6.24.18
3,mallory,192.168.1.3

```

We can extract these using the following pattern:

```
(
 INT:sequence
 LD:username
 IPADDR:ip
)(fs=',')
EOL

```

sequenceusernameip`1``alice``192.168.1.1``2``bob``10.6.24.18``3``mallory``192.168.1.3`
