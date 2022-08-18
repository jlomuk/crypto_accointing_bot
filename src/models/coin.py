import sqlalchemy as sa
from . import metadata_obj


coin = sa.Table(
    'coin', metadata_obj,
    sa.Column('id', sa.INTEGER, primary_key=True),
    sa.Column('shortcut', sa.String(10), nullable=False, unique=True),
    sa.Column('name', sa.String(200), nullable=False, unique=True),
    sa.Column('capitalization', sa.BigInteger, nullable=True),
    sa.Column('market_price', sa.DECIMAL(precision=10, scale=4), nullable=True),
    sa.Column('created_date', sa.DateTime(timezone=True), default=sa.func.now()),
    sa.Column('updated_date', sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now()),
)
