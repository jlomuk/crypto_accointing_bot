from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from sqlalchemy.exc import NoResultFound
from loguru import logger

from keyboards.reply_keyboard import action_crypto_buttons, action_list_crypto_buttons, confirm_crypto_buttons, \
    cancel_button
from schemas.base import Contex
from schemas.coin_schemas import GetCoinRequest, DeleteCoinRequest, CreateCoinRequest
from services.coin_service import CoinService
from loader import dp, jinja_env
from states import states


@dp.message_handler(lambda message: message.text.lower() == 'криптомонеты')
async def get_menu_coins(message: Message):
    return await message.reply('Выберите действие', reply_markup=action_list_crypto_buttons)


# ================ Обработчик для получения списка монет =======================
@dp.message_handler(lambda message: message.text.lower() == 'список криптомонет')
async def list_coins(message: Message):
    coins = await CoinService().list_coin()
    template = jinja_env.get_template('coins/list_coins.html')
    response = Contex(data=coins, func=enumerate)
    return await message.reply(template.render(response.dict()), reply_markup=action_crypto_buttons)


# ================ Обработчик для получения конкретной монеты ==================
@dp.message_handler(lambda message: message.text.startswith('/get_coin'))
async def get_coin(message: Message):
    coin_req = GetCoinRequest(shortcut=message.text)

    try:
        coin = await CoinService().get_coin(coin_req)
    except NoResultFound:
        return await message.reply("<b>Данной монеты нет в базе</b>", reply_markup=ReplyKeyboardRemove())

    template = jinja_env.get_template('coins/get_coin.html')
    context = Contex(data=coin)
    return await message.reply(template.render(context.dict()), reply_markup=ReplyKeyboardRemove())


# ================ Обработчики для добавления монеты ==========================================
@dp.message_handler(lambda message: message.text.lower() == 'добавить криптомонету')
async def add_cryptocoin(message: Message):
    await states.CreateCoinStates.name.set()
    return await message.reply('Введите название новой монеты', reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower() != 'отмена', state=states.CreateCoinStates.name)
async def add_process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await states.CreateCoinStates.next()
    return await message.reply('Введите краткое название монеты', reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower() != 'отмена', state=states.CreateCoinStates.shortcut)
async def add_process_shortcut(message: Message, state: FSMContext):
    await state.update_data(shortcut=message.text)

    async with state.proxy() as data:
        coin_req = CreateCoinRequest(**data)
    try:
        added_coin = await CoinService().create_coin(coin_req)
    except:
        return await message.reply('Невозможно добавить монету', reply_markup=action_list_crypto_buttons)
    finally:
        await state.finish()

    template = jinja_env.get_template('coins/add_coin.html')
    context = Contex(data=added_coin)
    return await message.reply(template.render(context.dict()), reply_markup=action_list_crypto_buttons)


# ================ Обработчики для удаления монеты =============================
@dp.message_handler(lambda message: message.text.lower() == 'удалить криптомонету')
async def destroy_cryptocoin(message: Message):
    await states.DeleteCoinStates.shortcut.set()
    return await message.reply('Введите краткое название монеты для ее удаления', reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower() != 'отмена', state=states.DeleteCoinStates.shortcut)
async def destroy_process_shortcut(message: Message, state: FSMContext):
    coin_req = DeleteCoinRequest(shortcut=message.text)

    try:
        coin = await CoinService().get_coin(coin_req)
    except NoResultFound:
        await state.finish()
        return await message.reply("<b>Данной монеты нет в базе</b>", reply_markup=action_list_crypto_buttons)

    await state.update_data(shortcut=message.text)
    await states.DeleteCoinStates.next()

    template = jinja_env.get_template('coins/delete_coin.html')
    context = Contex(data=coin)
    return await message.reply(template.render(context.dict()), reply_markup=confirm_crypto_buttons)


@dp.message_handler(Text(equals='Подтвердить', ignore_case=True), state=states.DeleteCoinStates.delete_coin)
async def destroy_process_confirm(message: Message, state: FSMContext):
    async with state.proxy() as data:
        coin_req = DeleteCoinRequest(shortcut=data.get('shortcut'))

    try:
        await CoinService().delete_coin(coin_req)
    except:
        return await message.reply('Невозможно удалить монету', reply_markup=action_list_crypto_buttons)
    finally:
        await state.finish()

    return await message.reply('Монета успешно удалена!', reply_markup=action_list_crypto_buttons)
