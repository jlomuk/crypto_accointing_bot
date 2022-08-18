from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

action_list_crypto_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Список криптомонет')
        ],
        [
            KeyboardButton('Добавить криптомонету'),
        ],
        [
            KeyboardButton('Отмена')
        ]
    ],
    resize_keyboard=True
)

action_crypto_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Добавить криптомонету'),
            KeyboardButton('Удалить криптомонету')
        ],
        [
            KeyboardButton('Отмена')
        ]
    ],
    resize_keyboard=True
)

