---
name: python-stubs
description: >-
  Write, review, generate, test, or package Python type stubs (`.pyi`) for
  libraries and applications. Trigger WHENEVER the user works with stub files,
  `py.typed`, `types-*` packages, `stubgen`, `stubtest`, `pyright --createstub`,
  MonkeyType, typeshed-style annotations, overloads, `Incomplete`, `_typeshed`,
  stub-only packages, partial stubs, or fixes mismatches between Python runtime
  APIs and static type checker behavior.
---

# python-stubs

Use this skill for Python stub authoring based on the Python typing
documentation's "Writing Stubs" guide. The guide was checked on 2026-07-17.

## Default Workflow

1. Identify the target: inline typed package, third-party library, C extension,
   compiled package, private module, or typeshed/stub-only package.
2. Inspect the runtime API directly with source, docs, introspection, tests, and
   examples. Do not guess public signatures from names alone.
3. Bootstrap stubs with a generator only when it saves time:
   `stubgen`, `pyright --createstub`, or MonkeyType.
4. Replace generated `Any` and weak signatures with precise types where the
   public contract is known.
5. Use `.pyi` syntax and stub conventions: ellipsis bodies, overloads for
   argument-dependent returns, properties for attributes, and exported names.
6. Run both a type checker and runtime/stub consistency checks.
7. Keep stubs maintainable: concise public API, no implementation details, and
   clear `Incomplete`/`Any` only where information is intentionally missing.

## Quick Commands

```bash
python -m pip install mypy pyright monkeytype flake8-pyi

# Generate a starting point with mypy:
stubgen -m package_name -o stubs

# Generate a starting point with Pyright:
pyright --createstub package_name

# Check stubs against runtime objects:
python -m mypy.stubtest package_name --mypy-config-file mypy.ini

# Lint stub style:
flake8 path/to/stubs
```

## Minimal `.pyi`

```python
from collections.abc import Iterable

class User:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None: ...
    def aliases(self) -> Iterable[str]: ...

def find_user(id: int, /) -> User | None: ...
```

## Decision Rules

- Prefer precise public contracts over mechanically generated broad `Any`.
- Use `Any` when dynamic behavior is truly arbitrary; use `Incomplete` for
  unknown types that should be improved later.
- Use overloads when return type depends on literal arguments, argument count,
  or whether an optional/default value is supplied.
- Prefer `collections.abc` protocols for parameters and concrete collection
  types for returns when the runtime guarantees them.
- Do not include private helper implementation details unless they are part of
  the supported API or needed for public typing.
- For packages with inline types, include `py.typed`. For separate stubs, use
  stub-only packages or typeshed-compatible layout.
- Always compare stubs with runtime behavior before finalizing.

## References

- Read [references/tooling-workflow.md](references/tooling-workflow.md) for
  generation, refinement, validation, packaging, and CI workflows.
- Read [references/stub-syntax-and-content.md](references/stub-syntax-and-content.md)
  for `.pyi` syntax, exports, attributes, classes, functions, imports, and
  package/module layout.
- Read [references/typing-patterns.md](references/typing-patterns.md) for
  overloads, generics, protocols, literals, callbacks, `Self`, `type`, `Any`,
  and `Incomplete`.
- Read [references/style-and-review.md](references/style-and-review.md) for
  typeshed-style quality rules, flake8-pyi guidance, runtime mismatch review,
  and common pitfalls.
