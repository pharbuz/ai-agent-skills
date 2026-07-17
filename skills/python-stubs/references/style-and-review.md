# Style And Review

## What Belongs In A Stub

Include public API surface:

- Public modules, classes, functions, constants, and attributes.
- Re-exported names that users import from the module.
- Methods and descriptors that callers can use.
- Dunder methods when they define public behavior such as iteration,
  comparison, context manager support, or numeric operations.

Avoid:

- Private implementation helpers unless users rely on them or they affect
  public typing.
- Function bodies beyond `...`.
- Runtime-only side effects.
- Overly narrow inferred types from one trace or one example.

## Quality Rules

- Keep signatures compatible with runtime callability.
- Preserve defaulted parameters, positional-only markers, keyword-only markers,
  variadic `*args`/`**kwargs`, and async/sync behavior.
- Prefer precise parameter and return types for documented behavior.
- Use broader input protocols and precise output types.
- Add overloads instead of unions when a union loses argument/return
  relationships.
- Mark class variables with `ClassVar` when they are not per-instance fields.
- Use `Final` sparingly for true public constants.
- Keep imports minimal and explicit.

## Runtime Compatibility Review

When reviewing a stub, check:

```python
import inspect
import package_name

print(inspect.signature(package_name.some_function))
print(dir(package_name.SomeClass))
```

Compare:

- Does every public runtime object have a stub if it should be typed?
- Does every stubbed object exist at runtime on the supported platform?
- Do required/default parameters match?
- Are decorators represented correctly (`@property`, `@classmethod`,
  `@staticmethod`, `@overload`)?
- Are documented exceptions or sentinel return values represented by types when
  relevant?

## `stubtest` Allowlist Guidance

Use an allowlist for deliberate mismatches only:

- Platform-specific APIs.
- Version-specific APIs under conditional imports.
- Dynamically generated members that are real but not introspectable.
- Runtime signatures that are too broad or opaque but documented behavior is
  narrower.

Do not allowlist avoidable missing exports or wrong signatures.

## flake8-pyi Guidance

Run `flake8-pyi` through `flake8` on stubs. Fix issues instead of suppressing
them when possible. Common categories:

- Use `...` bodies and defaults correctly.
- Avoid unnecessary `Any`.
- Prefer modern collection aliases and typing constructs.
- Avoid redundant unions or optional forms.
- Keep type variables and aliases scoped clearly.

## Common Pitfalls

- Treating generated stubs as finished.
- Forgetting `py.typed` for inline typed packages.
- Missing re-exports in `__init__.pyi`.
- Using concrete containers for parameters where `Iterable` or `Mapping` is the
  public contract.
- Returning `Any` from APIs with documented return types.
- Overusing `object` where callers need operations on the value.
- Forgetting async functions return the awaited result type.
- Missing `None` in return types for functions that can return `None`.
- Encoding one Python version's API without guards or separate validation for
  supported versions.

## Review Output Format

When asked to review stubs, lead with findings:

```text
Findings
- path/module.pyi:12: signature requires `name`, but runtime default is `None`.
- path/module.pyi:35: return type loses relationship with `binary=True`; use overloads.

Tests
- Ran `python -m mypy.stubtest package_name`.
- Ran `flake8 path/to/stubs`.
```
