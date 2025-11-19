from django.shortcuts import render
from .models import Portfolio
from .api_utils import get_stock_price

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
