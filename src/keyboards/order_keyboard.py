from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


action_order_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Список всех ордеров по монете')
        ],
        [
            KeyboardButton('Добавить ордер'),
        ],
        [
            KeyboardButton('Отмена')
        ]
    ],
    resize_keyboard=True
)

type_action_order = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Покупка'),
            KeyboardButton('Продажа'),
        ],
        [
            KeyboardButton('Отмена')
        ]
    ],
    resize_keyboard=True
)

delete_order_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Удалить ордер'),
        ],
        [
            KeyboardButton('Отмена')
        ]
    ],
    resize_keyboard=True
)
