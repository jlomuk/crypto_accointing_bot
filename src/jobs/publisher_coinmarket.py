import asyncio

from async_cron.job import CronJob
from async_cron.schedule import Scheduler

from utils.rabbitmq.base_rabbit import BaseConnection
from vendors.coinmarket import requestor
from adapters.coin import CoinRepository
from settings import DSN_RABBITMQ
from schemas.coin_schemas import CoinUpdate


class Publisher(BaseConnection):
    QUEUE = 'COINMARKET'

    @classmethod
    def execute(cls, data: dict, shortcuts: list):
        instance = cls(DSN_RABBITMQ)
        instance.connect()
        for shortcut in shortcuts:
            coin = instance.parse_for_message(data, shortcut)
            instance.publish(body=coin.json())
        instance.disconnect()

    @staticmethod
    def parse_for_message(data, shortcut) -> CoinUpdate:
        raw_coins = data['data']
        name = raw_coins[shortcut][0]['name']
        info = raw_coins[shortcut][0]['quote']['USD']
        coin_update = CoinUpdate(shortcut=shortcut,
                                 name=name,
                                 capitalization=int(info['market_cap']),
                                 market_price=info['price'])

        return coin_update


async def main():
    db_shortcuts = await CoinRepository().distinct_shortcuts(mapped=False)
    shortcuts: list = [value for value, in db_shortcuts]
    result = requestor.CoinMarketCupRequestor().get_cryptocurrency(symbols=','.join(shortcuts))
    Publisher.execute(result, shortcuts)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    msh = Scheduler(locale="ru_RU")
    job = CronJob(name='main').every(20).minute.go(main)
    msh.add_job(job)
    try:
        loop.run_until_complete(msh.start())
    except KeyboardInterrupt:
        print('exit')
