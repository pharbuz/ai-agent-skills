---
name: dynatrace-dpl
description: >-
  Write Dynatrace Pattern Language (DPL) patterns for parsing and reshaping
  Grail data. Use WHENEVER the user asks about DPL, Dynatrace Pattern Language,
  DQL parse command patterns, log processing patterns, matchers (INT, IPADDR,
  TIMESTAMP, LD, JSON), export names, quantifiers, lookaround (<<, >>), DPL
  Architect, preset patterns, STRUCTURE/ARRAY/ENUM groups, key-value pairs, or
  extracting fields from logs/spans/events. Trigger on "DPL", "parse content",
  "matcher", "export_name", Log processing on Grail, or schema-on-read field
  extraction. Covers grammar, modifiers, grouping, JSON/network/time matchers,
  and macros.
---

# Dynatrace Pattern Language (DPL)

DPL describes **patterns** built from **matchers** — mini-patterns for specific
data types (`INT`, `IPADDR`, `TIMESTAMP`, `LD`, …). Patterns are read **left to
right**; whitespace, line breaks, and `/* comments */` are ignored.

Official docs: <https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language>

This skill mirrors the full DPL reference scraped from Dynatrace docs (2026).
Open linked reference files for exhaustive matcher syntax and examples.

## Where DPL is used

1. **DQL `parse` command** — split a field into typed output fields at query time
2. **Log processing** — reshape incoming log data on ingest (LMA)
3. **DPL Architect** — interactive pattern builder with coverage feedback

```dql
fetch logs, from:now() - 1h
| parse content, "LD IPADDR:ip ':' LONG:payload SPACE LD 'HTTP_STATUS' SPACE INT:http_status LD (EOL|EOS)"
```

For DQL pipeline context see the [`dynatrace-dql`](../dynatrace-dql/SKILL.md) skill.

## Mental model

1. **All matchers must match** — the full pattern must succeed for a record
2. **Only named matchers export data** — assign `:export_name` to expose a field
3. **Separators match but don't export** — literals like `' '` or `','` anchor structure
4. **Element order** (right-to-left for modifiers):

   ```
   [lookaround] MATCHER ['(' config ')'] [quantifier] [optional?] [:export_name]
   ```

5. **Groups** compose matchers: sequence `(a, b)`, alternatives `(a | b)`,
   `ARRAY{}`, `STRUCTURE{}`, `ENUM{}`, `JSON{}`

## Minimal pattern

```
INT ' ' IPADDR:ip EOL
```

Equivalent multi-line with comments:

```
/* integer, space, IP — export IP as `ip` */
INT       // integer
' '       // single space
IPADDR:ip // IPv4/IPv6 → field `ip`
EOL       // line feed
```

## Matcher expression syntax

| Element | Syntax | Reference |
|---------|--------|-----------|
| Export name | `MATCHER:field_name` | [`log-processing-modifiers.md`](references/log-processing-modifiers.md) |
| Literal | `'text'`, `"text"` | [`log-processing-literal-expression.md`](references/log-processing-literal-expression.md) |
| Char group | `[a-zA-Z0-9]+` (regex-compatible) | [`log-processing-lines-strings.md`](references/log-processing-lines-strings.md) |
| Configuration | `TIMESTAMP('MMM d HH:mm:ss')`, `INT(min=50)` | [`log-processing-modifiers.md`](references/log-processing-modifiers.md) |
| Quantifier | `*`, `+`, `{n}`, `{min,max}` | [`log-processing-modifiers.md`](references/log-processing-modifiers.md) |
| Optional | `MATCHER?` or `(group)?` | [`log-processing-modifiers.md`](references/log-processing-modifiers.md) |
| Look behind | `<<` / `!<<` (max 64 bytes) | [`log-processing-modifiers.md`](references/log-processing-modifiers.md) |
| Look ahead | `>>` / `!>>` | [`log-processing-modifiers.md`](references/log-processing-modifiers.md) |
| Macro | `$$name = pattern;` then `$name` | [`log-processing-macros.md`](references/log-processing-macros.md) |

## Grammar quick reference

Full matcher table: [`references/log-processing-grammar.md`](references/log-processing-grammar.md)

| Category | Matchers | Reference |
|----------|----------|-----------|
| Lines & strings | `LD`, `DATA`, `EOL`, `LF`, `STRING`, `SQS`, `DQS`, `WORD`, `ALPHA`, `DIGIT`, `SPACE`, … | [`log-processing-lines-strings.md`](references/log-processing-lines-strings.md) |
| Numeric | `INT`, `LONG`, `FLOAT`, `DOUBLE`, `HEXINT`, `BOOL` | [`log-processing-numeric.md`](references/log-processing-numeric.md) |
| Time & date | `TIMESTAMP`, `TIME`, `ISO8601`, `JSONTIMESTAMP`, `HTTPDATE` | [`log-processing-time-date.md`](references/log-processing-time-date.md) |
| Network | `IPADDR`, `IPV4`, `IPV6` | [`log-processing-network.md`](references/log-processing-network.md) |
| JSON | `JSON`, `JSON_OBJECT{}`, `JSON_ARRAY{}`, `JSON_VALUE{}` | [`log-processing-json-object.md`](references/log-processing-json-object.md), [`log-processing-json-array.md`](references/log-processing-json-array.md), [`log-processing-json-value.md`](references/log-processing-json-value.md) |
| Key-value | `KVP{patternExprs}` | [`log-processing-key-value-pairs.md`](references/log-processing-key-value-pairs.md) |
| Credit card | `CREDITCARD` | [`log-processing-credit-card.md`](references/log-processing-credit-card.md) |
| Smartscape | `SMARTSCAPEID` | [`log-processing-smartscape.md`](references/log-processing-smartscape.md) |

