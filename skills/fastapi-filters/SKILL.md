---
name: fastapi-filters
description: >-
  Use the `fastapi-filters` library (import `fastapi_filters`) to add filtering
  and sorting to FastAPI endpoints. Trigger WHENEVER the user filters or sorts a
  FastAPI list endpoint; defines a `FilterSet` with `FilterField[T]` fields or
  builds filters with `create_filters` / `create_filters_from_model`; injects
  `filters: ... = Depends()` or `sorting: SortingValues =
  Depends(create_sorting(...))`; uses operator query params like
  `?name[eq]=Steve&age[gt]=30&sort=+age`; references `FilterOperator` (eq, ne,
  gt, ge, lt, le, like, ilike, in, not_in, is_null, contains, overlap…); applies
  filters/sorting to a query with `fastapi_filters.ext.sqlalchemy`, `.tortoise`,
  or `.beanie` (`apply_filters`, `apply_sorting`, `apply_filters_and_sorting`);
  customizes a `FilterField` (operators, alias, default_op, op_types) or remaps
  filter fields to DB columns; or consumes resolved `FilterValues` /
  `SortingValues` for raw SQL. This is uriyyo's `fastapi-filters` (plural) — not
  the separate `fastapi-filter` (arthurio) library. Covers FilterSet, operators,
  sorting, the ext integrations, and customization.
---

# fastapi-filters — filtering & sorting for FastAPI

[`fastapi-filters`] turns typed field declarations into FastAPI query parameters
(`?field[op]=value`, `?sort=±field`) and applies them to your DB query via
backend extensions. Install and import as `fastapi_filters`.

```bash
pip install fastapi-filters
```

> This is **uriyyo/fastapi-filters** (plural). Don't confuse it with the
> similarly named **arthurio/fastapi-filter** (singular) — different API.

[`fastapi-filters`]: https://github.com/uriyyo/fastapi-filters

## Mental model

1. **Declare what's filterable** — a `FilterSet` subclass of `FilterField[T]`
   fields (or `create_filters(name=str, age=int)` functionally). The field
   **type decides which operators** are allowed.
2. **Inject as dependencies** — `filters: UserFilters = Depends()` and
   `sorting: SortingValues = Depends(create_sorting("name", "age"))`. FastAPI
   auto-generates the `?field[op]=…` and `?sort=±field` query params and
   documents them in OpenAPI.
3. **Apply to your query** with the backend ext:
   `apply_filters_and_sorting(stmt, filters, sorting)` from
   `fastapi_filters.ext.<backend>`. It returns the modified query — you execute it.
4. **Customize per field** via `FilterField(operators=[...], alias=...,
   default_op=...)` when the type-driven defaults aren't enough.
5. **No supported ORM?** Consume the resolved `FilterValues` / `SortingValues`
   yourself and build any query.

```python
from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_filters import FilterField, FilterSet, SortingValues, create_sorting
from fastapi_filters.ext.sqlalchemy import apply_filters_and_sorting

app = FastAPI()

class UserFilters(FilterSet):
    name: FilterField[str]
    age: FilterField[int]

@app.get("/users")
async def get_users(
    db: AsyncSession = Depends(get_db),
    filters: UserFilters = Depends(),
    sorting: SortingValues = Depends(create_sorting("name", "age")),
) -> list[UserOut]:
    stmt = apply_filters_and_sorting(select(User), filters, sorting)
    return (await db.scalars(stmt)).all()
```

```
GET /users?name[eq]=Steve&age[gt]=30&age[le]=40&sort=+age,-name
```

## Operators are type-driven

Each `FilterField[T]` exposes only the operators that make sense for `T`. Use them
as `?field[operator]=value`.

| Field type | Operators available (`[op]`) |
|---|---|
| any type | `eq`, `ne`, `in`, `not_in` |
| `str` | + `like`, `ilike`, `not_like`, `not_ilike` |
| `int` `float` `date` `datetime` `timedelta` | + `gt`, `ge`, `lt`, `le` |
| `bool` | `eq`, `ne` only |
| `list` / sequence | `overlap`, `not_overlap`, `contains`, `not_contains` only |
| `Optional[...]` | + `is_null` |

```
?name[eq]=Steve          ?name[ilike]=ste        ?age[gt]=30&age[le]=40
?id[in]=1,2,3            ?deleted_at[is_null]=true   ?tags[contains]=python,fastapi
```

- **List operators take CSV** — `in`, `not_in`, `overlap`, `contains` accept a
  comma-separated list: `?id[in]=1,2,3`. (Enum member is `in_`; the URL token is `in`.)
- **`FilterValues`** is the resolved result: a mapping of field → operator →
  value. Pass it (or the `FilterSet` instance) straight to the ext apply funcs.

Full operator reference, `FilterField` options, and the functional `create_filters`
API → [`references/filters-and-operators.md`](references/filters-and-operators.md).

## Sorting

