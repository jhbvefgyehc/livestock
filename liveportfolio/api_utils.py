import requests

ALPHAVANTAGE_API_KEY = 'SZSRMMUNODCLYRUO'  # <-- your actual API key

def get_stock_price(symbol):
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': ALPHAVANTAGE_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    try:
        price = float(data['Global Quote']['05. price'])
        return price
    except (KeyError, ValueError):
        return None
