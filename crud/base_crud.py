from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.engine import CursorResult
from sqlalchemy.sql.schema import Table
from sqlalchemy.ext.asyncio.engine import AsyncEngine, AsyncConnection
from database.db import engine
import asyncio
from models.coin import coin

TableType = TypeVar('TableType', bound=Table)


class BaseCRUD:
    Table = None

    def __init__(self):
        self.table: TableType = self.Table
        self.connection: AsyncEngine = engine

    async def list(self) -> dict:
        async with self.connection.begin() as conn:
            print(self.table)
            result: CursorResult = await conn.execute(select(self.table))
            return result.mappings().all()

    async def retrieve(self, db_session):
        ...

    async def create(self, db_session):
        ...

    async def delete(self, db_session):
        ...


