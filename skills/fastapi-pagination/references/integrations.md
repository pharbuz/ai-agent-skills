# fastapi-pagination — Integrations (`fastapi_pagination.ext.*`)

**The golden rule:** to paginate a database query, import `paginate` from the
backend's ext module and pass the **query** (not a materialized list). The ext
`paginate` translates the active params into the backend's own `LIMIT`/`OFFSET`
(or cursor / `.skip().limit()`), so only one page is fetched. The built-in
`fastapi_pagination.paginate` is for **in-memory sequences only**.

```python
# ❌ loads the whole table, then slices in Python
from fastapi_pagination import paginate
return paginate(db.execute(select(User)).scalars().all())

# ✅ pages in the database
from fastapi_pagination.ext.sqlalchemy import paginate
return paginate(db, select(User).order_by(User.id))
```

## Full backend table

| Backend | Import | `paginate(...)` first args |
|---|---|---|
| SQLAlchemy | `fastapi_pagination.ext.sqlalchemy` | `session, select(...)` (or a `Query`) |
| SQLModel | `fastapi_pagination.ext.sqlmodel` | `session, select(...)` |
| Databases (encode/databases) | `fastapi_pagination.ext.databases` | `database, query` |
| asyncpg | `fastapi_pagination.ext.asyncpg` | `connection, query` |
| psycopg | `fastapi_pagination.ext.psycopg` | `connection, query` |
| Django ORM | `fastapi_pagination.ext.django` | `queryset` |
| Tortoise ORM | `fastapi_pagination.ext.tortoise` | `Model` or queryset |
| ormar | `fastapi_pagination.ext.ormar` | `Model.objects` query |
| GINO | `fastapi_pagination.ext.gino` | `query` |
| Pony ORM | `fastapi_pagination.ext.pony` | `query` |
| Piccolo | `fastapi_pagination.ext.piccolo` | `query` |
| Peewee | `fastapi_pagination.ext.peewee` | `query` |
| `orm` library | `fastapi_pagination.ext.orm` | `query` |
| Cassandra | `fastapi_pagination.ext.cassandra` | `session, query` |
| Beanie | `fastapi_pagination.ext.beanie` | `Document.find(...)` |
| Bunnet | `fastapi_pagination.ext.bunnet` | `Document.find(...)` |
| Motor | `fastapi_pagination.ext.motor` | `collection, filter=...` |
| PyMongo | `fastapi_pagination.ext.pymongo` | `collection, filter=...` |
| MongoEngine | `fastapi_pagination.ext.mongoengine` | `Document.objects` |
| ODMantic | `fastapi_pagination.ext.odmantic` | `engine, Model` |

Most ext `paginate` functions also accept `params=` and `transformer=` keyword
arguments, mirroring the built-in.

## SQLAlchemy (sync)

```python
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

@app.get("/users")
def get_users(db: Session = Depends(get_db)) -> Page[UserOut]:
    return paginate(db, select(User).order_by(User.id))

add_pagination(app)
```

`paginate` runs a `SELECT count(*)` for `total` plus the windowed query. Pass a
fully built `select()`/`Query` including `where`/`join`/`order_by`.

## SQLAlchemy (async)

```python
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination.ext.sqlalchemy import paginate    # same module, async session

@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_async_db)) -> Page[UserOut]:
    return await paginate(db, select(User).order_by(User.id))
```

With an `AsyncSession`, `paginate` is awaitable — `await` it. (Older code may use
`fastapi_pagination.ext.async_sqlalchemy`; the unified `ext.sqlalchemy` handles
both sync and async sessions.)

## SQLModel

```python
from sqlmodel import select
from fastapi_pagination.ext.sqlmodel import paginate

@app.get("/heroes")
def heroes(session: Session = Depends(get_session)) -> Page[Hero]:
    return paginate(session, select(Hero).order_by(Hero.id))
```

## Beanie / Motor (MongoDB, async)

```python
from fastapi_pagination.ext.beanie import paginate

@app.get("/docs")
async def docs() -> Page[DocOut]:
    return await paginate(Document.find(Document.active == True))   # noqa: E712

# Motor (raw collection)
from fastapi_pagination.ext.motor import paginate
@app.get("/raw")
async def raw() -> Page[DocOut]:
    return await paginate(db.my_collection, {"active": True})
```

## Tortoise ORM (async)

```python
from fastapi_pagination.ext.tortoise import paginate

@app.get("/users")
async def users() -> Page[UserOut]:
    return await paginate(User.all().order_by("id"))
```

## Databases (encode/databases)

```python
from fastapi_pagination.ext.databases import paginate

@app.get("/users")
async def users() -> Page[UserOut]:
    return await paginate(database, users_table.select().order_by(users_table.c.id))
```

## Notes

- **Install extras.** Core install covers the basics; some backends/cursor paging
  need extras, e.g. `pip install "fastapi-pagination[sqlalchemy]"` (also pulls in
  `sqlakeyset` for cursor paging). Use the extra matching your backend.
- **Async ↔ await.** If the backend is async (AsyncSession, Beanie, Motor,
  Tortoise, databases, asyncpg), the ext `paginate` returns a coroutine — `await`
  it inside an `async def` route.
- **Ordering for cursor paging.** Cursor `paginate` requires an `ORDER BY` on the
  query (a unique/tiebreaker column is strongly recommended).
- **Transformers** convert rows → schema after paging — see
  `references/transformers-and-advanced.md`.
