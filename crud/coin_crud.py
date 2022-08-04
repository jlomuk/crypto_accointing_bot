from sqlalchemy import select, delete
from sqlalchemy.engine import CursorResult

from .base_crud import BaseCRUD
from models.coin import coin


class CoinCRUD(BaseCRUD):
    Table = coin

    async def retrieve(self, shortcut: str) -> dict:
        async with self.connection.begin() as conn:
            result: CursorResult = await conn.execute(select(self.table).where(self.table.c.shortcut == shortcut))
            return result.mappings().first()

    async def delete(self, shortcut: str):
        statement = delete(self.table).where(self.table.c.shortcut == shortcut)
        async with self.connection.begin() as conn:
            await conn.execute(statement)
