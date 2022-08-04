from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteCoinStates(StatesGroup):
    shortcut = State()
    delete_coin = State()


class CreateCoinStates(StatesGroup):
    name = State()
    shortcut = State()
