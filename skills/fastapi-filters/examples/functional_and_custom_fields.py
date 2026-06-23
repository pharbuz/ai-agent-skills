#!/usr/bin/env python3
"""Functional create_filters() API + customized FilterField.

When you don't want a FilterSet class, build the dependency with create_filters()
mapping name -> type or name -> FilterField. FilterField customizes a field:
restrict operators, rename the query param (alias), or set the default operator
used when the client omits the [op] bracket.

Try:
    GET /users?mail[ilike]=gmail        # 'email' field exposed as ?mail[...]
    GET /users?name=steve               # default_op=ilike -> ?name[ilike]=steve
    GET /users?age[gt]=18&age[lt]=65    # age restricted to gt/lt only

Run:
    pip install fastapi-filters sqlalchemy aiosqlite uvicorn
    uvicorn functional_and_custom_fields:app --reload
"""
from __future__ import annotations

from collections.abc import AsyncIterator

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy import String, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from fastapi_filters import (
    FilterField,
    FilterOperator as Op,
    SortingValues,
    create_filters,
    create_sorting,
)
from fastapi_filters.ext.sqlalchemy import apply_filters_and_sorting

engine = create_async_engine("sqlite+aiosqlite:///:memory:")
Session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120))
    age: Mapped[int] = mapped_column()


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: str
    age: int


# Functional filters: name -> type, or name -> FilterField for customization.
user_filters = create_filters(
    name=FilterField(str, default_op=Op.ilike),               # bare ?name= == ?name[ilike]=
    email=FilterField(str, operators=[Op.eq, Op.ilike], alias="mail"),  # exposed as ?mail[...]
    age=FilterField(int, operators=[Op.gt, Op.lt]),           # only gt / lt
)


async def get_db() -> AsyncIterator[AsyncSession]:
    async with Session() as session:
        yield session


app = FastAPI()


@app.on_event("startup")
async def seed() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with Session() as s:
        s.add_all(
            User(name=f"user{i}", email=f"user{i}@gmail.com", age=18 + i)
            for i in range(20)
        )
        await s.commit()


@app.get("/users")
async def get_users(
    db: AsyncSession = Depends(get_db),
    filters=Depends(user_filters),
    sorting: SortingValues = Depends(create_sorting("name", "age", default="+id")),
) -> list[UserOut]:
    stmt = apply_filters_and_sorting(select(User), filters, sorting)
    return list((await db.scalars(stmt)).all())
