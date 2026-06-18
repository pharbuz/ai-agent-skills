---
name: dynatrace-dql
description: >-
  Write and optimize Dynatrace Query Language (DQL) queries against Grail data.
  Use WHENEVER the user asks about DQL, Grail queries, fetch/filter/summarize
  pipelines, makeTimeseries, parse with Dynatrace Pattern Language, DQL
  functions or operators, querying logs/spans/bizevents/events/metrics/security
  data on Grail, DQL dashboards/notebooks, or migrating from SQL/Splunk/Kusto.
  Trigger on "DQL", "Dynatrace Query Language", "Grail query", pipe-based
  observability queries, dt.system.bucket, samplingRatio, scanLimitGBytes, or
  DQL API/Playground usage. Covers syntax, commands, functions, data types,
  operators, best practices, and domain-specific examples.
---

# Dynatrace Query Language (DQL)

DQL is Dynatrace's **read-only**, **pipeline-based** query language for exploring
data stored in **Grail**. Queries are plain text: commands chained with `|`, each
step receiving tabular input (records × fields) and passing output to the next.

Official docs: <https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language>

This skill mirrors the full language reference scraped from Dynatrace docs (Jan–Jun
2026). For exhaustive syntax per command/function, open the linked reference file.

## Mental model

1. **Start with a source command** — usually `fetch <dataObject>` (logs, spans,
   bizevents, events, metrics, smartscape.nodes, …) or `data` / `load` for
   samples and lookups.
2. **Pipe transformations** — `filter`, `parse`, `fieldsAdd`, `summarize`,
   `makeTimeseries`, `join`, `lookup`, `sort`, `limit`, …
3. **Order matters** — data flows sequentially; filter early, aggregate before
   `limit`, put `sort` near the end (see best practices).
4. **Schema-on-read** — no predefined SQL schema; field names can be dynamic.
   Use `describe <dataObject>` or `fieldsSnapshot <dataObject>` to discover fields.
5. **Strong typing** — functions/operators require compatible types; cast with
   `toLong()`, `toDouble()`, `toString()`, etc.

## Minimal query template

```dql
fetch logs, from:now() - 2h
| filter loglevel == "ERROR"
| summarize error_count = count(), by:{dt.entity.host}
| sort error_count, direction:"descending"
| limit 20
```

## Timeframes

Prefer the UI timeframe selector when building in Notebooks/Dashboards. Override
in `fetch` when needed:

```dql
fetch logs, from:now() - 2h
fetch logs, from:now() - 24h, to:now() - 2h
fetch logs, timeframe:"2021-10-20T00:00:00Z/2021-10-28T12:00:00Z"
```

Default timeframe (UI/API): **2 hours** unless specified.

## Field naming

- Unqualified names: `a-zA-Z0-9_.` (e.g. `dt.entity.host`, `host.name`)
- Other characters → wrap in backticks: `` `my field*` ``, `` `LOCAL_MACHINE\Software` ``
- Reserved words (`true`, `false`, `null`, `and`, `or`, `not`, `xor`, `mod`) as
  field names → backticks: `` `true` ``

## Command categories → reference

| Category | Reference | Key commands |
|----------|-----------|--------------|
| Getting started | [`references/dql-guide.md`](references/dql-guide.md) | Concepts, first queries |
| Syntax | [`references/dql-reference.md`](references/dql-reference.md) | Pipes, parameters, field rules |
| Best practices | [`references/dql-best-practices.md`](references/dql-best-practices.md) | Performance, command order |
| vs SQL/Splunk/Kusto | [`references/dql-comparison.md`](references/dql-comparison.md) | Migration cheatsheet |
| Data types | [`references/data-types.md`](references/data-types.md) | string, long, double, timestamp, duration, array, record, ip, … |
| Operators | [`references/operators.md`](references/operators.md) | `==`, `!=`, `~`, `!~`, `in`, `and`/`or`/`not`, arithmetic |
| Command index | [`references/commands.md`](references/commands.md) | All commands overview |

### Commands (detailed)

