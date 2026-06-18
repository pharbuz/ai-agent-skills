> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/filtering-commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/filtering-commands)

# DQL filter and search commands

## dedup

Removes duplicates from a list of records.

You can use multiple field names or expressions for deduplication. The output of the `dedup` command will have the same number of records as there are unique combinations in the given fields or expressions.

The original order of the records is not preserved. Therefore, by default the sequence of records that are chosen during deduplication is random. If you want to pick a particular record out of the duplicates, you can use the sort parameter.

The count of records following the `dedup` command will be identical to the count of records following the `summarize` command. The `summarize` command groups together records with the same values for a given field and aggregates them, whereas `dedup` removes duplicate values from a list of records.

#### Syntax

`dedup expr, [expr...], [sort:expr [asc|desc], [....expr [asc|desc]]]`

#### Basic examples

##### Example 1: Show all locations

In the following example, the input for the `dedup` command are records that show the number of bookings and their locations historically. The `dedup` command removes duplicate records based on the field location and keeps a random record per unique location.

```
data record(timestamp = 1, location = "Vienna", bookings = 1254),
     record(timestamp = 1, location = "London", bookings = 4564),
     record(timestamp = 2, location = "Vienna", bookings = 1457),
     record(timestamp = 2, location = "London", bookings = 8741),
     record(timestamp = 3, location = "Vienna", bookings = 1654)
| dedup location

```

Query result:

| timestamp |
| --- |
| location |
| bookings |
| `1` |
| `London` |
| `4,564` |
| `1` |
| `Vienna` |
| `1,254` |

##### Example 2: Bookings per location

In the following example, the input for the `dedup` command are records that show the number of bookings and their locations historically. The `dedup` command removes duplicate records based on the field location and for each location keeps the record with the latest timestamp.

```
data record(timestamp = 1, location = "Vienna", bookings = 1254),
     record(timestamp = 1, location = "London", bookings = 4564),
     record(timestamp = 2, location = "Vienna", bookings = 1457),
     record(timestamp = 2, location = "London", bookings = 8741),
     record(timestamp = 3, location = "Vienna", bookings = 1654)
| dedup location, sort: { timestamp desc }

```

Query result:

| timestamp |
| --- |
| location |
| bookings |
| `2` |
| `London` |
| `8,741` |
| `3` |
| `Vienna` |
| `1,654` |

##### Example 3: Bookings over time

In the following example, the input for the `dedup` command are records that show the number of bookings and their locations historically. The `dedup` command removes duplicate records based on the fields timestamp and location and per unique combination keeps the record with the largest value in the bookings field.

```
data record(timestamp = 1, location = "Vienna", bookings = 1254),
     record(timestamp = 1, location = "London", bookings = 4553),
     record(timestamp = 1, location = "London", bookings = 4564),
     record(timestamp = 2, location = "Vienna", bookings = 1451),
     record(timestamp = 2, location = "Vienna", bookings = 1457),
     record(timestamp = 2, location = "London", bookings = 8741)
| dedup { timestamp, location }, sort: { bookings desc }

```

Query result:

| timestamp |
| --- |
| location |
| bookings |
| `1` |
| `London` |
| `4,564` |
| `1` |
| `Vienna` |
| `1,254` |
| `2` |
| `London` |
| `8,741` |
| `2` |
| `Vienna` |
| `1,457` |

#### Practical example

##### Example: List currently open vulnerabilities

The following example shows the currently open vulnerabilities. Because vulnerabilities are stored as snapshot, the `dedup` command is used to retrieve the most recent snapshot of a vulnerability.

The query below has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/secure/threat-observability/migration).

```
fetch security.events
| filter event.provider == "Dynatrace"
| filter event.type == "VULNERABILITY_STATE_REPORT_EVENT"
| filter event.level== "VULNERABILITY"
| filter vulnerability.resolution.status == "OPEN"
| filter vulnerability.mute.status != "MUTED"
| dedup vulnerability.display_id, sort: { timestamp desc }

```

## filter

Reduces the number of records in a list by keeping only those records that match the specified condition.

#### Syntax

`filter condition [, input]`

#### Basic examples

##### Example 1: Filter on one condition