`create_sorting(*fields, default=..., alias=...)` builds a `SortingResolver`
dependency that yields `SortingValues` (a list of `(field, nulls, direction)`).

```python
sorting: SortingValues = Depends(create_sorting("name", "age", default="-age"))
```

```
?sort=+age,-name      # CSV: +asc, -desc, bare = asc; left-to-right priority
```

`create_sorting_from_model(Model, include=..., exclude=...)` derives sortable
fields from a Pydantic model. Nulls handling, multi-field priority, defaults →
[`references/sorting.md`](references/sorting.md).

## Backend integrations (`fastapi_filters.ext.*`)

Each ext exposes `apply_filters(query, filters)`, `apply_sorting(query, sorting)`,
and `apply_filters_and_sorting(query, filters, sorting)` — all take the backend's
query object and **return the same type** (so you execute it yourself).

| Backend | Import | Query object |
|---|---|---|
| SQLAlchemy (sync + async) | `fastapi_filters.ext.sqlalchemy` | `Select` / `Query` |
| Tortoise ORM | `fastapi_filters.ext.tortoise` | `QuerySet` |
| Beanie (MongoDB) | `fastapi_filters.ext.beanie` | `FindMany` |
| Raw SQL / other | — (no ext) | iterate `FilterValues` + `SortingValues` yourself |

```python
# Tortoise
from fastapi_filters.ext.tortoise import apply_filters_and_sorting
qs = apply_filters_and_sorting(User.all(), filters, sorting)
return await qs

# Beanie
from fastapi_filters.ext.beanie import apply_filters_and_sorting
q = apply_filters_and_sorting(User.find(), filters, sorting)
return await q.to_list()
```

Exact signatures, async SQLAlchemy, `remapping=` (field→column), the `additional`
namespace, and custom condition hooks → [`references/integrations.md`](references/integrations.md).

## Customization

```python
from fastapi_filters import FilterField, FilterOperator as Op

class UserFilters(FilterSet):
    # restrict operators + expose under a different query name
    email: FilterField[str] = FilterField(operators=[Op.eq, Op.ilike], alias="mail")
    # default operator when client omits the [op] bracket
    name: FilterField[str] = FilterField(default_op=Op.ilike)
```

`FilterField(type=None, operators=None, default_op=None, name=None, alias=None,
internal=False, op_types=None)`. Custom operators, `op_types`, `alias_generator`,
field→column `remapping`, computed columns, and `create_filters_from_model`
include/exclude → [`references/advanced-customization.md`](references/advanced-customization.md).

## Common pitfalls

- **Operator not allowed for the type.** `?active[gt]=...` on a `bool` field is
  rejected — `bool` only gets `eq`/`ne`. Check the type→operator table; widen with
  `FilterField(operators=[...])`.
- **Bracket syntax, not double-underscore.** This library uses `?age[gt]=30`
  (square brackets). `age__gt` is a *different* library's syntax.
- **`in` token vs `in_` member.** Query param is `?id[in]=1,2,3`; the Python enum
  member is `FilterOperator.in_`.
- **You must execute the returned query.** `apply_*` only builds the
  `Select`/`QuerySet`/`FindMany` — run it (`db.scalars`, `await qs`,
  `await q.to_list()`). It doesn't hit the DB itself.
- **Filter field name ≠ DB column.** When the API field and the column differ,
  pass `remapping={"api_field": "db_column"}` to the ext apply functions (or set
  `alias`/`name` on the `FilterField`).
- **`create_sorting` fields must be listed.** Only fields you pass to
  `create_sorting(...)` are sortable; `?sort=+other` for an unlisted field 422s.
- **Wrong sibling library.** `pip install fastapi-filters` (plural, uriyyo) — not
  `fastapi-filter` (singular, arthurio), which has an incompatible API.

## Reference files

- [`references/filters-and-operators.md`](references/filters-and-operators.md) — `FilterField`, `FilterSet`, `create_filters*`, every operator + string value, type→operator rules, query syntax, `FilterValues`
- [`references/sorting.md`](references/sorting.md) — `create_sorting` / `create_sorting_from_model`, `SortingValues`, `?sort=` syntax, nulls, defaults
- [`references/integrations.md`](references/integrations.md) — SQLAlchemy (sync/async), Tortoise, Beanie signatures, `remapping`, `additional`, custom conditions, raw-SQL via `FilterValues`
- [`references/advanced-customization.md`](references/advanced-customization.md) — custom operators/`op_types`, `alias_generator`, `remapping`, computed columns, model-derived filters, internal fields

## Example scripts

- [`examples/quickstart_sqlalchemy.py`](examples/quickstart_sqlalchemy.py) — `FilterSet` + `create_sorting` + async SQLAlchemy `apply_filters_and_sorting`
- [`examples/functional_and_custom_fields.py`](examples/functional_and_custom_fields.py) — functional `create_filters` + `FilterField` with custom operators/alias
- [`examples/tortoise_integration.py`](examples/tortoise_integration.py) — same filters applied to a Tortoise `QuerySet`
