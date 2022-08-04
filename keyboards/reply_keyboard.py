from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Криптомонеты')
        ],
        [
            KeyboardButton('Добавить продажу/покупку криптомонеты')
        ],
        [
            KeyboardButton('Отмена')
        ]
    ],
    resize_keyboard=True
)

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

cancel_button = ReplyKeyboardMarkup(

    [
        [
            KeyboardButton('Отмена')
        ],
    ],
    resize_keyboard=True
)

confirm_crypto_buttons = ReplyKeyboardMarkup(

    [
        [
            KeyboardButton('Подтвердить'),
            KeyboardButton('Отмена')
        ],
    ],
    resize_keyboard=True
)
