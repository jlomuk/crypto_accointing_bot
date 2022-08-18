from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Криптомонеты')
        ],
        [
            KeyboardButton('Покупки и продажи криптомонет')
        ],
    ],
    resize_keyboard=True
)
confirm_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Подтвердить'),
            KeyboardButton('Отмена')
        ],
    ],
    resize_keyboard=True
)
cancel_button = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Отмена')
        ],
    ],
    resize_keyboard=True
)
