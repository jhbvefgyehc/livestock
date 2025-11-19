from django.shortcuts import render
from django.http import JsonResponse
from .models import Portfolio
import requests

# Finnhub API key
FINNHUB_API_KEY = 'd4f2depr01qkcvvg8js0d4f2depr01qkcvvg8jsg'

def home(request):
    """Simple home view"""
    return render(request, 'home.html')

def stock_price_view(request):
    """Fetch stock price from Finnhub API"""
    symbol = request.GET.get('symbol', 'TATASTEEL.BSE')
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}'
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if 'c' in data and data['c']:
            price = data['c']
            return JsonResponse({
                'symbol': symbol,
                'price': price,
                'raw': data
            })
        else:
            return JsonResponse({
                'error': 'Unable to fetch price',
                'raw': data
            })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_live_price(symbol):
    """Helper function for dashboard view"""
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}'
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if 'c' in data and data['c']:
            return str(data['c'])
        else:
            return 'N/A'
    except Exception as e:
        print(f"Finnhub Error for {symbol}: {e}")
        return 'N/A'

def portfolio_dashboard(request):
    """Display portfolio with live prices from Finnhub API"""
    portfolios = Portfolio.objects.all()
    print(f"\n=== DEBUG: Found {portfolios.count()} stocks ===")

    portfolio_data = []
    for portfolio in portfolios:
        live_price = get_live_price(portfolio.stock_symbol)
        portfolio_data.append({
            'symbol': portfolio.stock_symbol,
            'quantity': portfolio.quantity,
            'buy_price': portfolio.buy_price,
            'buy_date': portfolio.buy_date,
            'live_price': live_price
        })
    print(f"Sending {len(portfolio_data)} stocks to template")

    return render(request, 'portfolio_dashboard.html', {'dashboard': portfolio_data})
