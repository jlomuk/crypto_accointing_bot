import enum

import sqlalchemy as sa
from . import metadata_obj


class Action(enum.Enum):
    buy = 1
    sell = 2

    @classmethod
    def get_action(cls, value: str):
        match value:
            case 'продажа':
                return cls.sell
            case 'покупка':
                return cls.buy
            case _:
                raise ValueError


order = sa.Table(
    'order', metadata_obj,
    sa.Column('id', sa.INTEGER, primary_key=True),
    sa.Column('coin_id', sa.INTEGER, sa.ForeignKey('coin.id', ondelete='CASCADE'), nullable=False),
    sa.Column('count', sa.DECIMAL(precision=6, scale=4), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=6, scale=4), nullable=False),
    sa.Column('action', sa.Enum(Action), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), default=sa.func.now()),
    sa.Column('updated_date', sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now()),
)
