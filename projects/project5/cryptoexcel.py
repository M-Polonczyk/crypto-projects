import requests
import json
import xlsxwriter

currency, symbol = 'USD', '$'
api_key = os.getenv('COINMARKETCAP_API_KEY', '')
headers = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'


crypto_workbook = xlsxwriter.Workbook('cryptocurrencies.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Market Cap')
crypto_sheet.write('D1', 'Price')
crypto_sheet.write('E1', '24H Volume')
crypto_sheet.write('F1', '1H Change')
crypto_sheet.write('G1', '24H Change')
crypto_sheet.write('H1', '7D Change')

row = 1
for i in range(10):
    listing_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + currency + '&start=' + str(i*100 + 1)
    request = requests.get(listing_url, headers=headers)
    result = request.json()

    for crypto in result['data']:
        quote = crypto['quote'][currency]
        crypto_sheet.write(row, 0, crypto['name'])
        crypto_sheet.write(row, 1, crypto['symbol'])
        crypto_sheet.write(row, 2, symbol + str(quote['market_cap']))
        crypto_sheet.write(row, 3, symbol + str(quote['price']))
        crypto_sheet.write(row, 4, symbol + str(quote['volume_24h']))
        crypto_sheet.write(row, 5, symbol + str(quote['percent_change_1h']))
        crypto_sheet.write(row, 6, symbol + str(quote['percent_change_24h']))
        crypto_sheet.write(row, 7, symbol + str(quote['percent_change_7d']))
        row += 1
    
crypto_workbook.close()    