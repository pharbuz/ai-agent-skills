---
name: tomlkit
description: >-
  Build, edit, validate, or migrate Python code that reads or writes TOML with
  `tomlkit`. Trigger WHENEVER the user installs or imports `tomlkit`; edits
  `pyproject.toml`, `Cargo.toml`, or another TOML configuration while retaining
  comments and formatting; uses `parse`, `load`, `dumps`, `dump`, `document`,
  `table`, `array`, `aot`, `inline_table`, `TOMLFile`, custom encoders, or
  handles TOML parse and conversion errors.
---

# tomlkit

Use `tomlkit` when a TOML file is a human-maintained document and its comments,
whitespace, indentation, quoting, and key order must survive edits. It is TOML
1.0.0 compliant. For read-only data loading where formatting is irrelevant,
prefer the standard-library `tomllib` on Python 3.11+.

## Default Workflow

1. Inspect the installed version and the target file before changing code.
2. Parse the existing text with `parse()` or use `load()` on an already-open
   text file. This returns a mutable `TOMLDocument` that behaves like a dict.
3. Make the smallest possible mutation to that document; do not convert it to a
   plain `dict` and back if formatting must be preserved.
4. Serialize the same document with `dumps()` or `dump()`.
5. Re-parse the generated TOML in tests and assert both the intended values and
   formatting-sensitive expectations such as retained comments when relevant.

```bash
python -m pip show tomlkit
python - <<'PY'
import tomlkit
print(tomlkit.__version__)
PY
```

## Parse, Edit, and Write an Existing File

Use UTF-8 text mode and retain the `TOMLDocument` throughout the edit.

```python
from pathlib import Path

from tomlkit import dumps, parse
from tomlkit.exceptions import ParseError


path = Path("pyproject.toml")
try:
    document = parse(path.read_text(encoding="utf-8"))
except ParseError as exc:
    raise ValueError(f"Invalid TOML at line {exc.line}, column {exc.col}") from exc

document["project"]["version"] = "1.2.0"
document["tool"]["ruff"]["line-length"] = 100
path.write_text(dumps(document), encoding="utf-8")
```

- `loads()` is an alias for `parse()`; it also accepts bytes.
- `load(fp)` reads an open text or binary file; `dump(document, fp)` writes to
  an open writable text stream.
- `TOMLFile(path).read()` and `.write(document)` are useful only when their
  small file wrapper makes the call site clearer.
- Use `document.unwrap()` only when a plain Python `dict`/`list` representation
  is required. It deliberately loses TOML-specific presentation metadata.
- Do not use `sort_keys=True` when preserving the original key order matters.

## Safe Mutations

Parsed containers support normal mapping operations. Assigning a supported
Python value converts it to a TOML item automatically.

```python
document["build-system"]["requires"].append("setuptools>=70")
document["project"]["keywords"] = ["cli", "toml"]
document["tool"].pop("obsolete", None)
del document["project"]["dynamic"]
```

- Check a key before indexing when it may not exist; missing container keys can
  raise `NonExistentKey`/`KeyError`.
- Create a missing nested table explicitly with `table()`; do not assume a
  mapping assignment will create every intermediate table.
- Preserve a value's intended TOML spelling and layout by modifying the parsed
  item rather than reconstructing a large parent table.
- Do not hand-format generated strings. Let `dumps()` render TOML and then
  validate by parsing its output.

## Construct Documents and TOML-Specific Values

Use helpers when creating structure, comments, precise string types, or layouts
that normal Python assignments cannot express.

```python
from tomlkit import aot, comment, document, inline_table, item, nl, table

doc = document()
doc.add(comment("Generated configuration"))
doc.add(nl())
doc.add("enabled", True)

server = table()
server.add("host", "127.0.0.1")
server.add("port", 8080)
doc.add("server", server)

metadata = inline_table()
metadata.update({"owner": "platform", "tier": "internal"})
doc["metadata"] = metadata

workers = aot()
workers.append(item({"name": "api", "replicas": 2}))
workers.append(item({"name": "jobs", "replicas": 1}))
doc["worker"] = workers
```

- `document()` creates a new root document; `table()` creates `[table]`.
- `aot()` creates an array of tables rendered as repeated `[[name]]` blocks.
- `array()` creates an array item. Use `.multiline(True)` for one-item-per-line
  output, or `.add_line(...)` when exact array line layout matters.
- `inline_table()` renders `{ key = value }`; use it only when a compact inline
  representation is intended.
- `string(value, literal=True)` creates literal strings; `multiline=True`
  creates triple-quoted strings. Leave `escape=True` unless the content is
  already known to be valid TOML without escaping.
- Use `key(["parent", "child"])` only when intentionally writing a dotted
  key such as `parent.child = value`.

## Comments, Whitespace, and Ordering

```python
from tomlkit import comment, nl

doc.add(comment("Configuration for the public API"))
doc.add(nl())
doc["server"].add("timeout", 30)
doc["server"]["timeout"].comment("seconds")
```

- `comment()` creates a standalone comment and `nl()` creates a blank line.
- `container.add(key, value)` appends an entry; `append(key, item)` is the
  stricter alternative when both key and item must be explicit.
- Parse first, then make local changes, to retain surrounding trivia. Replacing
  a whole table or serializing a plain `dict` may alter the chosen layout.

## Errors and Custom Types

Catch `ParseError` for invalid input; it exposes `line` and `col`. Catch
`ConvertError` when `tomlkit` cannot turn a Python value into a TOML item.

```python
from pathlib import Path
from tomlkit import item, register_encoder
from tomlkit.exceptions import ConvertError, ParseError

class Version:
    def __init__(self, text: str) -> None:
        self.text = text

@register_encoder
def encode_version(value: object):
    if isinstance(value, Version):
        return item(value.text)
    raise ConvertError(f"Unsupported TOML value: {type(value).__name__}")
```

- A registered encoder takes one value and must return a tomlkit item; raise
  `ConvertError` when it does not handle that value. Remove it with
  `unregister_encoder(encode_version)` when registration should not be global.
- Do not silently replace a broken TOML file with a new document after a parse
  error; surface the location and preserve the original file for correction.

## Verification Checklist

```python
from tomlkit import dumps, parse

rendered = dumps(document)
reparsed = parse(rendered)
assert reparsed["project"]["version"] == "1.2.0"
assert "# existing comment" in rendered
```

- Test parsing malformed TOML if error reporting is part of the feature.
- Assert generated TOML round-trips and contains required tables, arrays, and
  comments.
- For edits to a repository configuration file, inspect the diff: only the
  requested semantic change and unavoidable adjacent formatting should appear.
