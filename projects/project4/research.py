import math
import locale
import json
import requests
from prettytable import PrettyTable


currency, currency_symbol = 'USD', '$'
api_key = os.getenv('COINMARKETCAP_API_KEY', '')
headers = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'
global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + currency
listing_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + currency
request = requests.get(global_url, headers=headers)
result = request.json()
total_cap = result['data']['quote'][currency]['total_market_cap']
total_cap_string = currency_symbol + '{:,}'.format(round(total_cap, 2))
request = requests.get(listing_url, headers=headers)
result = request.json()
table = PrettyTable(['Name', 'Ticker', '% of global cap', 'Price', '10.9T (gold)', '35.2T (Narrow Money)', '89.5T (stock market)'])


for crypto in result['data']:
    market_cap = crypto['quote'][currency]['market_cap']
    percentage_of_global_cap = float(market_cap) / float(total_cap)
    if crypto['total_supply'] == 0:
        p_supply = percentage_of_global_cap / 100000000
    else:
        p_supply = percentage_of_global_cap / crypto['total_supply']
    gold = 10900000000000 * p_supply
    narrow =  35200000000000 * p_supply
    stock = 89500000000000 * p_supply
    table.add_row([crypto['name'], crypto['symbol'], currency_symbol + str(round(crypto['quote'][currency]['market_cap'])), str(round(percentage_of_global_cap * 100, 2)) + '%',round(gold, 2), round(narrow, 2), round(stock, 2)])
print(table)