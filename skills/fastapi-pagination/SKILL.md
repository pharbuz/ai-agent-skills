---
name: fastapi-pagination
description: >-
  Use the `fastapi-pagination` library (import `fastapi_pagination`) to add
  pagination to FastAPI endpoints. Trigger WHENEVER the user paginates FastAPI
  responses; declares a route returning `Page[T]`, `LimitOffsetPage[T]`, or
  `CursorPage[T]`; calls `paginate(...)`, `apaginate(...)`, or
  `add_pagination(app)`; imports from `fastapi_pagination` or
  `fastapi_pagination.ext.*`; wires page/size, limit/offset, or cursor query
  params; paginates a SQLAlchemy / SQLModel / Tortoise / Beanie / Motor / PyMongo
  / Databases / Django / ormar / GINO / Piccolo query; builds a custom Page or
  Params model (`AbstractPage`, `AbstractParams`, `to_raw_params`,
  `__params_type__`); customizes pages with `CustomizedPage` and `Use*`
  customizers; transforms ORM rows into Pydantic schemas before returning a page;
  or adds page links, response headers, or total counts. Covers page types,
  params, the ext integrations, item transformers, customization, and the
  low-level API.
---

# fastapi-pagination — pagination for FastAPI

[`fastapi-pagination`] adds page / limit-offset / cursor pagination to FastAPI
with a typed response model and a single `paginate()` call. Install and import as
`fastapi_pagination`.

```bash
pip install fastapi-pagination
# some integrations need extras, e.g.:
pip install "fastapi-pagination[sqlalchemy]"      # cursor paging pulls in sqlakeyset
```

[`fastapi-pagination`]: https://uriyyo-fastapi-pagination.netlify.app/

## Mental model

1. **Declare the page type as the return annotation** — `-> Page[Schema]`
   (or `LimitOffsetPage`, `CursorPage`). This both sets the response shape **and**
   adds the pagination query params (`page`/`size`, `limit`/`offset`, or
   `cursor`/`size`) to the endpoint.
2. **`return paginate(data)`** in the handler. `paginate` reads params from the
   request context (a `contextvar`) and produces the page. Use the **right
   `paginate`**: the built-in one for in-memory sequences, or
   `fastapi_pagination.ext.<backend>.paginate` for a DB query so paging happens
   **in the database**, not in Python.
3. **Call `add_pagination(app)` once** to wire the params dependency into your
   routes. Without it the query params don't appear and `paginate` can't find
   params at runtime.
4. **Customize** declaratively with `CustomizedPage[Page[T], Use...]`, or build
   your own with `AbstractPage` / `AbstractParams`.
5. **Transform items** (e.g. ORM row → Pydantic schema) with `transformer=` or
   `set_items_transformer`.

```python
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi_pagination import Page, add_pagination, paginate

app = FastAPI()

class UserOut(BaseModel):
    name: str
    surname: str

users = [UserOut(name="Steve", surname="Rogers")]

@app.get("/users")
async def get_users() -> Page[UserOut]:      # ?page=&size= + response shape
    return paginate(users)

add_pagination(app)                          # required — wires the params dependency
```

Response body:

```json
{ "items": [{"name": "Steve", "surname": "Rogers"}],
  "total": 1, "page": 1, "size": 50, "pages": 1 }
```

> The return-annotation style (`-> Page[UserOut]`) is the modern form;
> `@app.get("/users", response_model=Page[UserOut])` works identically.

## The three pagination techniques

Pick the page type; the matching params (and query string) follow automatically.

| Page type | Import | Query params | Page fields |
|---|---|---|---|
| `Page[T]` (default) | `fastapi_pagination` | `page` (≥1, def 1), `size` (1–100, def 50) | `items, total, page, size, pages` |
| `LimitOffsetPage[T]` | `fastapi_pagination` | `limit` (1–100, def 50), `offset` (≥0, def 0) | `items, total, limit, offset` |
| `CursorPage[T]` | `fastapi_pagination.cursor` | `cursor` (opt), `size` (def 50) | `items, total?, current_page, previous_page, next_page` |

```python
from fastapi_pagination import Page, LimitOffsetPage
from fastapi_pagination.cursor import CursorPage

@app.get("/a") async def a() -> Page[Item]:            return paginate(items)
@app.get("/b") async def b() -> LimitOffsetPage[Item]: return paginate(items)
```

Field shapes, defaults, JSON examples, explicit `Params` dependencies, and
`set_page` / `set_params` → [`references/page-types-and-params.md`](references/page-types-and-params.md).

## Paginating a database query (integrations)

**Don't** load the whole table and `paginate()` it in memory — import the
backend-specific `paginate` so the `LIMIT`/`OFFSET` (or cursor) runs in the DB:

```python
from sqlalchemy import select
from fastapi_pagination.ext.sqlalchemy import paginate     # NOT fastapi_pagination.paginate

@app.get("/users")
def get_users(db: Session = Depends(get_db)) -> Page[UserOut]:
    return paginate(db, select(User).order_by(User.created_at))
```

