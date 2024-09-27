import os
import csv
import json
import requests
import sys
import time
from datetime import datetime

currency, currency_symbol = 'USD', '$'
api_key = os.getenv('COINMARKETCAP_API_KEY', '')
headers = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'

hit_symbols = []

while True:
    with open('alerts.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if '\ufeff' in row[0]:
                row[0] = row[0][1:].upper()
            else:
                row[0] = row[0].upper()
            quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + currency + '&symbol=' + row[0]
            request = requests.get(quote_url,headers=headers)
            result = request.json()
            if float(result['data'][row[0]]['quote'][currency]['price']) >= float(row[1]) and not row[0] in hit_symbols:
                os.system('say ' + str(row[0]) + ' hit ' + str(row[1]))
                sys.stdout.flush()
                current_time = datetime.now().strftime('%H:%M')
                print(row[0] + ' hit ' + str(round(result['data'][row[0]]['quote'][currency]['price'], 2)) + ' at ' + current_time)
    print('...')
    time.sleep(300)