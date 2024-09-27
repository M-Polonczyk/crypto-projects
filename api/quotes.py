import constants as const

symbol = input('Enter cryptocurrency symbol: ')
global_url = const.BASE_URL + '/v1/cryptocurrency/quotes/latest?convert=' + const.CURRENCY + '&symbol=' + symbol
data = const.data


print(data[symbol.upper()]['name'])
print('The price is:',data[symbol.upper()]['quote'][const.CURRENCY]['price'])
print('\ntags')
for i in data[symbol.upper()]['tags']:
    print(i)
# print(data[symbol.upper()]['name'])
