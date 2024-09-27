import constants as const
import json


global_url = const.BASE_URL + '/v1/cryptocurrency/listings/latest?convert=' + const.CURRENCY
request = const.requests.get(global_url, headers=const.HEADERS)
result = request.json()
data = result['data']


# print(json.dumps(result, sort_keys=True, indent=4))

for currency in data:
    print(currency['name'], currency['symbol'])
    print(currency['quote'][const.CURRENCY]['price'])

