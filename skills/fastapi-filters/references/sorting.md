# fastapi-filters — Sorting

## create_sorting

```python
from fastapi_filters import SortingValues, create_sorting

@app.get("/users")
async def users(
    sorting: SortingValues = Depends(create_sorting("name", "age", default="-age")),
):
    ...
```

```python
def create_sorting(
    *fields: str | tuple[str, SortingNulls],
    in_: FilterPlace | None = None,
    default: str | list[str] | None = None,
    alias: str | None = None,
) -> SortingResolver: ...
```

- **`*fields`** — the allowed sortable field names. A field may be a plain string
  or a `(name, SortingNulls)` tuple to fix null placement for that field.
- **`default`** — applied when the client sends no `sort` (e.g. `"-age"` or
  `["-age", "+name"]`).
- **`alias`** — rename the `sort` query parameter itself.
- **`in_`** — where to read the param from (`FilterPlace`, e.g. query).
- Returns a `SortingResolver` dependency that yields `SortingValues`.

Only listed fields are sortable; `?sort=+unlisted` returns **422**.

## create_sorting_from_model

```python
from fastapi_filters import create_sorting_from_model

sorting_dep = create_sorting_from_model(
    UserOut,                    # a pydantic BaseModel — fields become sortable
    default="-created_at",
    include={"name", "age"},    # or exclude={...}
)
```

```python
def create_sorting_from_model(
    model: type[BaseModel],
    *,
    default: str | None = None,
    in_: FilterPlace | None = None,
    include: Container[str] | None = None,
    exclude: Container[str] | None = None,
) -> SortingResolver: ...
```

## The `sort` query parameter

```
?sort=+age            # ascending
?sort=-age            # descending
?sort=age             # bare = ascending
?sort=+age,-name      # CSV; priority is left-to-right (age first, then name)
```

## SortingValues

The resolved value is a **list of tuples** `(field_name, nulls, direction)`,
in priority order. `direction` is ascending/descending; `nulls` controls
NULL placement (nulls-first / nulls-last) where the backend supports it.

Pass `SortingValues` straight to an ext `apply_sorting(query, sorting)` or
`apply_filters_and_sorting(query, filters, sorting)`:

```python
from fastapi_filters.ext.sqlalchemy import apply_sorting
stmt = apply_sorting(select(User), sorting)
```

For an unsupported backend, iterate the tuples and build your own `ORDER BY`.

## Notes

- **Combine with filters in one call.** `apply_filters_and_sorting(stmt, filters,
  sorting)` is the common path; the separate `apply_filters` / `apply_sorting`
  exist for when you only need one.
- **Field names vs columns.** If a sortable field name differs from the DB
  column, use the ext `remapping={"field": "column"}` argument (see
  `references/integrations.md`).
- **Stable ordering.** Add a unique tiebreaker (e.g. `id`) to `create_sorting`
  and/or `default` so equal values sort deterministically.
