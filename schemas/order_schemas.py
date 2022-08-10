import datetime
from decimal import Decimal
from models.order import Action
import pytz

from pydantic import BaseModel, validator


class Order(BaseModel):
    id: int
    shortcut: str
    count: Decimal
    price: Decimal
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
            return value.strftime('%Y.%m.%d %H:%M')
        raise ValueError


class OrderRequest(BaseModel):
    shortcut: str
