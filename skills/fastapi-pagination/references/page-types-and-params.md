# fastapi-pagination — Page types & params

A **page type** is the response model; its **params type** supplies the query
parameters. Declaring the page type on a route (return annotation or
`response_model=`) auto-injects the params as a dependency once
`add_pagination(app)` has run.

## Page (page-number based) — the default

```python
from fastapi_pagination import Page, Params, paginate

@app.get("/items")
async def items() -> Page[ItemOut]:
    return paginate(all_items)
```

- **Params** (`fastapi_pagination.Params`): `page` (`int ≥ 1`, default `1`),
  `size` (`int`, `1..100`, default `50`). Query: `?page=2&size=25`.
- **Page fields:** `items: list[T]`, `total: int | None`, `page: int | None`,
  `size: int | None`, `pages: int | None`.

```json
{ "items": ["..."], "total": 100, "page": 2, "size": 25, "pages": 4 }
```

## LimitOffsetPage

```python
from fastapi_pagination.limit_offset import LimitOffsetPage, LimitOffsetParams
# also re-exported at fastapi_pagination.LimitOffsetPage / LimitOffsetParams

@app.get("/items")
async def items() -> LimitOffsetPage[ItemOut]:
    return paginate(all_items)
```

- **Params:** `limit` (`1..100`, default `50`), `offset` (`≥ 0`, default `0`).
  Query: `?limit=10&offset=20`.
- **Page fields:** `items`, `total`, `limit`, `offset`.

## CursorPage

```python
from fastapi_pagination.cursor import CursorPage, CursorParams
from fastapi_pagination.ext.sqlalchemy import paginate

@app.get("/items")
def items(db: Session = Depends(get_db)) -> CursorPage[ItemOut]:
    return paginate(db, select(Item).order_by(Item.id))   # ORDER BY is mandatory
```

- **Params:** `cursor` (`str | None`, default `None` → first page),
  `size` (default `50`). Query: `?cursor=xyz&size=20`.
- **Page fields:** `items`, `total` (optional), `current_page`,
  `current_page_backwards`, `previous_page`, `next_page`. Follow `next_page` /
  `previous_page` as the opaque `cursor` value for the next request.
- Cursors encode the ordered position (SQLAlchemy uses the `sqlakeyset` library),
  so the query **must** have a deterministic `ORDER BY`. Cursor paging is O(1) on
  deep pages, unlike `OFFSET`.

## Explicit `Params` as a dependency

Pagination params resolve implicitly from the page type, but you can also take
them explicitly (e.g. to read `params.size` before calling `paginate`):

```python
from fastapi import Depends
from fastapi_pagination import Page, Params, paginate

@app.get("/items")
async def items(params: Params = Depends()) -> Page[ItemOut]:
    # params.page, params.size available here
    return paginate(all_items, params)
```

`paginate(seq, params)` accepts an explicit params object; omit it to use the
one resolved from the request context.

## Low-level: `set_page` / `set_params` / `resolve_params`

When you can't use the declarative route annotation (custom flow, background
job, non-route code), drive pagination manually:

```python
from fastapi_pagination import set_page, set_params, resolve_params
from fastapi_pagination.cursor import CursorPage, CursorParams

set_page(CursorPage[ItemOut])                 # which page type to build
set_params(CursorParams(size=20, cursor=None))# the params to use
page = paginate(db, select(Item).order_by(Item.id))

# resolve_params() returns the params currently in context (or a default)
current = resolve_params()
```

- `set_page(page_type)` — sets the page class used by the next `paginate`.
- `set_params(params)` — sets params explicitly (bypasses the request dependency).
- `resolve_params(params=None)` — returns the active params, falling back to the
  page's `__params_type__` default.

## Notes

- **`total`/`pages` optionality.** They are `Optional` on `Page`; when counting is
  disabled (`UseIncludeTotal(False)`) or on cursor pages they may be `None`.
- **Changing defaults/limits.** Prefer `CustomizedPage[..., UseParamsFields(...)]`
  or a custom `Params` (see `references/customization.md`) over editing globals.
- **Both import sites work.** `LimitOffsetPage`/`LimitOffsetParams` are exported
  both from `fastapi_pagination` and `fastapi_pagination.limit_offset`.
