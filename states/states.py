from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteCoinStates(StatesGroup):
    shortcut = State()
    delete_coin = State()


class CreateCoinStates(StatesGroup):
    name = State()
    shortcut = State()


class GetOrderStates(StatesGroup):
    shortcut = State()


class AddOrderStates(StatesGroup):
    action = State()
    shortcut = State()
    count = State()
    price = State()


class DeleteOrderStates(StatesGroup):
    pk = State()
