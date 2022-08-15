from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from loguru import logger

from keyboards.default_keyboard import cancel_button
from services.order_service import OrderService
from schemas.order_schemas import GetOrderRequest, AddOrderRequest, DeleteOrderRequest
from keyboards.order_keyboard import action_order_buttons, type_action_order, delete_order_buttons
from states.states import GetOrderStates, AddOrderStates, DeleteOrderStates
from adapters.order import OrderRepository
from adapters.coin import CoinRepository
from loader import dp, jinja_env
from schemas.base import Contex


@dp.message_handler(Text(equals='Покупки и продажи криптомонет', ignore_case=True))
async def get_menu_orders(message: Message) -> Message:
    return await message.reply('Выберите действие', reply_markup=action_order_buttons)


# ================ Обработчики для получения списка ордеров =======================
@dp.message_handler(Text(equals='Список всех ордеров по монете', ignore_case=True))
async def get_order(message: Message) -> Message:
    shortcuts = await OrderRepository().distinct_shortcuts()
    await GetOrderStates.shortcut.set()

    template = jinja_env.get_template('orders/get_shortcuts.html')
    context = Contex(data=shortcuts, func=enumerate)
    return await message.reply(template.render(context.dict()), reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower != 'отмена', state=GetOrderStates.shortcut)
async def get_order_process_shortcut(message: Message, state: FSMContext) -> Message:
    order_req = GetOrderRequest(shortcut=message.text)
    order_repo = OrderRepository()
    orders = await OrderService(order_repo).list_orders(order_req)
    await state.finish()

    template = jinja_env.get_template('orders/get_orders.html')
    context = Contex(data=orders, func=enumerate)
    return await message.reply(template.render(context.dict()), reply_markup=delete_order_buttons)


# ================ Обработчики для добаления ордера ===============================
@dp.message_handler(Text(equals='Добавить ордер', ignore_case=True))
async def add_order(message: Message) -> Message:
    await AddOrderStates.action.set()

    return await message.reply('Выберите действие', reply_markup=type_action_order)


@dp.message_handler(lambda message: message.text.lower != 'отмена', state=AddOrderStates.action)
async def add_order_process_action(message: Message, state: FSMContext) -> Message:
    await state.update_data(action=message.text.title())
    await AddOrderStates.next()

    shortcuts = await CoinRepository().distinct_shortcuts()
    template = jinja_env.get_template('orders/get_shortcuts.html')
    context = Contex(data=shortcuts, func=enumerate)

    return await message.reply(template.render(context.dict()), reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower != 'отмена', state=AddOrderStates.shortcut)
async def add_order_process_shortcut(message: Message, state: FSMContext) -> Message:
    await state.update_data(shortcut=message.text.upper())
    await AddOrderStates.next()
    return await message.reply('Введите количество монет', reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower != 'отмена', state=AddOrderStates.count)
async def add_order_process_count(message: Message, state: FSMContext) -> Message:
    await state.update_data(count=message.text)
    await AddOrderStates.next()

    return await message.reply('Введите цену', reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower != 'отмена', state=AddOrderStates.price)
async def add_order_process_price(message: Message, state: FSMContext) -> Message:
    await state.update_data(price=message.text)

    async with state.proxy() as data:
        try:
            new_order = AddOrderRequest(**data)
            repo = OrderRepository()
            await OrderService(repo).add_order(new_order)
        except Exception as e:
            logger.bind(message=message).error(str(e))
            return await message.reply('Не удалось добавить ордер', reply_markup=action_order_buttons)
        finally:
            await state.finish()

    return await message.reply('Ордер успешно добавлен', reply_markup=action_order_buttons)


# ================ Обработчики для удаления ордеров ===============================
@dp.message_handler(Text(equals='Удалить ордер', ignore_case=True))
async def delete_order(message: Message) -> Message:
    await DeleteOrderStates.pk.set()

    return await message.reply('Введите ID ордера для удаления', reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower != 'отмена', state=DeleteOrderStates.pk)
async def delete_order_process_pk(message: Message, state: FSMContext) -> Message:

    try:
        order = DeleteOrderRequest(pk=message.text)
        repo = OrderRepository()
        await OrderService(repo).delete_order(order)
    except Exception as e:
        logger.bind(message=message).error(str(e))
        return await message.reply("Не удалось удалить ордер", reply_markup=action_order_buttons)
    finally:
        await state.finish()

    return await message.reply('Ордер успешно удален', reply_markup=action_order_buttons)
