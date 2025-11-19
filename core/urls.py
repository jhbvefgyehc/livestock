from django.contrib import admin
from django.urls import path
from liveportfolio.views import home, stock_price_view, portfolio_dashboard

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('admin/', admin.site.urls),
    path('price/', stock_price_view, name='stock_price'),
    path('dashboard/', portfolio_dashboard, name='portfolio_dashboard'),
]
