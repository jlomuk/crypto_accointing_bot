from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loguru import logger

from keyboards.reply_keyboard import menu_buttons
from loader import dp, jinja_env


@dp.message_handler(Command(['menu', 'меню'], ignore_case=True))
async def test(message: Message):
    template = jinja_env.get_template('index.html')
    return await message.reply(template.render(), reply_markup=menu_buttons)


@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    message = await message.reply('Отмена', reply_markup=menu_buttons)

    if current_state is None:
        logger.info("Canceling..... State already empty")
        return message

    await state.finish()
    logger.info("Canceling..... State is reset")
    return message
