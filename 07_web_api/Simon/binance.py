# root URL is https://api.binance.com

# the endpoints for klines are /api/v3/klines

import requests

response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&startTime=1633853410&limit=75')

# 75 entries of BTCUSDT from 10.10.2021 in 1minute interval

print(response.json())



# for FRED root: https://api.stlouisfed.org/fred
# FRED endpoint: series

# query string for FRED: https://api.stlouisfed.org/fred/series?series_id=UNRATE&api_key=abc123&realtime_start=2020-01-01&file_type=json
