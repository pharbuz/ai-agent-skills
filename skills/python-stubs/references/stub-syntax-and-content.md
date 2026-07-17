# Stub Syntax And Content

Stub files use Python syntax with implementation bodies replaced by ellipses.

## Functions

```python
def parse(value: str, *, strict: bool = False) -> int: ...
async def fetch(url: str) -> bytes: ...
```

Preserve positional-only (`/`) and keyword-only (`*`) markers when the runtime
API has them.

Use `...` for unknown default values:

```python
def open_resource(name: str, timeout: float = ...) -> Resource: ...
```

## Classes

```python
class Client:
    base_url: str

    def __init__(self, base_url: str, /, *, timeout: float = ...) -> None: ...
    def close(self) -> None: ...
```

Annotate instance attributes in the class body when they are public. Include
methods, classmethods, staticmethods, properties, descriptors, and class
variables that are part of the API.

```python
from typing import ClassVar

class Config:
    default_timeout: ClassVar[float]
    timeout: float

    @property
    def is_enabled(self) -> bool: ...
```

## Constants And Variables

```python
VERSION: str
DEFAULT_PORT: int
DEBUG: bool
```

Use `Final` for constants that users should not reassign through the public
API.

```python
from typing import Final

DEFAULT_ENCODING: Final = "utf-8"
```

## Exports

Stubs should reflect runtime export behavior. If the module defines `__all__`,
represent it.

```python
__all__ = ["Client", "parse"]
```

Imported names are exported from a stub when they are intentionally re-exported.
Use explicit aliases to make this clear.

```python
from .client import Client as Client
```

## Imports

Import only types needed by the stub. Prefer modern standard-library locations
for typing constructs.

```python
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, Literal, overload
```

For compatibility across Python versions, use `typing_extensions` when the
target supported versions require it.

## Modules And Packages

Package stubs use the same module hierarchy as the runtime package.

```text
package/
  __init__.pyi
  client.pyi
  models.pyi
```

Use `__init__.pyi` for package-level exports. If a runtime submodule is part of
the public API, add a matching `.pyi`.

## C Extensions And Dynamic APIs

For C extensions or dynamic modules, rely on docs, introspection, examples, and
runtime tests. Use `stubtest` to catch objects missing from the stub or objects
declared in the stub that do not exist at runtime.

Do not encode implementation quirks as public API unless users can rely on
them.
