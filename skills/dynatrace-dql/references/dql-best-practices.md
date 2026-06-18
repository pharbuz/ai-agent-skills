> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-best-practices](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-best-practices)

# DQL best practices

This page describes actions you can take to improve query performance.

### Narrow the query time range

A shorter analysis window provides better performance based on identical data sets. Use available timeframe selectors provided by the user interface or directly specify the query time range within the [fetch command](/platform/grail/dynatrace-query-language/commands).

```
fetch bizevents, from:-10m

```

### Utilize available sampling options

Grail samples incoming data on write and allows the selection of these partitions within the DQL [fetch command](/platform/grail/dynatrace-query-language/commands). Depending on the specified value, a fraction (`1/<samplingRatio>`) of all available raw records is returned.

The applicable value ranges for sampling are:

- 1: Default value, resulting in no applied sampling.

- 10

- 100

- 1000

- 10000

The following query uses sampling to improve query performance to observe an approximation of the number of spans per function invocation.

```
fetch spans, samplingRatio:100
| summarize c=count(), by: { span.kind, code.namespace, code.function }
| fieldsAdd c = c*100

```

### Further options to limit the scanned amount of data

The DQL [fetch command](/platform/grail/dynatrace-query-language/commands) provides further options to limit data processing by

- stopping processing after a specified amount of data

```
fetch logs, scanLimitGBytes:100

```

- filtering on specific Grail Buckets

```
fetch logs, bucket:{"default_logs", "logs_365_*"}

```

### Recommended order of commands

Recommended order of commands

1.

2.
- Reduce the number of processed records by filtering the data using, for example, the `filter` or `search` commands.

- Try avoiding transformations like `| filter matchesValue(lower(k8s.namespace.name), "astro*")` and filter directly on the field such as: `| filter k8s.namespace.name ~ "astro*"`.

- Try matching against words or phrases for text searches using `| filter content ~ "refused"`

- Try to use inclusive filters and avoid negations such as `| filter not k8s.namespace.name ~ "astro*"`

- Avoid `join` and `lookup` for filtering unless necessary. Filtering on enriched fields is suggested.

3.

4.
- Select the amount of processed data by selecting fields early using the `fields`, `fieldsKeep`, or `fieldsRemove` commands.
5.

6.
- Process the resulting dataset to achieve the required result set. Typically, non-transformative commands are used, such as `fieldsAdd`, `parse`, `append`.
7.

8.
- Aggregate your data set using the `summarize` command to create a tabular result and `maketimeseries` if a time chart is required. Don't use `limit` before aggregating the data to prevent wrong aggregates unless intended.
9.

**Example**

Applying the mentioned practices above leads to the following blueprint:

```
fetch logs, bucket:{"astroshop_log_*"}, from:-1d@d, samplingRatio:10
| filter loglevel=="ERROR" and k8s.namespace.name ~ "astroshop"
| filter content ~ "error"
| summarize c=count(), by:pod.name
| sort c desc
| limit 5

```

It is recommended to place `sort` at the end of the query. Sorting right after `fetch`, and continuing the query will reduce the query performance.

**Examples**

This example shows a query, where we put `sort` right after `fetch`.

It is recommended to place `sort` at the end of the query. Sorting right after `fetch` and then continuing the query will reduce the query performance. Example:

```
fetch logs
| sort timestamp desc
| filter content ~ "error"

```

This example shows the recommended order of putting `sort` at the end of the query.

```
fetch logs
| filter content ~ "error"
| sort timestamp desc

```

You can repeat the same command within one query and still stick to the recommended order. In the below example, you first filter the fetched content, then again you filter the parsed content, but the `sort` command and `summarize` function retain their positions:

```
fetch logs, bucket:{"astroshop_log_*"}, from:-1d@d, samplingRatio:10
| filter loglevel == "ERROR" and k8s.namespace.name ~ "astroshop"
| parse content, "ipaddr:ip ld ' POST ' ld:action ' HTTP/1.1 ' long:status ld"
| filter action == "/cart" or action == "/cart/checkout"
| summarize count = count(), by:{ ip, log.source }
| sort count desc

```

### Use string comparisons with care

-

Use `==` or `!=` whenever the value of a field is known.

```
fetch logs
| filter k8s.container.name == "coredns"

```

-

Use `~` whenever the value of a field is only partly known or unknown.

```
fetch logs
| filter k8s.container.name ~ "core*"

```

### Fields names to be avoided or used in backticks

It is not recommended to use the below eight reserved keywords as field identifiers (field names) or dimensions:

- true

- false

- null

- mod

- and

- or

- xor

- not

However, you can still use these words as field names, identifiers and dimensions if you put them in backticks ('`')

For example, if you have a dimension named 'true':

```
...
| fields x = true // creates a boolean field that is always true

```

```
...
| fields x = `true` // allows to access the custom dimension named 'true'

```

Similarly, if you need to sort by a field named 'not':

```
...
| sort not desc // sorts by a boolean value of dimension `desc`

```

```
...
| sort `not` desc // sorts descending by a field named `not`

```
