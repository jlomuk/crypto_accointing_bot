from loguru import logger


from utils.rabbitmq.base_rabbit import BaseConnection
from adapters.coin import CoinRepository
from settings import DSN_RABBITMQ
from schemas.coin_schemas import CoinUpdate
from utils.helpers import sync


class Consumer(BaseConnection):
    QUEUE = 'COINMARKET'

    def __init__(self, dsn):
        super().__init__(dsn)
        self.coin_repo = CoinRepository()

    async def update_coin_db(self, coin: CoinUpdate) -> bool:
        try:
            await self.coin_repo.update(shortcut=coin.shortcut, update_data=coin.dict(exclude={'shortcut'}))
            return True
        except Exception as e:
            logger.error(e)
            return False


    @sync
    async def callback(self, ch, method, properties, body):
        coin = CoinUpdate.parse_raw(body)
        is_updated = await self.update_coin_db(coin)
        if is_updated:
            ch.basic_ack(method.delivery_tag)

    @classmethod
    def execute(cls, dsn):
        channel = cls(dsn)
        channel.connect()
        channel.consume(callback=channel.callback)
        channel.start_consume()


def main():
    Consumer.execute(DSN_RABBITMQ)


if __name__ == '__main__':
    main()
