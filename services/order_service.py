from adapters.order import OrderRepository
from schemas.order_schemas import GetOrderRequest, Order, AddOrderRequest, DeleteOrderRequest


class OrderService:

    def __init__(self, repository: OrderRepository):
        self.order = repository

    async def list_orders(self, coin: GetOrderRequest) -> list[Order]:
        db_result: dict = await self.order.list(shortcut=coin.shortcut)
        return [Order(**row) for row in db_result]

    async def add_order(self, new_order: AddOrderRequest) -> None:
        await self.order.create(new_order.dict())

    async def delete_order(self, order: DeleteOrderRequest) -> None:
        await self.order.delete(pk=order.pk)