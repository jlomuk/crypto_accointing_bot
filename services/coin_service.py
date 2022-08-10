from adapters.coin import CoinRepository
from schemas.coin_schemas import Coin, GetCoinRequest, DeleteCoinRequest, CreateCoinRequest


class CoinService:

    def __init__(self):
        self.coin_crud = CoinRepository()

    async def list_coin(self) -> list[Coin]:
        db_result = await self.coin_crud.list()
        return [Coin(**data) for data in db_result]

    async def create_coin(self, new_coin: CreateCoinRequest) -> Coin:
        db_result = await self.coin_crud.create(new_coin.dict())
        return Coin(**db_result)

    async def delete_coin(self, coin: DeleteCoinRequest) -> None:
        await self.coin_crud.delete(coin.shortcut)

    async def get_coin(self, coin: GetCoinRequest | DeleteCoinRequest) -> Coin:
        db_result = await self.coin_crud.retrieve(coin.shortcut)
        return Coin(**db_result)
