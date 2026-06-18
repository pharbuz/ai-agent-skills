> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands)

# DQL correlation and join commands

## append

Appends a given list of records by the records returned by a sub-query. It doesn't change the fields of the original records and does not remove duplicate records. The behavior of the `append` command is similar to the SQL **UNION ALL** operation.

#### Syntax

`append executionBlock`

#### Basic example

##### Example: Append records

The following example appends a set of records to an existing set of records.

```
data record(a = 2),
     record(a = 7)
| append [
      data record(a = 3),
           record(a = 7)
    ]

```

Query result:

| a |
| --- |
| `2` |
| `7` |
| `3` |
| `7` |

#### Practical example

##### Example: Garbage collection and warning logs

In this example, the `append` command is used to combine metric and log data.
The query shows the garbage collection and the number of warning logs for a given host.

```
timeseries gctime = sum(dt.runtime.jvm.pgi.cpu_time_suspension),
  filter: dt.entity.host == "HOST-84D65AF93A3C185A"
| fields total_gc = arraySum(gctime)
| append [
      fetch logs
      | filter dt.entity.host == "HOST-84D65AF93A3C185A" and loglevel == "WARN"
      | summarize warnings = count()
    ]

```

## join

The join command merges the records of two tables and forms a new table by matching records from each table.

DQL offers three kinds of joins that each affect the rows in the resultant table in different ways:

- The **inner join**, which represents the default behavior of the DQL join, produces an output record whenever a record on the left side matches a record on the right side based on the join condition.

- The **leftOuter join** returns all the records from the left side and only matching records from the right side. In case of no match, the left side's record will remain.

- The **outer join** returns matched and unmatched records from either or both sides.

#### Syntax

`join joinTable [, kind] , on: condition, … [, prefix] [, fields: { [field, …] }] [, executionOrder]`

The join condition is formed from one or more criteria, where each criterion is an equality condition that links two fields, one from each side.

If the join field name is identical on the left and right sides, the join criterion is defined as follows:

`.. | join [...] on:id`

If the join field name differs between the left side and right side:

`.. | join [...] on:left[dt.entity.host] == right[id]`

The join command supports more complex join conditions by chaining multiple criteria in a comma-separated list.

`.. | join [...] on:{left[service.id] == right[id], left[cloudType] == right[cloud]  , dt.entity.host}`

Each criterion is combined using AND boolean logic. This requires all criteria to be met in order to match records from both sides.

When key values on the right and left side of the query are both `null`, corresponding records aren't matched.

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | joinTable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The sub-query producing the right side. |  |  |  |  |  |  |  |  |
| kind |  |  |  |  |  |  |  |  |
| Specifies the join kind. The default is `inner`. Possible options are `inner`, `outer` and `leftOuter`. |  |  |  |  |  |  |  |  |
| on |  |  |  |  |  |  |  |  |
| The join condition. |  |  |  |  |  |  |  |  |
| prefix |  |  |  |  |  |  |  |  |
| The prefix to add to the joined fields. If not specified, the default prefix is `right`. |  |  |  |  |  |  |  |  |
| fields |  |  |  |  |  |  |  |  |
| A field from the subquery to add to the input. |  |  |  |  |  |  |  |  |
| executionOrder |  |  |  |  |  |  |  |  |
| Defines which side of the join will be executed first. The allowed values are `auto`, `leftFirst`, `rightFirst`. The default value is `auto`. |  |  |  |  |  |  |  |  |

#### Basic examples

##### Example 1: Inner join

Returns all known fields from both tables, including the fields mentioned in the join condition. Only the matching records from both tables are returned.

```
data record(key = "a", value = 1),
     record(key = "b", value = 2),
     record(key = "c", value = 4)
| join [
      data record(key = "b", amount = 10),
           record(key = "c", amount = 20),
           record(key = "c", amount = 40),
           record(key = "d", amount = 50)
    ],
    on: { key }

```

Query result:

| key |
| --- |
| value |
| right.key |
| right.amount |
| `b` |
| `2` |
| `b` |
| `10` |
| `c` |
| `4` |
| `c` |
| `20` |
| `c` |
| `4` |
| `c` |
| `40` |

##### Example 2: Left outer join

Returns all known fields from both tables, including the fields mentioned in the join condition. All records from the left side plus matching records from the right side are returned.

```
data record(key = "a", value = 1),
     record(key = "b", value = 2),
     record(key = "c", value = 4)
| join [
      data record(key = "b", amount = 10),
           record(key = "c", amount = 20),
           record(key = "c", amount = 40),
           record(key = "d", amount = 50)

    ],
    kind: leftOuter,
    on: { key }

```

