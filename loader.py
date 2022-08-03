from aiogram import Bot, Dispatcher

from settings import API_TOKEN

dp: Dispatcher | None = None


def setup_bot():
    global dp
    if not dp is None:
        return dp
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    return dp