The following query uses the `filter` command to filter on the field `event`.

```
data record(event = "search failed", prodId = 5, qty = 6, host = "A"),
     record(event = "product found", prodId = 3, qty = 3, host = "A"),
     record(event = "search failed", prodId = 4, qty = 7, host = "B"),
     record(event = "search failed", prodId = 2, qty = 7, host = "C")
| filter event == "search failed"

```

Query result:

| event |
| --- |
| prodId |
| qty |
| host |
| `search failed` |
| `5` |
| `6` |
| `A` |
| `search failed` |
| `4` |
| `7` |
| `B` |
| `search failed` |
| `2` |
| `7` |
| `C` |

##### Example 2: Filter on multiple conditions

The following query uses the `filter` command to filter records based on evaluating multiple conditions.
[Logical operators](/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators) connect the conditions.

```
data record(event = "search failed", prodId = 5, qty = 6, host = "A"),
     record(event = "product found", prodId = 3, qty = 3, host = "A"),
     record(event = "search failed", prodId = 4, qty = 7, host = "B"),
     record(event = "search failed", prodId = 2, qty = 7, host = "C")
| filter in(host, array("B", "C")) or prodId == 3

```

Query result:

| event |
| --- |
| prodId |
| qty |
| host |
| `product found` |
| `3` |
| `3` |
| `A` |
| `search failed` |
| `4` |
| `7` |
| `B` |
| `search failed` |
| `2` |
| `7` |
| `C` |

#### Practical example

##### Example: Filter for critical logs

The following example uses the [fetch](/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch) command to load data from logs.
The `filter` command keeps only error records containing the string `failed` in the `content` field.

```
fetch logs
| filter loglevel == "ERROR" and matchesPhrase(content, "failed")

```

## filterOut

Removes records that match a specific condition.

The `filterOut` command only removes records where the condition evaluates to `true`. If the condition evaluates to `null` (or to any non-`boolean` data type), the record is kept.

This means that `filterOut x` and `filter not x` behave differently:

- `filterOut x` keeps records where `x` is `null`.

- `filter not x` removes records where `x` is `null`.

#### Syntax

`filterOut condition [, input]`

#### Basic examples

##### Example 1: Filter out by one condition

The following query uses the `filterOut` command to remove records based on the field `event`.

```
data record(event = "search failed", prodId = 5, qty = 6, host = "A"),
     record(event = "product found", prodId = 3, qty = 3, host = "A"),
     record(event = "search failed", prodId = 4, qty = 7, host = "B"),
     record(event = "search failed", prodId = 2, qty = 7, host = "C")
| filterOut event == "product found"

```

Query result:

| event |
| --- |
| prodId |
| qty |
| host |
| `search failed` |
| `5` |
| `6` |
| `A` |
| `search failed` |
| `4` |
| `7` |
| `B` |
| `search failed` |
| `2` |
| `7` |
| `C` |

##### Example 2: Filter out by multiple conditions

The following query uses the `filterOut` command to remove records based on evaluating multiple conditions.
[Logical operators](/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators) connect the conditions.

```
data record(event = "search failed", prodId = 5, qty = 6, host = "A"),
     record(event = "product found", prodId = 3, qty = 3, host = "A"),
     record(event = "search failed", prodId = 4, qty = 7, host = "B"),
     record(event = "search failed", prodId = 2, qty = 7, host = "C")
| filterOut host == "A" and qty > 3 or prodId == 4

```

Query result:

| event |
| --- |
| prodId |
| qty |
| host |
| `product found` |
| `3` |
| `3` |
| `A` |
| `search failed` |
| `2` |
| `7` |
| `C` |

#### Practical example

##### Example: Filter out informational logs

The following example uses the [fetch](/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch) command to load data from logs.
The `filterOut` command removes records with a `loglevel` value of `NONE` or `INFO`.

```
fetch logs
| filterOut loglevel == "NONE" or loglevel == "INFO"

```

## search

Searches for records that match the specified search condition.

The `search` command works like a search bar in DQL and allows you to explore your data with simple DQL queries. It filters the input data and keeps only those records that match the specified search condition. You can apply the command directly after the starting command - for example, `fetch` - or later in the query. With the `search` command, you can choose between searching across all fields of the records or within specific fields.
The `search` command performs a case-insensitive string matching.

