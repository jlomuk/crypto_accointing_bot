from crud.coin_crud import CoinCRUD
from schemas.coin_schemas import Coin


class CoinService:

    def __init__(self):
        self.coin_crud = CoinCRUD()

    async def list_coin(self) -> list[Coin]:
        db_result = await self.coin_crud.list()
        return [Coin(**data) for data in db_result]

    async def create_coin(self, schema): ...

    async def delete_coin(self, schema): ...

    async def get_coin(self, schema): ...

