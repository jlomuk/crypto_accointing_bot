import asyncio

from database.db import engine
from models import metadata_obj


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all)


if __name__ == '__main__':
    asyncio.run(create_tables())
