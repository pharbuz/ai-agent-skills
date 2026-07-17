# Typing Patterns

## Overloads

Use overloads when the return type depends on argument values or combinations.

```python
from typing import Literal, overload

@overload
def read(path: str, *, binary: Literal[False] = False) -> str: ...
@overload
def read(path: str, *, binary: Literal[True]) -> bytes: ...
def read(path: str, *, binary: bool = False) -> str | bytes: ...
```

In `.pyi` files, overload sets do not need a runtime implementation body unless
needed by the checker style being used. Many stubs contain only overload
variants.

## Optional Defaults

When `None` is a meaningful argument, include it explicitly.

```python
def connect(timeout: float | None = None) -> Connection: ...
```

When the default value exists but is not representable or not important, use
ellipsis.

```python
def connect(timeout: float = ...) -> Connection: ...
```

## Generics

```python
from collections.abc import Iterable, Iterator
from typing import TypeVar, Generic

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T) -> None: ...
    def get(self) -> T: ...

def first(values: Iterable[T]) -> T: ...
```

Prefer `Sequence[T]`, `Mapping[K, V]`, `Iterable[T]`, and `Callable[...]` for
parameters when callers can pass any compatible object.

## Protocols

Use protocols for structural requirements.

```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None: ...

def register(resource: SupportsClose) -> None: ...
```

Use callback protocols when a callback has attributes, overloads, or keyword
argument requirements that `Callable` cannot express well.

## `Self`, `type`, And Class Objects

```python
from typing import Self

class Query:
    def filter(self, expression: str) -> Self: ...

def create(cls: type[T]) -> T: ...
```

Use `Self` for fluent APIs returning the current class. Use `type[T]` for class
objects that instantiate or return subclasses.

## `Any` And `Incomplete`

Use `Any` when the public contract is intentionally dynamic or arbitrary.

```python
from typing import Any

def loads(data: str) -> Any: ...
```

Use `Incomplete` for stub information that is missing and should be improved.
In typeshed-style stubs, import it from `_typeshed`.

```python
from _typeshed import Incomplete

class Dynamic:
    generated_field: Incomplete
```

Do not hide known precise behavior behind `Any` or `Incomplete`.

## Literals And Sentinels

Use `Literal` for small fixed sets that affect behavior.

```python
from typing import Literal

def sort(order: Literal["asc", "desc"] = "asc") -> list[str]: ...
```

For sentinel defaults, expose the sentinel if it is public; otherwise use
overloads or ellipsis defaults to model behavior.

## Context Managers And Async APIs

```python
from types import TracebackType

class Resource:
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool | None: ...

class AsyncResource:
    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, exc_type, exc, tb) -> bool | None: ...
```

Annotate async functions as returning the awaited result, not `Coroutine`,
unless the function itself returns a coroutine object without awaiting.
