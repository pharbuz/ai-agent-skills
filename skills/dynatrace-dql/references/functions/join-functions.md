> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/join-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/join-functions)

# Join functions

Functions that join records from subqueries.

## lookup

Returns a record from a subquery (the lookup table) producing a match between a field in the source table (`sourceField`) and a field in the lookup table (`lookupField`).

In contrast to the `lookup` command, the `lookup` function nests all included fields in the form of a DQL record.

In a case, where more than one match is produced in the lookup table, only the first matching record of the lookup table is returned. When the key values in the source and lookup table are both `null`, corresponding records aren't matched.

#### Syntax

`lookup(lookupTable, lookupField [, sourceField] [, executionOrder])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| lookupTable |  | execution block |  | Subquery producing the lookup table. |  |  |
| sourceField |  | expression |  | The matching field in the source table (left side). |  |  |
| lookupField |  | expression |  | The matching field in the lookup table (right side). |  |  |
| executionOrder |  |  |  |  |  |  |
| Defines which side of the join will be executed first. The allowed values are `auto`, `leftFirst`, `rightFirst`. The default value is `auto`. |  |  |  |  |  |  |

#### Returns

The data type of the returned value is `record`.

#### Examples

##### Example 1

```
data record(location = "Vienna", bookings = 1337),
     record(location = "London", bookings = 2431)
| fieldsAdd result = lookup([
    data record(city = "Vienna", country = "Austria"),
         record(city = "Barcelona", country = "Spain")
    ],
    sourceField:location,
    lookupField:city)

```

Query result:

| location |  | bookings |  | result |  | `Vienna` |  | `1,337` |  | **city**: `Vienna`**country**: `Austria` |  | `London` |  | `2,431` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

In a case, where more than one match is produced in the lookup table, only the first matching record of the lookup table is returned.

```
data record(location = "Barcelona"),
     record(location = "London")
| fieldsAdd result = lookup([
    data record(team = "FC Barcelona", city = "Barcelona"),
         record(team = "Chelsea", city = "London"),
         record(team = "FC Arsenal", city = "London"),
         record(team = "Tottenham Hotspur", city = "London")
    ],
    sourceField:location,
    lookupField:city)

```

Query result:

| location |  | result |  | `Barcelona` |  | **team**: `FC Barcelona`**city**: `Barcelona` |  | `London` |  | **team**: `Chelsea`**city**: `London` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Limits

The same [limits](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join-limits) as described for the `join` command apply.

## getNodeName

Returns the Smartscape node name.

#### Syntax

`getNodeName(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The expression to determine the Smartscape node ID. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
fetch bizevents
| fieldsAdd getNodeName(dt.smartscape.host)

```

## getNodeField

Returns the field value for a Smartscape node.

#### Syntax

`getNodeField(expression, name)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The expression to determine the Smartscape node ID. |  |  |
| name |  | string |  | The Smartscape field name to be queried. |  |  |

#### Returns

The data type of the returned value can be `boolean`, `long`, `double`, `timestamp`, `timeframe`, `duration`, `string`, `ip`, `uid`, `binary`, `array`, or `record`.

#### Examples

##### Example 1

```
timeseries avg(dt.host.cpu.idle), by:{ dt.smartscape.host }
| fieldsAdd getNodeField(dt.smartscape.host, "tags")

```
