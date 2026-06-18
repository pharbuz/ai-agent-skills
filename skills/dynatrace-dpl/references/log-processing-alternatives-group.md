> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-alternatives-group](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-alternatives-group)

# DPL Alternatives Group

**( matcher_expr | matcher_expr | … )**

Alternatives group applies matcher expressions in the order they are defined (from left to right). It stops at the first match found (i.e it uses so-called lazy match strategy) and its value is extracted (if the expression has an export name assigned). Other exported matcher fields in resultset will be assigned to NULL.

When alternatives group itself is exported, then its field will have matching member value converted to string (or the empty string if none matched).

| output type |  | quantifier |  | configuration |
| --- | --- | --- | --- | --- |
| string |  | not allowed |  |  |

Alternatives group comes handy when data in the same position may be of a different type. A good example is Apache webserver access log where the first field in the record may be an IP-address or hostname.

#### Example

Parsing an IP-address or hostname:

```
192.168.1.1
www.example.com

```

Pattern:

```
(IPADDR:ip | LD:host):alt_grp EOL;

```

Parsing results in ipaddr field `ip` being evaluated to 192.168.1.1 for data on line 1 and NULL for the line 2. string field `host` is evaluated oppositely. The string field `alt_grp`, exported by alternative group, has non-NULL value for data in both lines.iphostalt_grp`192.168.1.1``NULL``192.168.1.1``NULL``www.example.com``www.example.com`
