from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
import requests

def get_stock_price(symbol):
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': 'SZSRMMUNODCLYRUO'  # Replace with your active key!
    }
    data = requests.get(url, params=params).json()
    # Show the raw response for debugging
    if "Global Quote" in data and "05. price" in data["Global Quote"]:
        return data["Global Quote"]["05. price"]
    elif "Note" in data:
        return f"API rate limit hit: {data['Note']}"
    elif "Error Message" in data:
        return f"API error: {data['Error Message']}"
    else:
        return f"N/A (Raw: {str(data)})"

def stock_price_view(request):
    symbol = request.GET.get('symbol', 'TATASTEEL.BSE')
    price = get_stock_price(symbol)
    return HttpResponse(f"Current price for {symbol}: ₹{price}")

def portfolio_dashboard(request):
    holdings = Portfolio.objects.all()
    dashboard = []
    for h in holdings:
        price = get_stock_price(h.stock_symbol)
        dashboard.append({
            'symbol': h.stock_symbol,
            'quantity': h.quantity,
            'buy_price': h.buy_price,
            'buy_date': h.buy_date,
            'live_price': price,
        })
    return render(request, 'portfolio_dashboard.html', {'dashboard': dashboard})
