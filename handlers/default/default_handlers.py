from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.reply_keyboard import menu_buttons
from loader import dp, jinja_env


@dp.message_handler(Command('menu', ignore_case=True))
async def test(message: Message):
    template = jinja_env.get_template('index.html')
    return await message.reply(template.render(), reply_markup=menu_buttons)


@dp.message_handler(text='Отмена')
async def cancel(message: Message):
    return await message.reply('Отмена', reply_markup=ReplyKeyboardRemove())
