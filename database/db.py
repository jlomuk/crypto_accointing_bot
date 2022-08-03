from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from settings import DSN_DATABASE

engine = create_async_engine(DSN_DATABASE + '?prepared_statement_cache_size=0', echo=True, future=True)


# получение асинхронной сессии к БД
async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session

