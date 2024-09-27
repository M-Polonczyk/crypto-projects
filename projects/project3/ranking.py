import json
import requests
import time
from prettytable import PrettyTable
from colorama import Fore, Back, Style
from datetime import datetime

currency, currency_symbol = 'USD', '$'
api_key = os.getenv('COINMARKETCAP_API_KEY', '')
headers = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'
sort = ''

while True:
    print('1 - Top 100 sorted by marketcap\n2 - Top 100 sorted by 24 hour percent change\n3 - Top 100 sorted by hour volume\n0 - exit\n')
    choice = int(input('Your choice: '))
    if choice == 1:
        sort = 'market_cap'
        break
    elif choice == 2:
        sort = 'percent_change_24h'
        break
    elif choice == 3:
        sort = 'volume_24h'
        break
    elif choice == 0:
        exit(0)
    else:
        print('Bad choice. Try again.')
        time.sleep(1)
global_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + currency + '&sort=' + sort
request = requests.get(global_url,headers=headers)
result = request.json()
# print(json.dumps(result, sort_keys=True, indent=4))
table = PrettyTable(['Asset', 'Price', 'Market Cap', 'Volume', '1H', '24H', '7d'])
for crypto in result['data']:
    name = crypto['name']
    quote = crypto['quote'][currency]
    percent_change_1h = round(quote['percent_change_1h'], 2)
    percent_change_24h = round(quote['percent_change_24h'], 2)
    percent_change_7d = round(quote['percent_change_7d'], 2)
    if quote['market_cap'] == 0:
        continue
    if percent_change_1h > 0:
        percent_change_1h = Back.GREEN + str(percent_change_1h) + '%' + Style.RESET_ALL
    elif percent_change_1h < 0:
        percent_change_1h = Back.RED + str(percent_change_1h) + '%' + Style.RESET_ALL
    if percent_change_24h > 0:
        percent_change_24h = Back.GREEN + str(percent_change_24h) + '%' + Style.RESET_ALL
    elif percent_change_24h < 0:
        percent_change_24h = Back.RED + str(percent_change_24h) + '%' + Style.RESET_ALL
    if percent_change_7d > 0:
        percent_change_7d = Back.GREEN + str(percent_change_7d) + '%' + Style.RESET_ALL
    elif percent_change_7d < 0:
        percent_change_7d = Back.RED + str(percent_change_7d) + '%' + Style.RESET_ALL

    table.add_row([name + '(' + crypto['symbol'] + ')', quote['price'], round(quote['market_cap'], 2), quote['volume_24h'], percent_change_1h, percent_change_24h, percent_change_7d])
print(table)