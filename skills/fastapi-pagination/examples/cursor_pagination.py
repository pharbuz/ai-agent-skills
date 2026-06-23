#!/usr/bin/env python3
"""Cursor-based pagination over an ordered SQLAlchemy query.

Cursor pagination is stateless and stays O(1) on deep pages (no growing OFFSET).
The query MUST have a deterministic ORDER BY because the cursor encodes the sort
position. SQLAlchemy cursor paging relies on the `sqlakeyset` library.

Response carries `next_page` / `previous_page` cursor tokens; pass the token back
as ?cursor=<token> to fetch the adjacent page.

Run:
    pip install "fastapi-pagination[sqlalchemy]" sqlalchemy uvicorn
    uvicorn cursor_pagination:app --reload
    # GET http://127.0.0.1:8000/items?size=10   then follow `next_page`:
    # GET http://127.0.0.1:8000/items?size=10&cursor=<next_page token>
"""
from __future__ import annotations

from collections.abc import Iterator

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from fastapi_pagination import add_pagination
from fastapi_pagination.cursor import CursorPage
from fastapi_pagination.ext.sqlalchemy import paginate

engine = create_engine("sqlite:///:memory:")


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))


class ItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str


def get_db() -> Iterator[Session]:
    with Session(engine) as session:
        yield session


app = FastAPI()


@app.on_event("startup")
def seed() -> None:
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all(Item(title=f"item-{i}") for i in range(100))
        s.commit()


@app.get("/items")
def list_items(db: Session = Depends(get_db)) -> CursorPage[ItemOut]:
    # ORDER BY a unique column so the cursor position is stable.
    return paginate(db, select(Item).order_by(Item.id))


add_pagination(app)
