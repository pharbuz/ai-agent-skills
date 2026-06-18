> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/ordering-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/ordering-commands)

# DQL ordering commands

## limit

Limits the number of returned records.

If you do not specify the limit, the query renders 1000 results (this limit, by default, is appended as the last line of the query).

You can increase or decrease the limit depending on your needs. Changing the limit has an impact on your DDU consumption and query execution time.

#### Syntax

`limit numberOfQueryRecords`

#### Basic example

##### Example: Query three records

The following query uses the `limit` command to limit the result to three records.

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| limit 3

```

Query result:a`2``3``7`

#### Practical example

##### Example: Query up to five logs

The following query uses the [fetch](/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch) command to load data from `logs`.
Up to one thousand log records are returned by default, but the `limit` command limits the result to five records.

```
fetch logs
| limit 5

```

## sort

Sorts the records. When using the `sort` command, the default sorting order is ascending. You can control the order in which your records are displayed by adding `asc` for ascending and `desc` for descending. Sorting is case-sensitive, which means that inputs beginning with capital letters (for example, `K`) are listed before those beginning with lowercase (for example, `d`).

#### Syntax

`sort fieldname [asc | desc][, ...]`

#### Basic examples

##### Example 1: Sort result by one field

The following query uses the `sort` command to sort the result by field `a`.

```
data record(a = 2),
     record(a = 3),
     record(a = 7),
     record(a = 7),
     record(a = 1)
| sort a

```

Query result:a`1``2``3``7``7`

##### Example 2: Sort result by multiple fields

The following query uses the `sort` command to sort the result by field `a` descending and field `b` ascending.

```
data record(a = 2),
     record(a = 3),
     record(a = 7, b = 2),
     record(a = 7, b = 1),
     record(a = 1)
| sort a desc, b asc

```

Query result:ab`7``1``7``2``3`*null*`2`*null*`1`*null*

#### Practical example

##### Example: Sort business events by two fields

The following query uses the [fetch](/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch) command to query business events. The `sort` command sorts the records by `timestamp` descending. If there are records with the same timestamp, they are sorted by `event.type` ascending.

```
fetch bizevents
| sort timestamp desc, event.type asc

```

#### Sorting heterogeneous data

Sorting by fields with heterogeneous data sorts the records primarily based on the data type of the field in each record in the following ascending order: `boolean`, `long` and `double`, `binary`, `string`, `timestamp`, `duration`, `timeframe`, `uid`, `ip`, `array`, `record`. `Long` and `double` are considered equivalent in the sorting by data type. This also means that for equal numeric (`long` or `double`) values the order of the records in the input is preserved in the output of the `sort` command.

##### Example: Sort results by one field containing heterogeneous data

The following query sorts the records by field `a`, where the field can be of different [data types](/platform/grail/dynatrace-query-language/data-types).

```
data record(a = "6"),
     record(a = 7.0),
     record(a = 7),
     record(a = 0),
     record(a = 0.0),
     record(a = ip("1.1.1.1")),
     record(a = record(b = 1)),
     record(a = array(0, 1, 2)),
     record(a = now()),
     record(a = array()),
     record(),
     record(a = toUid(1)),
     record(a = timeframe(now() - 5m, to: now())),
     record(a = duration(5, "d")),
     record(a = decodeBase64ToBinary(encodeBase64("A"))),
     record(a = true)
| sort a asc
| fieldsAdd type(a)

```

Query result:atype(a)`true``boolean``0``long``0``double``7``double``7``long``QQ==``binary``6``string``2024-02-22T09:55:18.354Z``timestamp``5 d``duration`**start**: `2024-02-22T09:50:18.354Z`
**end**: `2024-02-22T09:55:18.354Z``timeframe``0000000000000001``uid``1.1.1.1``ip``[ ]``array``[0, 1, 2]``array`**b**: `1``record`*null**null*
