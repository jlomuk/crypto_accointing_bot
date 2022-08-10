from adapters.order import OrderRepository
from schemas.order_schemas import OrderRequest, Order


class OrderService:

    def __init__(self, repository):
        self.order = repository

    async def list_orders(self, coin: OrderRequest) -> list[Order]:
        db_result: dict = await self.order.list(shortcut=coin.shortcut)
        return [Order(**row) for row in db_result]
