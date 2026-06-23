# fastapi-pagination — Item transformers & advanced API

## Item transformers

A transformer runs over the **page's items** after they're fetched/sliced and
before the response is built — the canonical way to turn ORM rows into Pydantic
schemas. Signature: `Callable[[list[T]], list[U]]`.

### 1. Per-call (preferred) — `transformer=`

```python
@app.get("/ints")
async def route() -> Page[int]:
    return paginate(range(100), transformer=lambda items: [i * 2 for i in items])

# ORM rows -> schema
@app.get("/users")
def users(db: Session = Depends(get_db)) -> Page[UserOut]:
    return paginate(
        db, select(User),
        transformer=lambda rows: [UserOut.model_validate(r) for r in rows],
    )
```

Every ext `paginate` accepts `transformer=` too.

### 2. Per-route — `set_items_transformer`

```python
from fastapi_pagination import set_items_transformer

@app.get("/ints")
async def route() -> Page[int]:
    set_items_transformer(lambda items: [i * 2 for i in items])
    return paginate(range(100))
```

### 3. Async transformers — `apaginate`

For async transformer functions, use `apaginate` (the async paginator):

```python
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.async_paginator import apaginate

async def enrich(items: list[int]) -> list[int]:
    return [await some_async_lookup(i) for i in items]

@app.get("/ints")
async def route() -> Page[int]:
    return await apaginate(range(100), transformer=enrich)
```

`apaginate` also paginates async iterables/sequences in memory; for DB queries
keep using the backend's async ext `paginate`.

## Page links

Add `next`/`previous`/`first`/`last` URL links to the response by using the
links-enabled page classes:

```python
from fastapi_pagination.links import Page          # Page with a `links` object
# also: fastapi_pagination.links.LimitOffsetPage

@app.get("/users")
async def users() -> Page[UserOut]:
    return paginate(all_users)
```

The response gains a `links` field: `{ "first": "...", "last": "...",
"self": "...", "next": "...", "prev": "..." }` built from the current request URL
and params.

## Response headers

Emit pagination metadata as HTTP headers (instead of / in addition to the body)
with the `UseResponseHeaders` customizer:

```python
from fastapi_pagination import Page
from fastapi_pagination.customization import CustomizedPage, UseResponseHeaders

PageWithHeaders = CustomizedPage[Page[ItemOut], UseResponseHeaders()]
```

## Low-level API

The pieces `paginate` orchestrates, usable directly when you build pages outside
a normal route:

- `set_page(page_type)` — page class the next `paginate`/`create` will build.
- `set_params(params)` — params to use, bypassing the request dependency.
- `resolve_params(params=None)` — the params currently in context (or default).
- `set_items_transformer(fn)` — transformer for the current context.
- `response()` — the current `Response` object (e.g. to set headers/status).
- `create_page(items, total, params, **kwargs)` — build a page instance manually
  (what a custom `AbstractPage.create` ultimately returns).

```python
from fastapi_pagination import set_page, set_params, resolve_params, response
from fastapi_pagination.cursor import CursorPage, CursorParams

set_page(CursorPage[ItemOut])
set_params(CursorParams(size=20))
page = paginate(db, select(Item).order_by(Item.id))
response().headers["X-Total-Count"] = str(page.total or 0)
```

## Notes

- **Transformer runs once, on one page's items** — it's not a per-item DB hit
  multiplier. Do bulk conversion (`model_validate`) there, not N+1 queries.
- **Keep the response model in sync.** If a transformer changes the item type
  (`T → U`), declare the route as `Page[U]` so OpenAPI/serialization match.
- **`apaginate` vs ext paginate.** Use `apaginate` for in-memory async work or
  async transformers over sequences; use the backend ext `paginate` (awaited) to
  page an actual async DB query.
