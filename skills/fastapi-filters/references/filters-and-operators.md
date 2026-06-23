# fastapi-filters — Filters & operators

## Defining filters

### FilterSet (class API)

```python
from fastapi_filters import FilterField, FilterSet

class UserFilters(FilterSet):
    name: FilterField[str]
    surname: FilterField[str]
    age: FilterField[int]
    is_active: FilterField[bool]
    tags: FilterField[list[str]]
```

Inject with `filters: UserFilters = Depends()`. The instance is accepted directly
by the ext `apply_filters(...)` functions.

### create_filters (functional API)

```python
from fastapi_filters import create_filters, FilterField

filters_dep = create_filters(
    name=str,                       # name -> type
    age=int,
    email=FilterField(str, alias="mail"),   # or name -> FilterField instance
)

@app.get("/users")
async def users(filters=Depends(filters_dep)):
    ...
```

`create_filters(*, in_=None, alias_generator=None, hooks=None, **kwargs)` —
kwargs map field name → a type **or** a `FilterField`. Returns a
`FiltersResolver` (a FastAPI dependency) that yields `FilterValues`.

### create_filters_from_model

```python
from fastapi_filters import create_filters_from_model

filters_dep = create_filters_from_model(
    UserOut,                        # a pydantic BaseModel
    include={"name", "age"},        # or exclude=...
    age=FilterField(int, operators=[Op.gt, Op.lt]),   # **overrides per field
)
```

`create_filters_from_model(model, *, in_=None, alias_generator=None,
include=None, exclude=None, hooks=None, **overrides)`.

## FilterField

```python
FilterField(
    type=None,                 # the value type (inferred from FilterField[T] in a FilterSet)
    operators=None,            # explicit allowed operators (else derived from type)
    default_op=None,           # operator used when client omits [op] (eq, or overlap for sequences)
    name=None,                 # internal field name
    alias=None,                # query-param name exposed to clients
    internal=False,            # hide from generated query params (set programmatically)
    op_types=None,             # per-operator value type overrides, e.g. {Op.in_: list[int]}
)
```

```python
from fastapi_filters import FilterField, FilterOperator as Op

class ProductFilters(FilterSet):
    # only eq + ilike, exposed as ?title[...]
    name: FilterField[str] = FilterField(operators=[Op.eq, Op.ilike], alias="title")
    # bare ?q=foo behaves as ilike
    q: FilterField[str] = FilterField(default_op=Op.ilike)
```

## Operators (`FilterOperator`)

17 operators; the **string in the column** is the URL token used as `?field[token]=`.

| Member | URL token | Meaning |
|---|---|---|
| `eq` | `eq` | equal |
| `ne` | `ne` | not equal |
| `gt` `ge` `lt` `le` | `gt` `ge` `lt` `le` | `> ≥ < ≤` |
| `like` `not_like` | `like` `not_like` | SQL LIKE (case-sensitive) |
| `ilike` `not_ilike` | `ilike` `not_ilike` | case-insensitive LIKE |
| `in_` | **`in`** | value in CSV list |
| `not_in` | `not_in` | value not in CSV list |
| `is_null` | `is_null` | IS NULL / IS NOT NULL (bool value) |
| `overlap` `not_overlap` | `overlap` `not_overlap` | array overlap (any common element) |
| `contains` `not_contains` | `contains` `not_contains` | array contains all CSV elements |

### Type → default operators

When `operators` isn't set explicitly, they're derived from the field type:

- **All types:** `eq`, `ne`, `in`, `not_in`
- **`str`:** the above **+** `like`, `ilike`, `not_like`, `not_ilike`
- **numeric** (`int`, `float`, `date`, `datetime`, `timedelta`): the base **+**
  `gt`, `ge`, `lt`, `le`
- **`bool`:** `eq`, `ne` **only**
- **sequence** (`list[...]`, etc.): `overlap`, `not_overlap`, `contains`,
  `not_contains` **only**
- **`Optional[...]`:** additionally `is_null`

## Query-parameter syntax

```
?field[op]=value
?name[eq]=Steve
?name[ilike]=ste                # case-insensitive substring
?age[gt]=30&age[le]=40          # combine operators on one field (AND)
?id[in]=1,2,3                   # CSV for in / not_in / overlap / contains
?deleted_at[is_null]=true       # nullable fields only
?tags[contains]=python,fastapi  # sequence fields
```

- Multiple operators on the same field combine with **AND**.
- `default_op` lets clients drop the bracket: with `default_op=Op.ilike`,
  `?name=foo` == `?name[ilike]=foo`.

## FilterValues

The resolved object handed to the ext layer (also what `create_filters`'
dependency yields): a mapping of **field → operator → value**. Pass it — or the
`FilterSet` instance — directly into `apply_filters(...)`. To build a query for an
unsupported backend, iterate it yourself (see `references/integrations.md`).
