# fastapi-pagination — Customization

Two levels: **declarative** (`CustomizedPage[...]` + `Use*` customizers — covers
most needs) and **structural** (subclass `AbstractPage` / `AbstractParams`).

## CustomizedPage + customizers

`CustomizedPage` works like `typing.Annotated`: the first arg is the base page
type, the rest are customizer instances applied in order.

```python
from fastapi import Query
from fastapi_pagination import Page
from fastapi_pagination.customization import (
    CustomizedPage, UseParamsFields, UseName, UseIncludeTotal,
)

MyPage = CustomizedPage[
    Page[int],
    UseParamsFields(size=Query(100, ge=1, le=1_000)),   # change a param field
    UseIncludeTotal(False),                             # drop the count + total
    UseName("MyPage"),                                  # OpenAPI schema name
]

@app.get("/nums")
async def nums() -> MyPage:        # note: size param already bound to int via Page[int]
    return paginate(range(1_000))
```

### Customizer catalog

| Customizer | Effect |
|---|---|
| `UseParamsFields(**fields)` | Override individual param fields (e.g. `size=Query(...)`, `page=...`) |
| `UseParams(params_cls)` | Replace the whole params class |
| `UseOptionalParams()` | Make pagination params optional (return all if absent) |
| `UseIncludeTotal(bool)` | Toggle the `count(*)` / `total` field |
| `UseQuotedCursor(bool)` | Quote/unquote the cursor value (cursor pages) |
| `UseName(str)` | Rename the generated OpenAPI model |
| `UseModule(str)` | Set the model's `__module__` (schema grouping) |
| `UseModelConfig(**cfg)` | Inject Pydantic `model_config` entries |
| `UseExcludedFields(*names)` | Remove fields from the page model |
| `UseFieldsAliases(**aliases)` | Alias page fields (e.g. `items="data"`) |
| `UseAdditionalFields(**fields)` | Add extra fields to the page model |
| `UseFieldTypeAnnotations(...)` | Override field type annotations |
| `UseResponseHeaders(...)` | Emit pagination info as response headers |
| `UseFlattenPage()` | Flatten nested page structure |
| `UsePydanticV1()` | Render the model under Pydantic v1 semantics |

Combine freely — later customizers see the result of earlier ones:

```python
CompactPage = CustomizedPage[
    Page[ItemOut],
    UseFieldsAliases(items="data", total="count"),
    UseExcludedFields("pages"),
    UseName("CompactPage"),
]
```

## Custom Page model (structural)

Subclass `AbstractPage`, declare your fields, bind a params type via
`__params_type__`, and implement `create`:

```python
from typing import TypeVar, Generic, Any, Sequence, Optional
from fastapi_pagination import Params
from fastapi_pagination.bases import AbstractPage, AbstractParams

T = TypeVar("T")

class MyPage(AbstractPage[T], Generic[T]):
    results: list[T]
    totalResults: int

    __params_type__ = Params      # which query params this page uses

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        params: AbstractParams,
        *,
        total: Optional[int] = None,
        **kwargs: Any,
    ) -> "MyPage[T]":
        assert total is not None, "total must be provided"
        return cls(results=list(items), totalResults=total)
```

`create` receives the page's `items`, the resolved `params`, and `total`
(plus cursor extras for cursor pages). Return a fully built model instance.

## Custom Params model (structural)

Subclass `AbstractParams` and implement `to_raw_params`, returning `RawParams`
(limit/offset backends) or `CursorRawParams` (cursor backends):

```python
from typing import Annotated
from fastapi import Query
from fastapi_pagination.bases import AbstractParams, RawParams

class MyParams(AbstractParams):
    pageNumber: Annotated[int, Query(ge=1)] = 1
    pageSize: Annotated[int, Query(ge=1, le=100)] = 50

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.pageSize,
            offset=(self.pageNumber - 1) * self.pageSize,
            include_total=True,
        )
```

Cursor variant:

```python
from fastapi_pagination.bases import AbstractParams, CursorRawParams

class MyCursorParams(AbstractParams):
    cursor: Annotated[str | None, Query()] = None
    pageSize: Annotated[int, Query(ge=1, le=100)] = 50

    def to_raw_params(self) -> CursorRawParams:
        return CursorRawParams(cursor=self.cursor, size=self.pageSize)
```

Wire the params to a page through that page's `__params_type__`
(`__params_type__ = MyParams`), or attach with `UseParams(MyParams)`.

## Notes

- **Prefer customizers** for field/param tweaks — they keep the generated OpenAPI
  schema and serialization correct. Reach for `AbstractPage`/`AbstractParams`
  only when the shape itself must change.
- **`RawParams` is the bridge.** Whatever your params look like to the client,
  `to_raw_params()` maps them to the limit/offset (or cursor/size) the ext
  `paginate` functions understand.
- **`include_total=False`** skips the `count(*)` query — cheaper, but `total`
  comes back `None`.
