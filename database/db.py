from sqlalchemy.ext.asyncio import create_async_engine

from settings import DSN_DATABASE

engine = create_async_engine(DSN_DATABASE + '?prepared_statement_cache_size=0', echo=True, future=True)

