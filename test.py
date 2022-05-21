import json
import requests

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

data=cg.get_price(ids='bitcoin', vs_currencies='usd')

print(data)

list=cg.get_coins_markets(vs_currency='usd')
print(json.dumps((list), indent=4))