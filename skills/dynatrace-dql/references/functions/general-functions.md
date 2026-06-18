> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/general-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/general-functions)

# General functions

Functions with a general purpose.

## classicEntitySelector

Returns entities matching the specified entity selector.

You can use the returned entity IDs to filter entities based on their ID. The `classicEntitySelector` function is only supported as `in(field, classicEntitySelector(".."))`.
To learn more, see [entity selector.](/dynatrace-api/environment-api/entity-v2/entity-selector)

#### Syntax

`classicEntitySelector(entitySelector)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| entitySelector |  | string |  | The entity selector string. See [limitations.](/dynatrace-api/environment-api/entity-v2/entity-selector#limitations) |  |  |

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

In this example, the query fetches all logs for pod running on the Kubernetes namespace `CLOUD_APPLICATION_NAMESPACE-1B6CFC8C542A2273`.

```
fetch logs
| filter in(dt.entity.cloud_application_instance, classicEntitySelector("type(CLOUD_APPLICATION_INSTANCE),toRelationShip.IS_NAMESPACE_OF_CAI(type(CLOUD_APPLICATION_NAMESPACE), entityId(CLOUD_APPLICATION_NAMESPACE-1B6CFC8C542A2273))"))

```

To use this function, you need the `storage:entities:read` permissions. For details, see [Permissions in Grail](/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table).

## entityAttr

Returns the attribute value for an entity.
If you do not define an alias for a field added using the `entityAttr` function, the default field name will be `<entity-type>.<attribute-name>`.

To use this function, you need the `storage:entities:read` permissions. For details, see [Permissions in Grail](/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table).

#### Syntax

`entityAttr(expression, name [, type])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | entity type |  | The expression to determine the entity ID. |  |  |  | name |  | string |  | The entity attribute name that shall be queried. |  |  |  | type |  | string |  | The entity type that shall be queried. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value depends on the queried entity attribute.

#### Examples

##### Example 1

```
timeseries avg(dt.host.cpu.idle), by:{ dt.entity.host }
| fieldsAdd entityAttr(dt.entity.host, "tags")

```

To use this function, you need the `storage:entities:read` permissions. For details, see [Permissions in Grail](/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table).

## entityName

Returns the name of an entity.
If you do not define an alias for a field added using the `entityName` function, the default field name will be `<entity-type>.name`.

#### Syntax

`entityName(expression [, type])`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  | expression |  | entity type |  | The expression to determine the entity ID. |  |  |  | type |  | string |  | The entity type that shall be queried. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Returns

The data type of the returned value is a `string`.

#### Examples

##### Example 1

```
fetch bizevents
| fieldsAdd entityName(dt.entity.host)

```

To use this function, you need the `storage:entities:read` permissions. For details, see [Permissions in Grail](/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table).

## exists

Tests if a field exists.

#### Syntax

`exists(field)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| field |  | field identifier |  | The name of the field that will be checked if it exists. |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

In this example, the query fetches a single log record and uses the `exists` function to test if various fields exist in the record.

```
fetch logs
| limit 1
| fields exists(timestamp), exists(content), exists(non.existing.field)

```

Query result:

| exists(timestamp) |  | exists(content) |  | exists(non.existing.field) |  | `true` |  | `true` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## in

Tests if a value is a member of an `array`.

The `in` function supports multiple haystacks and allows arrays in all arguments.

#### Syntax

`in(needle, haystack, …)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| needle |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | The element(s) to search for (the needle). |  |  |
| haystack |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | The elements to search for the needle element (the haystack). |  |  |

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(a = "java"),
    record(a = "python"),
    record(a = "dotnet"),
    record(a = "rust")
| fieldsAdd in(a, {"java", "go", "rust"})

```

Query result:

| a |  | in(a, {"java", "go", "rust"}) |  | `java` |  | `true` |  | `python` |  | `false` |  | `dotnet` |  | `false` |  | `rust` |  | `true` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example 2

```
data record(technologies = array("Java", "Spring", "Jetty")),
     record(technologies = array("Python", "Flask")),
     record(technologies = array("Java", "Hibernate"))
| fieldsAdd in(technologies, "Python", "Hibernate"),
            in(technologies, array("Spring", "Flask"))

```

Query result:

| technologies |  | in(technologies, {"Python", "Hibernate"}) |  | in(technologies, array("Spring", "Flask")) |  | `[Java, Spring, Jetty]` |  | `false` |  | `true` |  | `[Python, Flask]` |  | `true` |  | `true` |  | `[Java, Hibernate]` |  | `true` |  | `false` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## record

Creates a `record` from the keys and values of the parameter.

#### Syntax

`record(expression, …)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | array, boolean, double, duration, ip, long, record, string, timeframe, timestamp |  | An expression to add to the record. |  |  |

#### Returns

The data type of the returned value is `record`.

#### Examples

##### Example 1

```
data record(executable = "java", technologies = array("Java", "Spring", "Jetty")),
     record(executable = "python", technologies = array("Python", "Flask")),
     record(executable = "java", technologies = array("Java", "Jetty", "Hibernate"))

```

Query result:

| executable |  | technologies |  | `java` |  | `[Java, Spring, Jetty]` |  | `python` |  | `[Python, Flask]` |  | `java` |  | `[Java, Jetty, Hibernate]` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
