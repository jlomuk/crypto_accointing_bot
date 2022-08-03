from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.reply_keyboard import action_crypto_buttons

from loader import dp


@dp.message_handler(lambda message: message.text.lower() == 'криптомонеты')
async def add_delete_handler(message: Message):
    return await message.reply('Выберите действие', reply_markup=action_crypto_buttons)


@dp.message_handler(lambda message: message.text.lower() == 'список криптомонет')
async def list_cryptocoin_handler(message: Message):
    return await message.reply('Список!!!!', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text.lower() == 'добавить криптомонету')
async def add_cryptocoin_handler(message: Message):
    return await message.reply('Добавить!!!!', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text.lower() == 'удалить криптомонету')
async def destroy_cryptocoin_handler(message: Message):
    return await message.reply('Удалить!!!', reply_markup=ReplyKeyboardRemove())
