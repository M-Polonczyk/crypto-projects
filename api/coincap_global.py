import constants as const
# import json


global_url = const.BASE_URL + '/v1/global-metrics/quotes/latest?convert=' + const.CURRENCY

btc_dominance = const.data['btc_dominance']
eth_dominance = const.data['eth_dominance']
total_cap = const.data['quote'][const.CURRENCY]['total_market_cap']
total_volume_24h = const.data['quote'][const.CURRENCY]['total_volume_24h']
total_cap_string = const.SYMBOL + '{:,}'.format(round(total_cap, 2))
total_volume_24h_string = const.SYMBOL + '{:,}'.format(round(total_volume_24h, 2))


print('Total market cap:',total_cap_string)
print('Total volume:',total_volume_24h_string,'\n')
print(f'BTC takes {round(btc_dominance, 2)}% of the global market cap')
print(f'ETH takes {round(eth_dominance, 2)}% of the global market cap\n')
# print(json.dumps(result, sort_keys=True, indent=4))

# constants.py file
'''
import requests


currency, symbol = 'USD', '$'
api_key = os.getenv('COINMARKETCAP_API_KEY', '')
headers = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'

'''