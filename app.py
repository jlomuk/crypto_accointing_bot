from aiogram import executor
from loguru import logger

if __name__ == '__main__':
    from loader import setup_bot
    dp = setup_bot()
    import handlers

    logger.info('Starting app....')
    executor.start_polling(dispatcher=dp, skip_updates=True)
