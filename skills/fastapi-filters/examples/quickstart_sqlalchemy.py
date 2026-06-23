#!/usr/bin/env python3
"""FilterSet + sorting applied to an async SQLAlchemy query.

Declaring a FilterSet of FilterField[T] auto-generates the ?field[op]=value query
params; create_sorting(...) adds ?sort=±field. apply_filters_and_sorting() turns
them into WHERE / ORDER BY on a Select that you then execute.

Try:
    GET /users?name[ilike]=st&age[gt]=20&age[le]=40&sort=-age,+name
    GET /users?id[in]=1,2,3

Run:
    pip install fastapi-filters sqlalchemy aiosqlite uvicorn
    uvicorn quickstart_sqlalchemy:app --reload
"""
from __future__ import annotations

from collections.abc import AsyncIterator

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy import String, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from fastapi_filters import FilterField, FilterSet, SortingValues, create_sorting
from fastapi_filters.ext.sqlalchemy import apply_filters_and_sorting

engine = create_async_engine("sqlite+aiosqlite:///:memory:")
Session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    surname: str
    age: int


class UserFilters(FilterSet):
    name: FilterField[str]          # str -> eq, ne, in, not_in, like, ilike, not_like, not_ilike
    surname: FilterField[str]
    age: FilterField[int]           # int -> base + gt, ge, lt, le
    id: FilterField[int]


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
            User(name=f"name{i}", surname=f"sur{i}", age=18 + (i * 3) % 40)
            for i in range(30)
        )
        await s.commit()


@app.get("/users")
async def get_users(
    db: AsyncSession = Depends(get_db),
    filters: UserFilters = Depends(),
    sorting: SortingValues = Depends(create_sorting("name", "age", default="+id")),
) -> list[UserOut]:
    stmt = apply_filters_and_sorting(select(User), filters, sorting)
    return list((await db.scalars(stmt)).all())