Query result:

| key |
| --- |
| value |
| right.key |
| right.amount |
| `a` |
| `1` |
| *null* |
| *null* |
| `b` |
| `2` |
| `b` |
| `10` |
| `c` |
| `4` |
| `c` |
| `20` |
| `c` |
| `4` |
| `c` |
| `40` |

##### Example 3: Outer join

Returns the matching records from the left and right side as combined records and also the non matching records from both sides.

```
data record(key = "a", value = 1),
     record(key = "b", value = 2),
     record(key = "c", value = 4)
| join [
      data record(key = "b", amount = 10),
           record(key = "c", amount = 20),
           record(key = "c", amount = 40),
           record(key = "d", amount = 50)
    ],
    on: { key },
    kind: outer

```

Query result:

| key |
| --- |
| value |
| right.key |
| right.amount |
| `a` |
| `1` |
| *null* |
| *null* |
| `b` |
| `2` |
| `b` |
| `10` |
| `c` |
| `4` |
| `c` |
| `20` |
| `c` |
| `4` |
| `c` |
| `40` |
| *null* |
| *null* |
| `d` |
| `50` |

#### Practical example

##### Example: Ingested business events by host name

The following example shows the number of ingested business events by host name.
The host name is retrieved with the help of the `join` command.

```
fetch bizevents
| filter event.provider == "www.easytrade.com"
| summarize count = count(),
    by: { dt.entity.host }
| join [ fetch dt.entity.host ],
    on: { left[dt.entity.host] == right[id] },
    fields: { host.name = entity.name }
| fields host.name, count

```

#### Usage and best practices

- Use the smallest dataset on the right side.

- Use the inner join if applicable.

- Select fields in the join subquery.

- Filter the right side's dataset in the join subquery.

#### Limits

In general, the right side's result size limit is 128 MB. If the limit is exceeded, the DQL query fails. To resolve this issue, reduce the right side's result set by filtering or aggregating the result set on the right side.

If the left side is expected to produce a smaller result size than the right side, set the `executionOrder` parameter to `leftFirst`. For inner and outer join, the size limit applies then to the left side. In case of an outerLeft join the result set from the left side, if executed first, can be used for additional filtering of the right side's result set to further reduce it.

##### Example: Changing join execution order

In this query, the left side produces only 100 rows from `bizevents`. However, the `logs` queried on the right side can potentially generate a large number of rows, which might exceed the size limit of a join table and cause the query to fail. By utilizing the `leftFirst` approach, we execute the smaller part first and then use it for the join operation.

```
fetch bizevents
| filter event.provider == "www.easytrade.com"
| limit 100
| join [ fetch logs ],
    kind: leftOuter,
    on: { trace_id },
    executionOrder: leftFirst,
    fields: { log.timestamp = timestamp, content }
| fieldsAdd timestamp.diff = timestamp - log.timestamp

```

## joinNested

Adds matching results from the sub-query as an array of nested records.
The `joinNested` command functions as a variant of the `join` command, specifically utilizing the `leftOuter` type. Instead of replicating matching records, it incorporates the list of matching records into a newly added field on the left side.

#### Syntax

`joinNested alias = joinTable [, on: condition, …] [, fields: { [field, …] }]  [, executionOrder:]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | joinTable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The sub-query producing the right side. |  |  |  |  |  |  |  |  |
| on |  |  |  |  |  |  |  |  |
| Records must match this condition in order to be joined. |  |  |  |  |  |  |  |  |
| fields |  |  |  |  |  |  |  |  |
| The fields from the sub-query to add to the source. |  |  |  |  |  |  |  |  |
| executionOrder |  |  |  |  |  |  |  |  |
| Defines which side of the join will be executed first. The allowed values are `auto`, `leftFirst`, `rightFirst`. The default value is `auto`. |  |  |  |  |  |  |  |  |

#### Basic examples

##### Example 1: Simple nested join

The `joinNested` command adds a new `nestedRecords` field to every record of the left side of the join. A `nestedRecords` field is an array of matching records of the left side of the join.

```
data record(key = "a", value = 1),
     record(key = "b", value = 2),
     record(key = "c", value = 4)
| joinNested nestedRecords = [
      data record(key = "b", amount = 10),
           record(key = "c", amount = 20),
           record(key = "c", amount = 40),
           record(key = "d", amount = 50)
    ],
    on: { key }