| Group | File | Commands |
|-------|------|----------|
| Data sources | [`references/commands/data-source-commands.md`](references/commands/data-source-commands.md) | `data`, `describe`, `fetch`, `fieldsSnapshot`, `load` |
| Filtering | [`references/commands/filtering-commands.md`](references/commands/filtering-commands.md) | `filter`, `filterOut`, `search`, `dedup` |
| Selection | [`references/commands/selection-and-modification-commands.md`](references/commands/selection-and-modification-commands.md) | `fields`, `fieldsAdd`, `fieldsKeep`, `fieldsRemove`, `fieldsRename` |
| Ordering | [`references/commands/ordering-commands.md`](references/commands/ordering-commands.md) | `sort`, `limit` |
| Aggregation | [`references/commands/aggregation-commands.md`](references/commands/aggregation-commands.md) | `summarize`, `makeTimeseries`, `fieldsSummary` |
| Joins | [`references/commands/correlation-and-join-commands.md`](references/commands/correlation-and-join-commands.md) | `join`, `lookup`, `append`, `join` (nested) |
| Parsing | [`references/commands/extraction-and-parsing-commands.md`](references/commands/extraction-and-parsing-commands.md) | `parse` (Dynatrace Pattern Language) |
| Structuring | [`references/commands/structuring-commands.md`](references/commands/structuring-commands.md) | `expand`, `fieldsFlatten` |
| Metrics | [`references/commands/metric-commands.md`](references/commands/metric-commands.md) | `timeseries`, `metrics` |
| Smartscape | [`references/commands/smartscape-commands.md`](references/commands/smartscape-commands.md) | `smartscapeNodes`, `smartscapeEdges`, `traverse` |

### Functions (detailed)

| Group | File |
|-------|------|
| Index (all functions) | [`references/functions.md`](references/functions.md) |
| Aggregation | [`references/functions/aggregation-functions.md`](references/functions/aggregation-functions.md) |
| Array | [`references/functions/array-functions.md`](references/functions/array-functions.md) |
| Bitwise | [`references/functions/bitwise-functions.md`](references/functions/bitwise-functions.md) |
| Boolean | [`references/functions/boolean-functions.md`](references/functions/boolean-functions.md) |
| Conditional | [`references/functions/conditional-functions.md`](references/functions/conditional-functions.md) |
| Conversion/casting | [`references/functions/conversion-and-casting-functions.md`](references/functions/conversion-and-casting-functions.md) |
| General | [`references/functions/general-functions.md`](references/functions/general-functions.md) |
| Hash | [`references/functions/hash-functions.md`](references/functions/hash-functions.md) |
| Join | [`references/functions/join-functions.md`](references/functions/join-functions.md) |
| Mathematical | [`references/functions/mathematical-functions.md`](references/functions/mathematical-functions.md) |
| Network/IP | [`references/functions/network-functions.md`](references/functions/network-functions.md) |
| String | [`references/functions/string-functions.md`](references/functions/string-functions.md) |
| Time | [`references/functions/time-functions.md`](references/functions/time-functions.md) |
| Vector distance | [`references/functions/vector-distance-functions.md`](references/functions/vector-distance-functions.md) |

## Domain examples

| Data domain | Reference |
|-------------|-----------|
| Logs on Grail | [`references/examples/analyze-explore-automate-logs-logs-on-grail-examples.md`](references/examples/analyze-explore-automate-logs-logs-on-grail-examples.md) |
| Metrics / timeseries | [`references/examples/analyze-explore-automate-metrics-dql-examples.md`](references/examples/analyze-explore-automate-metrics-dql-examples.md) |
| Security / threat observability | [`references/examples/secure-threat-observability-dql-examples.md`](references/examples/secure-threat-observability-dql-examples.md) |
| Business events | [`references/examples/observe-business-observability-bo-analysis.md`](references/examples/observe-business-observability-bo-analysis.md) |
| Davis problems & events | [`references/examples/dynatrace-intelligence-use-cases-dynatrace-intelligence-dql-examples.md`](references/examples/dynatrace-intelligence-use-cases-dynatrace-intelligence-dql-examples.md) |