| Backend | `fastapi_pagination.ext.…` | First arg(s) |
|---|---|---|
| SQLAlchemy / SQLModel | `.sqlalchemy` / `.sqlmodel` | `session, select(...)` |
| Async SQLAlchemy | `.sqlalchemy` (async session) | `async_session, select(...)` |
| Databases / asyncpg / psycopg | `.databases` / `.asyncpg` / `.psycopg` | `conn, query` |
| Tortoise / ormar / GINO / Pony / Piccolo / Peewee / Django | `.tortoise` / `.ormar` / … | model query / queryset |
| Beanie / Motor / PyMongo / MongoEngine / ODMantic | `.beanie` / `.motor` / `.pymongo` / … | collection / find query |

Full table, exact signatures, async vs sync, and per-backend snippets →
[`references/integrations.md`](references/integrations.md).

## Transforming items (ORM → schema)

Convert raw rows / ORM models to your response schema **after** paging:

```python
@app.get("/users")
def get_users(db: Session = Depends(get_db)) -> Page[UserOut]:
    return paginate(
        db, select(User),
        transformer=lambda rows: [UserOut.model_validate(r) for r in rows],
    )
```

Async transformers run via `apaginate`; a global hook is `set_items_transformer`.
Details → [`references/transformers-and-advanced.md`](references/transformers-and-advanced.md).

## Customization

Tweak a page without subclassing using `CustomizedPage` + `Use*` customizers
(works like `typing.Annotated`):

```python
from fastapi import Query
from fastapi_pagination import Page
from fastapi_pagination.customization import CustomizedPage, UseParamsFields, UseName

BigPage = CustomizedPage[
    Page[int],
    UseParamsFields(size=Query(100, ge=1, le=1_000)),   # raise max size to 1000
    UseName("BigPage"),                                  # rename the OpenAPI schema
]
```

Customizers include `UseParamsFields`, `UseParams`, `UseOptionalParams`,
`UseIncludeTotal`, `UseName`, `UseModule`, `UseExcludedFields`,
`UseFieldsAliases`, `UseAdditionalFields`, `UseResponseHeaders`,
`UseFlattenPage`, and more. For full control, subclass `AbstractPage` (implement
`create`, set `__params_type__`) and `AbstractParams` (implement
`to_raw_params`). All customizers + custom models →
[`references/customization.md`](references/customization.md).

## Common pitfalls

- **Forgot `add_pagination(app)`.** The single most common bug — query params
  don't render and `paginate` errors with no params in context. Call it once.
- **Wrong `paginate` for a DB query.** `from fastapi_pagination import paginate`
  on an ORM result fetches the *entire* table into memory, then slices. Import
  `fastapi_pagination.ext.<backend>.paginate` and pass the **query**, not a list.
- **Async backend, sync `paginate`.** Async sessions/ODMs need the async ext
  paginate (awaited) — using the sync one returns coroutines or errors.
- **Cursor pagination needs a stable `ORDER BY`.** Cursors encode the sort
  position; without deterministic ordering, pages drift or repeat. SQLAlchemy
  cursor paging requires `sqlakeyset`.
- **Default `size` cap is 100.** Requests with `size>100` get a 422. Raise it via
  `CustomizedPage[..., UseParamsFields(size=Query(50, le=1000))]`.
- **`total` may be `None`.** If you disable the count (`UseIncludeTotal(False)`)
  or use cursor pages, `total`/`pages` can be absent — don't assume they exist.
- **Pydantic v1 vs v2.** Page models follow your Pydantic major version; force v1
  rendering with the `UsePydanticV1` customizer if you mix versions.

## Reference files

- [`references/page-types-and-params.md`](references/page-types-and-params.md) — `Page`/`LimitOffsetPage`/`CursorPage`, `Params`, fields, defaults, JSON shapes, `set_page`/`set_params`/`resolve_params`
- [`references/integrations.md`](references/integrations.md) — every `ext.*` backend, exact `paginate` signatures, sync vs async, install extras, in-memory-vs-DB rule
- [`references/customization.md`](references/customization.md) — `CustomizedPage` + all `Use*` customizers, custom `AbstractPage`/`AbstractParams`, `RawParams`/`CursorRawParams`
- [`references/transformers-and-advanced.md`](references/transformers-and-advanced.md) — item transformers (sync/async), `apaginate`, page links, response headers, low-level API

## Example scripts

- [`examples/quickstart_inmemory.py`](examples/quickstart_inmemory.py) — minimal `Page[T]` + `paginate` app
- [`examples/sqlalchemy_integration.py`](examples/sqlalchemy_integration.py) — async SQLAlchemy ext paginate with an ORM→schema transformer
- [`examples/cursor_pagination.py`](examples/cursor_pagination.py) — `CursorPage` over an ordered query
