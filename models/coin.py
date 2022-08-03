import sqlalchemy as sa
from . import metadata_obj


coin = sa.Table(
    'coin', metadata_obj,
    sa.Column('id', sa.INTEGER, primary_key=True),
    sa.Column('shortcut', sa.String(10), nullable=False),
    sa.Column('name', sa.String(200), nullable=False),
    sa.Column('capitalization', sa.INTEGER, nullable=True),
    sa.Column('market price', sa.DECIMAL(precision=6, scale=4), nullable=True),
    sa.Column('created_date', sa.DateTime(timezone=True), default=sa.func.now()),
    sa.Column('updated_date', sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now()),
)
