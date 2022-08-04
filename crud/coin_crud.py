from .base_crud import BaseCRUD
from models.coin import coin


class CoinCRUD(BaseCRUD):
    Table = coin

