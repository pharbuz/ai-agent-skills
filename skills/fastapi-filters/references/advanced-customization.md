# fastapi-filters — Advanced customization

## Restricting / extending operators per field

```python
from fastapi_filters import FilterField, FilterSet, FilterOperator as Op

class ProductFilters(FilterSet):
    # only these operators are accepted for `name`
    name: FilterField[str] = FilterField(operators=[Op.eq, Op.ilike])
    # add is_null even though the annotation isn't Optional
    deleted_at: FilterField[datetime] = FilterField(operators=[Op.is_null, Op.lt])
```

If `operators` is omitted, they're derived from the field type (see
`references/filters-and-operators.md`).

## default_op — operator when the client omits `[op]`

```python
# ?q=foo  behaves as  ?q[ilike]=foo
q: FilterField[str] = FilterField(default_op=Op.ilike)
```

Default is `eq` (or `overlap` for sequence types).

## Aliases & alias_generator

Expose a field under a different query-param name:

```python
email: FilterField[str] = FilterField(alias="mail")     # ?mail[eq]=...
```

Generate aliases for all fields at once (functional API):

```python
from fastapi_filters import create_filters

def camel(name: str) -> str:
    head, *rest = name.split("_")
    return head + "".join(w.capitalize() for w in rest)

filters_dep = create_filters(first_name=str, last_name=str, alias_generator=camel)
# -> ?firstName[eq]=...&lastName[eq]=...
```

## op_types — per-operator value type

Override the parsed type for a specific operator (e.g. `in` takes a list of ints
while `eq` takes one int):

```python
age: FilterField[int] = FilterField(op_types={Op.in_: list[int], Op.not_in: list[int]})
```

## internal fields

`FilterField(internal=True)` keeps a field out of the generated query params —
useful when you set its value server-side (tenant scoping, soft-delete) rather
than exposing it to clients.

## Field → column remapping (ext layer)

When the API field name differs from the DB column, remap at apply time:

```python
from fastapi_filters.ext.sqlalchemy import apply_filters_and_sorting

stmt = apply_filters_and_sorting(
    select(User), filters, sorting,
    remapping={"name": "full_name", "joined": "created_at"},
)
```

## additional namespace — filter on computed columns (SQLAlchemy)

Expose expressions that aren't plain mapped columns to the filter/sort layer:

```python
from sqlalchemy import func
stmt = apply_filters_and_sorting(
    select(User), filters, sorting,
    additional={"full_name": func.concat(User.first_name, " ", User.last_name)},
)
# now ?full_name[ilike]=... and sort=full_name work
```

## Custom condition hooks (SQLAlchemy)

For operators/columns that need bespoke SQL, pass `apply_filter=` /
`add_condition=`, or use the provided helpers:

```python
from fastapi_filters.ext.sqlalchemy import (
    custom_apply_filter, custom_add_condition, generic_condition,
)
```

- `apply_filter=` — full control over how a single resolved filter is applied to
  the statement.
- `add_condition=` — customize how a built condition is attached (e.g. `having`
  vs `where`, OR-grouping).
- `generic_condition` — the default condition builder, reusable inside your hook.
- `adapt_sqlalchemy_column_type` — coerce values to a column's SQL type.

## Deriving filters/sorting from models

```python
from fastapi_filters import create_filters_from_model, create_sorting_from_model
from fastapi_filters.ext.sqlalchemy import create_filters_from_orm, create_sorting_from_orm

# from a Pydantic model
UserFilters = create_filters_from_model(UserOut, include={"name", "age"})
# from a SQLAlchemy ORM model
UserFilters = create_filters_from_orm(User, exclude={"password_hash"})
```

`include` / `exclude` select which fields become filterable/sortable;
`**overrides` (filters) let you replace individual fields with a tuned
`FilterField`.

## hooks (functional create_filters)

`create_filters(..., hooks=...)` accepts a `FiltersCreateHooks` object to
intercept field/operator generation — reach for it when you need to programmatically
add, drop, or rewrite fields across a whole filter set rather than per field.

## Notes

- **Prefer `FilterField` options and `remapping`** for the common 90% (limit
  operators, rename, map to a column). Reach for `additional` / custom hooks only
  for computed columns or non-trivial SQL.
- **Keep client-facing names stable** via `alias` so refactors of internal field
  or column names don't break the API contract.
