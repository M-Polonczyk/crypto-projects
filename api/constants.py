import os
import requests


CURRENCY, SYMBOL = 'USD', '$'
API_KEY = os.getenv('COINMARKETCAP_API_KEY', '')
HEADERS = {'X-CMC_PRO_API_KEY': API_KEY}
BASE_URL = 'https://pro-api.coinmarketcap.com'

GLOBAL_URL = BASE_URL + '/v1/global-metrics/quotes/latest?convert=' + CURRENCY
data = requests.get(GLOBAL_URL, headers=HEADERS, timeout=5).json().get('data')
