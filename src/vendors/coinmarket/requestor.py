import requests
from requests.adapters import Retry, HTTPAdapter
from settings import API_TOKEN_COINMARKETCAP
from loguru import logger


class CoinMarketCupRequestor:

    def __init__(self):
        self.base_url = 'https://pro-api.coinmarketcap.com'
        self.api_token = API_TOKEN_COINMARKETCAP
        self.headers = {
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
            'X-CMC_PRO_API_KEY': self.api_token
        }

    def call(self, endpoint, headers) -> dict:
        session = requests.Session()
        session.headers.update(headers)

        retries = Retry(total=3,
                        backoff_factor=.3,
                        status_forcelist=[500, 502, 503, 504])

        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))
        url = f'{self.base_url}/{endpoint}'

        try:
            response = session.get(url, timeout=5)

            if response.status_code == 200:
                logger.info('Данные успешно получены с ' + url)
                return response.json()

            logger.bind(
                body=response.text,
                status_code=response.status_code,
                url=url
            ).debug("Запрос прошел неуспешно, данные не получены")
            return {}

        except Exception as e:
            logger.bind(traceback=str(e)).error('Критическая ошибка при запросе ' + url)
            return {}

    def get_cryptocurrency(self, symbols: str = None) -> dict:
        endpoint = 'v2/cryptocurrency/quotes/latest'
        if symbols:
            endpoint += f'?symbol={symbols}'
        return self.call(endpoint, self.headers)


