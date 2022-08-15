from sqlalchemy import select
from sqlalchemy.engine import CursorResult

from .base import BaseRepository
from models.order import order


class OrderRepository(BaseRepository):
    Table = order

    async def list(self, shortcut: str) -> dict:
        async with self.connection.begin() as conn:
            result: CursorResult = await conn.execute(select(self.table).where(self.table.c.shortcut == shortcut))
            return result.mappings().all()

