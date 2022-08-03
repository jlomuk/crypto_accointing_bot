from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Криптомонеты')
        ],
        [
            KeyboardButton('Информация по криптомонете')
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

action_crypto_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Список криптомонет')
        ],
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
