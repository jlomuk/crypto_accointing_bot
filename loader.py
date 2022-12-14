from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from jinja2 import Environment, select_autoescape, FileSystemLoader

from settings import API_TOKEN

storage = MemoryStorage()
dp: Dispatcher | None = None

jinja_env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)


def setup_bot():
    global dp
    if not dp is None:
        return dp
    bot = Bot(token=API_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)
    return dp
