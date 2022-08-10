from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default_keyboard import cancel_button
from services.order_service import OrderService
from schemas.order_schemas import OrderRequest
from keyboards.order_keyboard import action_order_buttons
from states.states import GetOrderStates
from adapters.order import OrderRepository
from loader import dp, jinja_env
from schemas.base import Contex


@dp.message_handler(Text(equals='Покупки и продажи криптомонет', ignore_case=True))
async def get_menu_orders(message: Message) -> Message:
    return await message.reply('Выберите действие', reply_markup=action_order_buttons)


@dp.message_handler(Text(equals='Список всех ордеров по монете', ignore_case=True))
async def get_order(message: Message) -> Message:
    order_repo = OrderRepository()
    shortcuts = await order_repo.distinct_shortcuts()
    await GetOrderStates.shortcut.set()

    template = jinja_env.get_template('orders/get_shortcuts.html')
    context = Contex(data=shortcuts, func=enumerate)
    return await message.reply(template.render(context.dict()), reply_markup=cancel_button)


@dp.message_handler(lambda message: message.text.lower != 'отмена', state=GetOrderStates.shortcut)
async def get_order_process_shortcut(message: Message, state: FSMContext) -> Message:
    order_req = OrderRequest(shortcut=message.text)
    order_repo = OrderRepository()
    orders = await OrderService(order_repo).list_orders(order_req)
    await state.finish()

    template = jinja_env.get_template('orders/get_orders.html')
    context = Contex(data=orders, func=enumerate)
    return await message.reply(template.render(context.dict()), reply_markup=cancel_button)
