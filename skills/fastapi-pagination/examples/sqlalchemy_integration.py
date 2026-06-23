#!/usr/bin/env python3
"""Async SQLAlchemy pagination with an ORM -> schema transformer.

Key points:
  * Import `paginate` from `fastapi_pagination.ext.sqlalchemy` (NOT the built-in
    one) so LIMIT/OFFSET + count run in the database.
  * With an AsyncSession the ext `paginate` is awaitable -> `await` it.
  * The `transformer=` converts ORM `User` rows into the `UserOut` schema after
    the page is fetched (one bulk conversion, no N+1).

Run:
    pip install "fastapi-pagination[sqlalchemy]" sqlalchemy aiosqlite uvicorn
    uvicorn sqlalchemy_integration:app --reload
    # GET http://127.0.0.1:8000/users?page=1&size=10
"""
from __future__ import annotations

from collections.abc import AsyncIterator

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy import String, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

engine = create_async_engine("sqlite+aiosqlite:///:memory:")
Session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[str] = mapped_column(String(50))


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    surname: str


async def get_db() -> AsyncIterator[AsyncSession]:
    async with Session() as session:
        yield session


app = FastAPI()


@app.on_event("startup")
async def seed() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with Session() as s:
        s.add_all(User(name=f"user{i}", surname=f"sur{i}") for i in range(50))
        await s.commit()


@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)) -> Page[UserOut]:
    return await paginate(
        db,
        select(User).order_by(User.id),
        transformer=lambda rows: [UserOut.model_validate(r) for r in rows],
    )


add_pagination(app)
