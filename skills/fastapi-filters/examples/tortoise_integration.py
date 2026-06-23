#!/usr/bin/env python3
"""Same fastapi-filters declarations, applied to a Tortoise ORM QuerySet.

The ext API is uniform across backends: apply_filters_and_sorting(query, filters,
sorting) takes the backend's query object and returns it. For Tortoise the query
object is a QuerySet, which you await to execute.

Try:
    GET /users?name[ilike]=user1&age[ge]=20&sort=-age

Run:
    pip install fastapi-filters "tortoise-orm" uvicorn
    uvicorn tortoise_integration:app --reload
"""
from __future__ import annotations

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from tortoise.models import Model

from fastapi_filters import FilterField, FilterSet, SortingValues, create_sorting
from fastapi_filters.ext.tortoise import apply_filters_and_sorting


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    age = fields.IntField()

    class Meta:
        table = "users"


class UserOut(BaseModel):
    id: int
    name: str
    age: int


class UserFilters(FilterSet):
    name: FilterField[str]
    age: FilterField[int]


app = FastAPI()


@app.get("/users")
async def get_users(
    filters: UserFilters = Depends(),
    sorting: SortingValues = Depends(create_sorting("name", "age", default="+id")),
) -> list[UserOut]:
    qs = apply_filters_and_sorting(User.all(), filters, sorting)
    return [UserOut(id=u.id, name=u.name, age=u.age) for u in await qs]


# In-memory SQLite; generate_schemas creates the table on startup.
register_tortoise(
    app,
    db_url="sqlite://:memory:",
    modules={"models": [__name__]},
    generate_schemas=True,
)