## Grouping constructs

| Construct | Syntax | Purpose | Reference |
|-----------|--------|---------|-----------|
| Sequence | `(matcher, matcher, …)` | All members must match in order | [`log-processing-sequence-group.md`](references/log-processing-sequence-group.md) |
| Alternatives | `(matcher \| matcher \| …)` | First matching branch wins | [`log-processing-alternatives-group.md`](references/log-processing-alternatives-group.md) |
| Array | `ARRAY{patternExprs}` | Repeated elements | [`log-processing-array.md`](references/log-processing-array.md) |
| Structure | `STRUCTURE{patternExprs}:name` | Tuple of parsed values | [`log-processing-structure.md`](references/log-processing-structure.md) |
| Enum | `ENUM{string=integer, …}` | Map strings to integers | [`log-processing-enum.md`](references/log-processing-enum.md) |

## Common patterns

### Apache-style access log

```
IPADDR:ip ' ' LD ' ' '[' TIMESTAMP('dd/MMM/yyyy:HH:mm:ss Z'):ts ']' ' "' LD:method ' ' LD:path ' ' LD '" ' INT:status ' ' LONG:bytes
```

### Optional CSV field

```
TIMESTAMP:datetime ','
LD:level ','
LD:username? ','
INT:status EOL
```

Handles missing value (`INFO,,200`) and missing field (`INFO,500`).

### Multiline records (blank-line separator)

```
DATA:record (EOL EOL)
```

Use a **sequence group** around `(EOL EOL)` so `DATA` stops only at double line-feed.

### Conditional IP (look-behind)

Extract IP only when last octet ≥ 50:

```
IPADDR:ip_addr << INT(min=50) EOL
```

### Syslog header macro

```
$$syslog_hdr = TIMESTAMP('MMM d HH:mm:ss'):ts ' ' LD:host;
$syslog_hdr ' ' LD:process ': ' LD:message EOL
```

### JSON field extraction

```
JSON_OBJECT{ amount:INT, accountId:LONG }
```

See [`log-processing-json-object.md`](references/log-processing-json-object.md) for field mapping syntax.

## DPL Architect

Interactive tool for building/testing patterns with match coverage preview.

- Open from **Notebooks** (Fetch logs → cell → **Extract fields**) or **Investigations**
- **Base dataset** — coverage of pattern against query results
- **Match preview** — highlight matched portions per line
- **Preset patterns** for popular technologies

Full guide: [`references/dpl-architect.md`](references/dpl-architect.md)

## Workflow for the agent

When the user needs a DPL pattern:

1. Inspect a **sample record** (raw `content` or target field)
2. Identify **fixed literals** (separators, brackets, keywords) vs **variable data**
3. Choose **matchers** from grammar for each variable segment
4. Add **`:export_name`** only for fields needed in DQL downstream
5. Use **groups** for optional/alternative/multiline sections
6. Wrap in DQL: `| parse <field>, "<pattern>"`
7. For complex patterns, suggest **DPL Architect** or **macros** for reuse

When debugging parse failures:

- Check matcher **order** and **quantifiers** (`+` for multi-char char-groups)
- Distinguish missing value vs missing field (`?` placement)
- Use **lookaround** for conditional extraction without consuming input
- Verify **TIMESTAMP format** config matches actual string format

## Reference index

| Topic | File |
|-------|------|
| Overview & concepts | [`references/overview.md`](references/overview.md) |
| Full grammar table | [`references/log-processing-grammar.md`](references/log-processing-grammar.md) |
| Modifiers (lookaround, quantifier, optional, export) | [`references/log-processing-modifiers.md`](references/log-processing-modifiers.md) |
| DPL Architect | [`references/dpl-architect.md`](references/dpl-architect.md) |
| Literals | [`references/log-processing-literal-expression.md`](references/log-processing-literal-expression.md) |
| Lines & strings | [`references/log-processing-lines-strings.md`](references/log-processing-lines-strings.md) |
| Numeric | [`references/log-processing-numeric.md`](references/log-processing-numeric.md) |
| Time & date | [`references/log-processing-time-date.md`](references/log-processing-time-date.md) |
| Network | [`references/log-processing-network.md`](references/log-processing-network.md) |
| Credit card | [`references/log-processing-credit-card.md`](references/log-processing-credit-card.md) |
| Key-value pairs | [`references/log-processing-key-value-pairs.md`](references/log-processing-key-value-pairs.md) |
| JSON object/array/value | [`references/log-processing-json-object.md`](references/log-processing-json-object.md), [`log-processing-json-array.md`](references/log-processing-json-array.md), [`log-processing-json-value.md`](references/log-processing-json-value.md) |
| Array | [`references/log-processing-array.md`](references/log-processing-array.md) |
| Structure | [`references/log-processing-structure.md`](references/log-processing-structure.md) |
| Enum | [`references/log-processing-enum.md`](references/log-processing-enum.md) |
| Sequence group | [`references/log-processing-sequence-group.md`](references/log-processing-sequence-group.md) |
| Alternatives group | [`references/log-processing-alternatives-group.md`](references/log-processing-alternatives-group.md) |
| Macros | [`references/log-processing-macros.md`](references/log-processing-macros.md) |
| Smartscape ID | [`references/log-processing-smartscape.md`](references/log-processing-smartscape.md) |

## Updating this skill

Reference files are generated from Dynatrace docs:

```bash
python3 scripts/scrape_dpl_docs.py
```