## Performance checklist

From [`references/dql-best-practices.md`](references/dql-best-practices.md):

1. **Narrow time range** — `fetch logs, from:-10m`
2. **Limit buckets** — `fetch logs, bucket:{"default_logs", "logs_365_*"}`
3. **Sampling** (logs) — `samplingRatio:10|100|1000|1000|10000`; multiply counts by ratio
4. **Scan cap** — `scanLimitGBytes:100` (default 500 GB)
5. **Filter early** — prefer `field ~ "astro*"` over `matchesValue(lower(field), "astro*")`
6. **Inclusive filters** — avoid `not field ~ "x*"` when possible
7. **Avoid join/lookup for filtering** unless enriching first
8. **`sort` last** — never `fetch | sort | filter`
9. **Don't `limit` before `summarize`** unless intentional

## Common patterns

### Error rate by host

```dql
fetch logs, from:now() - 1h
| filter loglevel == "ERROR"
| summarize errors = count(), by:{host.name}
| sort errors, direction:"descending"
```

### Parse log content (DPL)

```dql
fetch logs, from:now() - 1h
| parse content, "LD 'status=' INT:status SPACE LD"
| filter status >= 400
| summarize count(), by:{status}
```

### Timeseries chart

```dql
fetch logs
| filter loglevel == "ERROR"
| makeTimeseries errors = count(), interval:5m
```

### Lookup enrichment

```dql
fetch bizevents
| lookup [load "/lookups/pricelist"], sourceField:product.id, lookupField:product.id
```

### Subquery / execution block

```dql
lookup [fetch logs | filter loglevel == "ERROR" | summarize c=count(), by:host.name], ...
```

## `fetch` key parameters

| Parameter | Purpose |
|-----------|---------|
| `from:` / `to:` | Relative timeframe (`-2h`, `now() - 24h`) |
| `timeframe:` | Absolute ISO8601 interval |
| `bucket:` | Bucket name(s) or wildcards |
| `samplingRatio:` | 1, 10, 100, 1000, 10000 (logs) |
| `scanLimitGBytes:` | Max uncompressed data read (-1 = all) |

## `summarize` syntax

```
| summarize [field=]aggregation [, ...] [, by:{ [field=]groupExpression [, ...] }]
```

```dql
| summarize event_count = count(), failed = countIf(http_status >= 400), by:{ip, host.name}
```

Parameter groups use `{}`:

```dql
| summarize {min(value), max(value)}, by:{field1, field2}
```

## String matching quick reference

| Operator / function | When to use |
|---------------------|-------------|
| `==` / `!=` | Exact known value |
| `~` / `!~` | Prefix/wildcard (`"core*"`) |
| `contains()`, `startsWith()`, `endsWith()` | Substring checks |
| `matchesPhrase()`, `matchesValue()` | Full-text style |
| `matchesPattern()` | Regex patterns |

String functions are **case-sensitive** by default; pass `caseSensitive:false` to override.

## Where to run DQL

- **Notebooks** — interactive exploration on Grail
- **Dashboards** — Add → DQL tile; supports `$variable` substitution
- **DQL Playground** — linked from command docs ("Run in Playground")
- **API** — Grail query API (see `dt-async` skill for Python client)
- **Learn DQL app** — interactive tutorials in Dynatrace Hub

## Workflow for the agent

When the user asks for a DQL query:

1. Identify **data object** (logs, spans, bizevents, events, metrics, …)
2. Set **timeframe** and **bucket** filters
3. Apply **early filters** on indexed/known fields
4. **Parse** only if raw text extraction is needed
5. **Aggregate** (`summarize` or `makeTimeseries`)
6. **Sort** and **limit** at the end
7. Open the relevant **reference file** for exact command/function syntax

When optimizing slow queries, read
[`references/dql-best-practices.md`](references/dql-best-practices.md) first.

When migrating from SQL/Splunk/Kusto, read
[`references/dql-comparison.md`](references/dql-comparison.md).

## Updating this skill

Reference files are generated from Dynatrace docs:

```bash
python3 scripts/scrape_dql_docs.py
```
