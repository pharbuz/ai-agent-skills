> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands)

# DQL commands

This page provides a list of DQL commands grouped by categories. To get more in-depth information on a specific command, select its name.

## [Data source commands](/platform/grail/dynatrace-query-language/commands/data-source-commands)

| Name |  | Description |  | [data](/platform/grail/dynatrace-query-language/commands/data-source-commands#data) |  | Generates sample data during query runtime. |  | [describe](/platform/grail/dynatrace-query-language/commands/data-source-commands#describe) |  | Describes the on-read schema extraction definition for a given data object. |  | [fetch](/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch) |  | Loads data from the specified resource. |  | [fieldsSnapshot](/platform/grail/dynatrace-query-language/commands/data-source-commands#fieldsSnapshot) |  | Returns a snapshot of the fields present in records of the specified data object. |  | [load](/platform/grail/dynatrace-query-language/commands/data-source-commands#load) |  | Loads data from the specified resource. It's used with [lookup data](/platform/grail/lookup-data). |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [Metric commands](/platform/grail/dynatrace-query-language/commands/metric-commands)

| Name |  | Description |  | [timeseries](/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries) |  | Combines loading, filtering and aggregating metrics data into a time series output. |  | [metrics](/platform/grail/dynatrace-query-language/commands/metric-commands#metrics) |  | Retrieves metric series. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [Filter and search commands](/platform/grail/dynatrace-query-language/commands/filtering-commands)

| Name |  | Description |  | [dedup](/platform/grail/dynatrace-query-language/commands/filtering-commands#dedup) |  | Removes duplicates from a list of records. |  | [filter](/platform/grail/dynatrace-query-language/commands/filtering-commands#filter) |  | Reduces the number of records in a list by keeping only those records that match the specified condition. |  | [filterOut](/platform/grail/dynatrace-query-language/commands/filtering-commands#filterOut) |  | Removes records that match a specific condition. |  | [search](/platform/grail/dynatrace-query-language/commands/filtering-commands#search) |  | Searches for records that match the specified search condition. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [Selection and modification commands](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands)

| Name |  | Description |  | [fields](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fields) |  | Keeps only specified fields. |  | [fieldsAdd](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsAdd) |  | Evaluates an expression and appends or replaces a field. |  | [fieldsKeep](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsKeep) |  | Keeps selected fields. |  | [fieldsRemove](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsRemove) |  | Removes fields from the result. |  | [fieldsRename](/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsRename) |  | Renames a field. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [Extraction and parsing commands](/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands)

| Name |  | Description |  | [parse](/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands#parse) |  | Parses a record field and puts the result into one or more fields as specified in the pattern. |
| --- | --- | --- | --- | --- | --- | --- |

## [Ordering commands](/platform/grail/dynatrace-query-language/commands/ordering-commands)

| Name |  | Description |  | [limit](/platform/grail/dynatrace-query-language/commands/ordering-commands#limit) |  | Limits the number of returned records. |  | [sort](/platform/grail/dynatrace-query-language/commands/ordering-commands#sort) |  | Sorts the records. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [Structuring commands](/platform/grail/dynatrace-query-language/commands/structuring-commands)

| Name |  | Description |  | [expand](/platform/grail/dynatrace-query-language/commands/structuring-commands#expand) |  | Expands an array into separate records. |  | [fieldsFlatten](/platform/grail/dynatrace-query-language/commands/structuring-commands#fieldsFlatten) |  | Extracts/flattens fields from a nested record. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [Aggregation commands](/platform/grail/dynatrace-query-language/commands/aggregation-commands)

| Name |  | Description |  | [fieldsSummary](/platform/grail/dynatrace-query-language/commands/aggregation-commands#fieldsSummary) |  | Calculates the cardinality of field values that the specified fields have. |  | [makeTimeseries](/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries) |  | Creates timeseries from the data in the stream. |  | [summarize](/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize) |  | Groups together records that have the same values for a given field and aggregates them. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [Correlation and join commands](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands)

| Name |  | Description |  | [append](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#append) |  | Appends a given list of records by the records returned by a sub-query. |  | [join](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join) |  | Joins all records from the source and the sub-query as long as they fulfill the join condition. |  | [joinNested](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join-nested) |  | Adds matching results from the sub-query as an array of nested records. |  | [lookup](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#lookup) |  | Adds fields from a subquery to the source table by finding a match between a field in the source table and the lookup table. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [Smartscape commands](/platform/grail/dynatrace-query-language/commands/smartscape-commands)

| Name |  | Description |  | [smartscapeNodes](/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeNodes) |  | Loads Smartscape nodes using a type pattern (use `*` for all types). |  | [smartscapeEdges](/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeEdges) |  | Loads Smartscape edges using an edge type pattern (use `*` for all types). |  | [traverse](/platform/grail/dynatrace-query-language/commands/smartscape-commands#traverse) |  | Traverses source nodes to target nodes in the specified direction, following edge types defined by edgeTypes. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
