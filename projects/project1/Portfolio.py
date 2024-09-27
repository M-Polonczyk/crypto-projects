import os
import csv
import json
import requests
from prettytable import PrettyTable
from colorama import Fore, Back, Style


currency, currency_symbol = 'USD', '$'
api_key = os.getenv('COINMARKETCAP_API_KEY', '')
headers = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'
portfolio_value = 0.
table = PrettyTable(['Asset', 'Amount Owned', 'Value', 'Price', '1H', '24H', '7d'])
def snapshot(value):
    with open('my-portfolio.csv', 'a+') as myfile:
        csvwriter = csv.writer(myfile)
        csvwriter.writerow(str(value))

with open('C:/Users/mpolo/dev/Crypto/projects/project1/my-portfolio.csv','r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if '\ufeff' in row[0]:
            row[0] = row[0][1:].upper()
        else:
            row[0] = row[0].upper()

        amount = row[1]
        symbol = row[0]
        quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + currency + '&symbol=' + symbol
        request = requests.get(quote_url, headers=headers)
        result = request.json()
        cryptocurrency = result['data'][symbol]
        name = cryptocurrency['name']
        quote = cryptocurrency['quote'][currency]
        percent_change_1h = round(quote['percent_change_1h'], 2)
        percent_change_24h = round(quote['percent_change_24h'], 2)
        percent_change_7d = round(quote['percent_change_7d'], 2)
        price = quote['price']
        value = float(price) * float(amount)

        portfolio_value += value

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

        table.add_row([name + '(' + symbol + ')', amount, round(value, 2), round(price, 2), percent_change_1h, percent_change_24h, percent_change_7d])
        # print(json.dumps(result, sort_keys=True, indent=4))
print(table)
print('Total portfolio value:', currency_symbol + str(round(portfolio_value, 2)))
# snapshot(portfolio_value) do naprawy