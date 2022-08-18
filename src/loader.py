from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from jinja2 import Environment, select_autoescape, FileSystemLoader
from utils.helpers import format_price, format_capitalization

from settings import API_TOKEN_TELEGRAM

storage = MemoryStorage()
dp: Dispatcher | None = None
jinja_env: Environment | None = None


def setup_jinja():
    global jinja_env
    if jinja_env is not None:
        return jinja_env

    jinja_env = Environment(
        loader=FileSystemLoader("src/templates"),
        autoescape=select_autoescape()
    )
    jinja_env.filters['format_price'] = format_price
    jinja_env.filters['format_capitalization'] = format_capitalization


def setup_bot():
    global dp
    if dp is not None:
        return dp
    bot = Bot(token=API_TOKEN_TELEGRAM, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)
    return dp