#### Syntax

`search condition`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| condition |  | search condition |  | The condition all records have to fulfill. |  |  |

#### Basic examples

##### Example 1: Search logs

Here is an example of using the `search` command to find a particular keyword in your logs.

```
fetch logs
| search "nullpointer"

```

#### Search terms and pattern matching

The `search` command uses token-based string matching to find the search terms in your data (similar to the [matchesPhrase()](/platform/grail/dynatrace-query-language/functions/string-functions#matchesPhrase) function).

You can use a string literal `"term"` as the search condition to search for a term in all fields of the record. If you want to search for a term in a particular field, use the `~` operator within the search condition. The syntax of the `~` operator is `field ~ "term"`. You can use a field identifier of a root-level field on the left side of the `~` operator. Search terms on the right side of the `~` operator are case-insensitive and must be string literals.

The `search` command also supports string matching using wildcards. To match any sequence of zero or more characters in a token, you can use a `*` character anywhere in the search term. A pattern supports a maximum of 64 wildcard characters. Consecutive wildcards (for example, `**`) aren't supported.

##### Example 2: Simple search conditions

The following examples illustrate the use of search terms and patterns within the search condition in the `search` command.

```
data record(id = 1, content = "Setting up page /Transaction-Error/", loglevel = "INFO"),
     record(id = 2, content = "/tmp/batch.go [51]: Queue full", loglevel = "ERROR"),
     record(id = 3, content = "Failed to get pod status.", loglevel = "WARN")
| search "error" // matches records 1,2

```

Query result:

| id |
| --- |
| content |
| loglevel |
| `1` |
| `Setting up page /Transaction-Error/` |
| `INFO` |
| `2` |
| `/tmp/batch.go [51]: Queue full` |
| `ERROR` |

```
data record(id = 1, content = "Setting up page /Transaction-Error/", loglevel = "INFO"),
     record(id = 2, content = "/tmp/batch.go [51]: Queue full", loglevel = "ERROR"),
     record(id = 3, content = "Failed to get pod status.", loglevel = "WARN")
| search content ~ "error" // matches record 1

```

Query result:

| id |
| --- |
| content |
| loglevel |
| `1` |
| `Setting up page /Transaction-Error/` |
| `INFO` |

```
data record(id = 1, content = "Setting up page /Transaction-Error/", loglevel = "INFO"),
     record(id = 2, content = "/tmp/batch.go [51]: Queue full", loglevel = "ERROR"),
     record(id = 3, content = "Failed to get pod status.", loglevel = "WARN")
| search "err*" // matches records 1,2

```

Query result:

| id |
| --- |
| content |
| loglevel |
| `1` |
| `Setting up page /Transaction-Error/` |
| `INFO` |
| `2` |
| `/tmp/batch.go [51]: Queue full` |
| `ERROR` |

##### Example 3: Refine your search by specifying fields and using additional filters

The following example fetches all logs and filters the result to include AWS specific logs only. The `search` command finds logs, which include the term `error` in the content field.

```
fetch logs
| filter in(aws.region, "us-east-1", "eu-west-1")
| search content ~ "error"

```

##### Example 4: Aggregate and visualize the search result

You can combine the search command with other DQL commands to perform more complex queries. The following example helps you to aggregate and visualize the search result.

```
fetch logs
| search content ~ "*timeout"
| summarize timeouts = count(), by:loglevel
| sort timeouts desc

```

#### Multiple search terms and conditions

Multiple search terms can be combined using `and` and `or` operators in the search condition. Within the search condition, you can also combine string matching of search terms with the standard comparison operators (`==`, `!=`, `<=` , `<`, `>`, `>=`). Note that string values are case-sensitive for those operators.

##### Example 5: Multi-conditional search

In the following example multiple conditions are combined using the `and` operator.

```
data record(id = 1, url = "/cart/view", status = 200),
     record(id = 2, url = "/cart/checkout", status = 429),
     record(id = 3, url = "/index", status = 200)
| search "cart" and status >= 400

```

Query result:

| id |
| --- |
| url |
| status |
| `2` |
| `/cart/checkout` |
| `429` |

#### String matching with non-string data types

In the case of numeric (`long`, `double`), `ip`, and `uid` field values, the `search` command finds a match where the search term is equal to the string representation of the field value. Search terms with wildcards don't produce a match for these data types.

For fields containing nested records, the `search` command matches the search term against field names and values within the nested record. In the case of arrays, the `search` command matches the search term against element values within the array. Records and arrays can be nested on multiple levels.

##### Example 6: Searching in different data types

The following examples demonstrate matching of search terms against different data types.

```
data record(id = 1, action = "login", error = 404),
     record(id = 2, action =" logout", elements = record(login = "OK")),
     record(id = 3, action = "timeout", elements = array(record(login = "OK", ip = ip("10.0.0.10")),
                                                         record(error = "IOException")))
| search "login" // matches records 1,2,3

```

Query result:

| id |
| --- |
| action |
| error |
| elements |
| `1` |
| `login` |
| `404` |
| `2` |
| `logout` |
| **login:** `OK` |
| `3` |
| `timeout` |
| [**login:** `OK` **ip:** `10.0.0.10`, **error:** `IOException`] |

```
data record(id = 1, action = "login", error = 404),
     record(id = 2, action =" logout", elements = record(login = "OK")),
     record(id = 3, action = "timeout", elements = array(record(login = "OK", ip = ip("10.0.0.10")),
                                                         record(error = "IOException")))
| search "elements" // no match (field names are matched only in nested records)

```

Query result:

| id |
| --- |
| action |
| error |
| elements |

```
data record(id = 1, action = "login", error = 404),
     record(id = 2, action =" logout", elements = record(login = "OK")),
     record(id = 3, action = "timeout", elements = array(record(login = "OK", ip = ip("10.0.0.10")),
                                                         record(error = "IOException")))
| search elements ~ "IOException" // matches record 3

```

Query result:

| id |
| --- |
| action |
| error |
| elements |
| `3` |
| `timeout` |
| [**login:** `OK` **ip:** `10.0.0.10`, **error:** `IOException`] |

```
data record(id = 1, action = "login", error = 404),
     record(id = 2, action =" logout", elements = record(login = "OK")),
     record(id = 3, action = "timeout", elements = array(record(login = "OK", ip = ip("10.0.0.10")),
                                                         record(error = "IOException")))
| search "404" // matches record 1

```

Query result:

| id |
| --- |
| action |
| error |
| elements |
| `1` |
| `login` |
| `404` |

```
data record(id = 1, action = "login", error = 404),
     record(id = 2, action =" logout", elements = record(login = "OK")),
     record(id = 3, action = "timeout", elements = array(record(login = "OK", ip = ip("10.0.0.10")),
                                                         record(error = "IOException")))
| search "10.0.0.10" // matches record 3

```

Query result:

| id |
| --- |
| action |
| error |
| elements |
| `3` |
| `timeout` |
| [**login:** `OK` **ip:** `10.0.0.10`, **error:** `IOException`] |

##### Example 7: Deep search in array of nested records

In the following example we search for a particular keyword in the `span.events` field, which represents a collection of events stored as an array of nested records.

```
fetch spans
| search span.events ~ "exception"

```

#### Best practices and limitations

Specify the field identifier in your search expression (`field ~ "keyword"`) if you know in which field the relevant search string can be present. Otherwise, perform your search over all fields in the record.

It is best to apply the `search` command right after the starting command, such as `fetch`, and, optionally, some prefiltering. Between the starting command and the `search` command, you can use the following commands: [filter](/platform/grail/dynatrace-query-language/commands/filtering-commands#filter), [filterOut](/platform/grail/dynatrace-query-language/commands/filtering-commands#filterOut), [fieldsKeep](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsKeep), [fieldsRemove](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsRemove), [fieldsRename](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsRename), [limit](/platform/grail/dynatrace-query-language/commands/ordering-commands#limit), and [append](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#append).

For regular filtering or advanced conditions not supported by the search condition syntax, use the generic [filter](/platform/grail/dynatrace-query-language/commands/filtering-commands#filter) command instead or a combination of `search` and `filter` commands.
