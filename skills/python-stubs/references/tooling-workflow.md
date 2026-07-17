# Tooling Workflow

Use generators to bootstrap, not to finish. Generated stubs often contain
`Any`, miss overloads, expose implementation details, or differ from documented
public behavior.

## Bootstrap Options

`stubgen` from mypy:

```bash
stubgen -m package_name -o stubs
stubgen -p package_name -o stubs
stubgen path/to/module.py -o stubs
```

Use `stubgen` when source or importable modules are available and a broad first
draft is useful.

Pyright:

```bash
pyright --createstub package_name
```

Use Pyright stubs as another draft source, especially when the project already
uses Pyright/Pylance.

MonkeyType:

```bash
monkeytype run script_using_library.py
monkeytype stub package_name.module
```

Use MonkeyType when representative runtime traces exist. Treat traced types as
examples, not full contracts.

## Manual Refinement Loop

1. Read public docs, examples, and tests.
2. Inspect runtime objects with `inspect.signature`, `help()`, `dir()`, and
   source code where possible.
3. Keep only public modules, classes, functions, constants, and attributes.
4. Replace broad generated types with stable public contracts.
5. Add overloads for argument-dependent behavior.
6. Use `Incomplete` for unknown details that should be improved, not for
   behavior that is truly dynamic.
7. Add package exports and `__all__` behavior.

## Validation

Run a static checker against code that imports the stubs:

```bash
mypy --strict examples/
pyright examples/
```

Run `stubtest` to compare stubs with runtime objects:

```bash
python -m mypy.stubtest package_name
python -m mypy.stubtest package_name --allowlist stubtest_allowlist.txt
```

Use an allowlist only for intentional runtime/static differences, platform
differences, or dynamically generated APIs that cannot be represented directly.

Lint stubs:

```bash
flake8 path/to/stubs
```

`flake8-pyi` catches stub-specific style and correctness issues.

## Packaging

Inline typed package:

```text
package/
  __init__.py
  module.py
  py.typed
```

Package with adjacent stubs:

```text
package/
  __init__.py
  module.py
  module.pyi
  py.typed
```

Stub-only package:

```text
types-package-name/
  package/
    __init__.pyi
    module.pyi
```

For partial stub packages, include a marker describing partial coverage in the
standard form expected by type checkers.

## CI Checklist

- Install the runtime package under test.
- Install type-checker dependencies and optional extras needed for imports.
- Run `stubtest` against supported Python versions and platforms when possible.
- Run `mypy` or `pyright` on representative user code.
- Run `flake8-pyi`.
- Keep allowlists small and reviewed.
