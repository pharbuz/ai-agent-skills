#!/usr/bin/env python3
"""Minimal fastapi-pagination app: Page[T] + in-memory paginate.

The built-in `paginate` is for in-memory sequences (lists, ranges, tuples).
Declaring `-> Page[UserOut]` adds the ?page=&size= query params and sets the
response shape; `add_pagination(app)` wires the params dependency.

Run:
    pip install fastapi-pagination uvicorn
    uvicorn quickstart_inmemory:app --reload
    # then GET http://127.0.0.1:8000/users?page=1&size=2
    # docs at  http://127.0.0.1:8000/docs
"""
from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from fastapi_pagination import Page, add_pagination, paginate

app = FastAPI()


class UserOut(BaseModel):
    name: str
    surname: str


USERS = [
    UserOut(name="Steve", surname="Rogers"),
    UserOut(name="Tony", surname="Stark"),
    UserOut(name="Natasha", surname="Romanoff"),
    UserOut(name="Bruce", surname="Banner"),
    UserOut(name="Wanda", surname="Maximoff"),
]


@app.get("/users")
async def get_users() -> Page[UserOut]:
    # paginate() reads ?page= & ?size= from the request context and slices USERS.
    return paginate(USERS)


# Required: registers the pagination params dependency on the routes.
add_pagination(app)
