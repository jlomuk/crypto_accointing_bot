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
