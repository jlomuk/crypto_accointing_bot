import environ

env = environ.Env()
env.read_env()

API_TOKEN = env.str('API_TOKEN', None)
LOGGER_LEVEL = env.str('LOGGER_LEVEL', 'DEBUG')
DSN_DATABASE = f"postgresql+asyncpg://" \
               f"{env.str('POSTGRES_USER')}:{env.str('POSTGRES_PASSWORD')}@" \
               f"{ env.str('POSTGRES_HOST')}:{env.int('POSTGRES_PORT')}/" \
               f"{env.str('POSTGRES_DB')}"
