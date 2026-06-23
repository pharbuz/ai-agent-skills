# fastapi-filters — Backend integrations

Every ext module exposes the same three functions. They take the backend's query
object plus the resolved `filters` (a `FilterValues` or a `FilterSet` instance)
and `sorting` (`SortingValues`), and **return the same query type** — you execute
it yourself.

```python
apply_filters(query, filters, *, remapping=None, ...)                 -> query
apply_sorting(query, sorting, *, remapping=None, ...)                 -> query
apply_filters_and_sorting(query, filters, sorting, *, remapping=None) -> query
```

`remapping={"api_field": "db_column"}` maps a filter/sort field name onto a
different column when they differ.

## SQLAlchemy — `fastapi_filters.ext.sqlalchemy`

Works with both sync and async sessions; you get back a `Select` to execute.

```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_filters import FilterSet, FilterField, SortingValues, create_sorting
from fastapi_filters.ext.sqlalchemy import apply_filters_and_sorting

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

Full signatures:

```python
def apply_filters(
    stmt, filters, *,
    remapping=None,            # {field: column}
    additional=None,          # extra named columns/expressions to filter on
    apply_filter=None,        # custom per-filter application hook
    add_condition=None,       # custom condition builder hook
) -> stmt
def apply_sorting(stmt, sorting, *, remapping=None, additional=None) -> stmt
def apply_filters_and_sorting(stmt, filters, sorting, *, remapping=None,
                              additional=None, apply_filter=None, add_condition=None) -> stmt
```

Extra exports: `create_filters_from_orm`, `create_sorting_from_orm` (derive
filters/sorting straight from an ORM model), plus `custom_apply_filter`,
`custom_add_condition`, `generic_condition`, `adapt_sqlalchemy_column_type` for
advanced hooks (see `references/advanced-customization.md`).

```python
# Derive filters from the ORM model instead of writing a FilterSet
from fastapi_filters.ext.sqlalchemy import create_filters_from_orm, create_sorting_from_orm
UserFilters = create_filters_from_orm(User)            # use: filters=Depends(UserFilters)
sorting_dep = create_sorting_from_orm(User)
```

## Tortoise ORM — `fastapi_filters.ext.tortoise`

```python
from fastapi_filters.ext.tortoise import apply_filters_and_sorting

@app.get("/users")
async def get_users(
    filters: UserFilters = Depends(),
    sorting: SortingValues = Depends(create_sorting("name", "age")),
) -> list[UserOut]:
    qs = apply_filters_and_sorting(User.all(), filters, sorting)   # -> QuerySet
    return await qs
```

Signatures: `apply_filters(qs, filters, *, remapping=None)`,
`apply_sorting(qs, sorting, remapping=None)`,
`apply_filters_and_sorting(qs, filters, sorting, *, remapping=None)`.
First arg is a Tortoise `QuerySet`; awaiting it runs the query.

## Beanie (MongoDB) — `fastapi_filters.ext.beanie`

```python
from fastapi_filters.ext.beanie import apply_filters_and_sorting

@app.get("/users")
async def get_users(
    filters: UserFilters = Depends(),
    sorting: SortingValues = Depends(create_sorting("name", "age")),
) -> list[UserOut]:
    q = apply_filters_and_sorting(User.find(), filters, sorting)   # -> FindMany
    return await q.to_list()
```

Same signature shape; first arg is a Beanie `FindMany` query
(`Document.find(...)`).

## Raw SQL / unsupported backends

No ext module ships for raw SQL, but `FilterValues` and `SortingValues` are plain
data — iterate them to build whatever query you need:

```python
filters_dep = create_filters(name=str, age=int)

@app.get("/users")
async def get_users(filters=Depends(filters_dep), sorting=Depends(create_sorting("age"))):
    where, params = [], {}
    for field, ops in filters.items():          # field -> {operator: value}
        for op, value in ops.items():
            where.append(build_sql_condition(field, op, value))   # your mapping
            params[field] = value
    order = ", ".join(f"{f} {'DESC' if desc else 'ASC'}" for f, _nulls, desc in sorting)
    ...
```

The exact `FilterValues` structure (field → operator → value) is what the ext
modules consume internally; treat the ext source as the reference implementation
when writing your own adapter.

## Notes

- **Always execute the result.** `apply_*` is pure query-building. Run it with
  `db.scalars(...)` (SQLAlchemy), `await qs` (Tortoise), `await q.to_list()`
  (Beanie).
- **`filters` accepts a `FilterSet` or `FilterValues`.** A `Depends()`-resolved
  `FilterSet` instance works directly; so does the dict from `create_filters`.
- **`remapping` is the quick field→column fix;** for computed/derived columns use
  the SQLAlchemy `additional` namespace or the custom-condition hooks.
