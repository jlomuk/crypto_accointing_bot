import environ
from utils.logging.logger import setup_logger

env = environ.Env()
env.read_env()



API_TOKEN_TELEGRAM = env.str('API_TOKEN_TELEGRAM', None)
LOGGER_LEVEL = env.str('LOGGER_LEVEL', 'DEBUG')
DSN_DATABASE = f"postgresql+asyncpg://" \
               f"{env.str('POSTGRES_USER')}:{env.str('POSTGRES_PASSWORD')}@" \
               f"{ env.str('POSTGRES_HOST')}:{env.int('POSTGRES_PORT')}/" \
               f"{env.str('POSTGRES_DB')}"

API_TOKEN_COINMARKETCAP = env.str('API_TOKEN_COINMARKETCAP', None)


setup_logger(LOGGER_LEVEL)