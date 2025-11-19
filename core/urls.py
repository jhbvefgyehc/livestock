from django.contrib import admin
from django.urls import path
from liveportfolio.views import stock_price_view, portfolio_dashboard  # Import dashboard view
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django is running! Visit /price/?symbol=TATASTEEL.BSE or /dashboard for portfolio.")

urlpatterns = [
    path('', home),                 # Homepage
    path('admin/', admin.site.urls),
    path('price/', stock_price_view),
    path('dashboard/', portfolio_dashboard),  # Dashboard/table of holdings
]
