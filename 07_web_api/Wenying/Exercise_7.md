### The first part is about the [Binance API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md):

> What is the root URL?

The root URL is: `https://api.binance.com`
Three backup root URLs:
```
    https://api1.binance.com
    https://api2.binance.com
    https://api3.binance.com
```

> What is the endpoint to retrieve klines (open-high-low-close data) for a specific cryptocurrency?

The endpoint is: `/api/v3/klines`.

> Specify a request string to retrieve 75 observations of klines data for BTCUSDT since 2021-06-15.

The request string is: `https://api.binance.com/api/v3/klines?symbol=BTCUSDT&startTime=20210615&interval=1h&limit=75`

> Write a function (in Python, R or Julia) that retrieves 75 observations of klines data for a generic currency pair since a generic date. The function should take the currency pair and start date as input parameters.

```python
import requests

klines_url = 'https://api.binance.com/api/v3/klines'

def retrive_observation(currencyPair, startDate):
    params = {
        'symbol': currencyPair,
        'startTime': startDate,
        'interval': '1h',
        'limit': 75
    }

    response = requests.get(klines_url , params = params)
    return response

def main():
    print(retrive_observation('BTCUSDT', '20210615').json())

if __name__ == '__main__':
    main()
```

### The rest is about the [FRED API](https://fred.stlouisfed.org/docs/api/fred/):

> Read how authentication with API keys works. Create an account and obtain your own key.

Got a 32 Byte api key: `a1161b85aa55ac517e238899xxxxxxxx`

The last 8 digits are hided for security reasons.

> What is the root URL?

The root URL is: `https://api.stlouisfed.org`

> What is the endpoint to retrieve time series observations?

The endpoint is: `/fred/series/observations`

> Construct a query string to retrieve the series of the monthly unemployment rate (seasonally adjusted) since 2020-01. Use the fake API key abc123 in the query string.

The query string is: `https://api.stlouisfed.org/fred/series/observations?series_id=unrate&observation_start=2020-01-01&api_key=abc123&file_type=json`