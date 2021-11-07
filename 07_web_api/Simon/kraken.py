import requests

response = requests.get('https://api.kraken.com/0/public/Trades?pair=XBTUSD')



print(response.json())