```

Query result:

| key |
| --- |
| value |
| nestedRecords |
| `a` |
| `1` |
| *null* |
| `b` |
| `2` |
| [**key:** `b` **amount:** `10`] |
| `c` |
| `4` |
| [**key:** `c` **amount:** `20`, **key:** `c` **amount:** `40`] |

##### Example 2: Nested join with custom fields

The `joinNested` command adds only those fields, that are specified in the `fields` parameter, into the `nestedRecords` field.

```
data record(key = "a", value = 1),
     record(key = "b", value = 2),
     record(key = "c", value = 4)
| joinNested nestedRecords = [
      data record(key = "b", amount = 10),
           record(key = "c", amount = 20),
           record(key = "c", amount = 40),
           record(key = "d", amount = 50)
    ],
    on: { key },
    fields: { amount }

```

Query result:

| key |
| --- |
| value |
| nestedRecords |
| `a` |
| `1` |
| *null* |
| `b` |
| `2` |
| [**amount:** `10`] |
| `c` |
| `4` |
| [**amount:** `20`, **amount:** `40`] |

#### Practical example

##### Example: Process groups and their services

In the following example, the `joinNested` command adds the field `services` to every record. That new field contains a list of all service IDs and service names running on that process group.

```
fetch dt.entity.process_group
| joinNested services = [
      fetch dt.entity.service
      | fieldsAdd dt.entity.process_group = runs_on[dt.entity.process_group]
    ],
    on: { left[id] == right[dt.entity.process_group] },
    fields: { id, name = entity.name }

```

#### Limits

The same [limits](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join-limits) as described for the `join` command apply.

## lookup

Adds (joins) fields from a subquery (the lookup table) to the source table by finding a match between a field in the source table (`sourceField`) and the lookup table (`lookupField`). In case the lookup command finds more than one match in the lookup table, only the top result is retrieved (the first matching record). When key values in the source and lookup table are both `null`, corresponding records aren't matched.

#### Syntax

`lookup lookupTable [, sourceField] [, lookupField] [, prefix] [, fields: { [field, …] }] [, executionOrder]`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | sourceField |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The matching field on the source table (left side). |  |  |  |  |  |  |  |  |
| lookupField |  |  |  |  |  |  |  |  |
| The matching field on the lookup table (right side). |  |  |  |  |  |  |  |  |
| prefix |  |  |  |  |  |  |  |  |
| The prefix to add to the joined fields. If not specified, the default prefix is `lookup.` |  |  |  |  |  |  |  |  |
| fields |  |  |  |  |  |  |  |  |
| A field from the subquery to add to the input. |  |  |  |  |  |  |  |  |
| executionOrder |  |  |  |  |  |  |  |  |
| Defines which side of the join will be executed first. The allowed values are `auto`, `leftFirst`, `rightFirst`. The default value is `auto`. |  |  |  |  |  |  |  |  |

#### Basic example

##### Example: Lookup names to records

The following example uses the `lookup` command to join names from the subquery to the source table.

```
data record(key = "a", value = 1),
     record(key = "b", value = 2),
     record(key = "c", value = 4)
| lookup [
      data record(key = "b", amount = 10),
           record(key = "c", amount = 20),
           record(key = "c", amount = 40),
           record(key = "d", amount = 50)
    ],
    sourceField: key,
    lookupField: key,
    prefix: "lookuptable."

```

Query result:

| key |
| --- |
| value |
| lookuptable.key |
| lookuptable.amount |
| `a` |
| `1` |
| *null* |
| *null* |
| `b` |
| `2` |
| `b` |
| `10` |
| `c` |
| `4` |
| `c` |
| `20` |

#### Practical examples

##### Example 1: Lookup cluster name to log

The following example uses the `lookup` command to query the Kubernetes cluster name and add it to logs.

```
fetch logs
| filter isNotNull(dt.entity.kubernetes_cluster)
| lookup [ fetch dt.entity.kubernetes_cluster ],
    sourceField: dt.entity.kubernetes_cluster,
    lookupField: id,
    fields: { cluster.name = entity.name }

```

##### Example 2: Nested field as join condition

You can include nested fields in your queries as `sourceField` or `lookupField`. Nested fields can only come from inside a record and not from an array.

```
fetch dt.entity.service_instance
| lookup [ fetch dt.entity.host ],
    sourceField: runs_on[dt.entity.host],
    lookupField: id,
    fields: { host.name = entity.name }

```

#### Lookup as a function

You can also use `lookup` as a function to perform a lookup. In contrast to the `lookup` command, the `lookup` function nests all included fields as a record.
For further details, go to the [lookup](/platform/grail/dynatrace-query-language/functions/join-functions#lookup) function documentation.

#### Limits

The same [limits](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join-limits) as described for the `join` command apply.
