import datetime
from decimal import Decimal
from typing import Optional

from models.order import Action
import pytz

from pydantic import BaseModel, validator, root_validator

from utils.helpers import normalize_fraction


class Order(BaseModel):
    id: int
    shortcut: str
    count: Decimal
    price: Decimal
    sum: Decimal
    action: Action
    created_date: datetime.datetime | None

    class Config:
        use_enum_values = True

    @validator('created_date')
    def date_to_str(cls, value: datetime.datetime):
        if not value:
            return 'нет даты'
        if isinstance(value, datetime.datetime):
            value = value.astimezone(tz=pytz.timezone('Europe/Moscow'))
            return value.strftime('%d.%m.%Y %H:%M')
        raise ValueError

    @root_validator
    def decimal_normalize(cls, values: dict) -> dict:
        for key, value in values.items():
            if isinstance(value, Decimal):
                values[key] = normalize_fraction(value)
        return values


class GetOrderRequest(BaseModel):
    shortcut: str

    @validator('shortcut')
    def upper_shortcut(cls, v: str):
        return v.upper()


class AddOrderRequest(GetOrderRequest):
    action: Action
    count: Decimal
    price: Decimal
    sum: Optional[Decimal]

    @root_validator
    def calculate(cls, values: dict) -> dict:
        values['sum'] = values['count'] * values['price']
        return values


class DeleteOrderRequest(BaseModel):
    pk: int
