from typing import TypeVar

from sqlalchemy import select, delete, insert
from sqlalchemy.engine import CursorResult
from sqlalchemy.sql.schema import Table
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from database.db import engine

TableType = TypeVar('TableType', bound=Table)


class BaseCRUD:
    Table: TableType = None

    def __init__(self):
        self.table: TableType = self.Table
        self.connection: AsyncEngine = engine

    async def list(self) -> dict:
        async with self.connection.begin() as conn:
            result: CursorResult = await conn.execute(select(self.table))

        return result.mappings().all()

    async def retrieve(self, pk: int) -> dict:
        async with self.connection.begin() as conn:
            result: CursorResult = await conn.execute(select(self.table).where(self.table.c.id == pk))
        return result.mappings().first()

    async def create(self, data: dict) -> dict:
        async with self.connection.begin() as conn:
            statement = insert(self.table).returning(*self.table.c)
            result: CursorResult = await conn.execute(statement, data)
        return result.mappings().first()

    async def delete(self, pk: int):
        statement = delete(self.table).where(self.table.c.id == pk)
        async with self.connection.begin() as conn:
            await conn.execute(statement)
