from django.contrib import admin
from .models import Portfolio
from django.utils.html import format_html
from django.urls import reverse
import requests
import os


class PortfolioAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = [
        'stock_symbol_display', 
        'quantity', 
        'buy_price_display', 
        'buy_date', 
        'current_price_display', 
        'profit_loss_display'
    ]
    
    # Add filters in the sidebar
    list_filter = ['buy_date', 'stock_symbol']
    
    # Add search functionality
    search_fields = ['stock_symbol']
    
    # Fields to show when editing
    fields = ['stock_symbol', 'quantity', 'buy_price', 'buy_date']
    
    # Make the list sortable
    ordering = ['-buy_date']
    
    # Items per page
    list_per_page = 20
    
    # Add date hierarchy for easy filtering
    date_hierarchy = 'buy_date'
    
    # Custom display methods with colored styling
    def stock_symbol_display(self, obj):
        return format_html(
            '<strong style="color: #2563eb; font-size: 14px;">{}</strong>',
            obj.stock_symbol
        )
    stock_symbol_display.short_description = 'Stock Symbol'
    
    def buy_price_display(self, obj):
        return format_html(
            '<span style="color: #059669; font-weight: 600;">₹{}</span>',
            f'{obj.buy_price:,.2f}'  # Format BEFORE passing to format_html
        )
    buy_price_display.short_description = 'Buy Price'
    buy_price_display.admin_order_field = 'buy_price'
    
    def current_price_display(self, obj):
        try:
            api_key = os.environ.get('ALPHA_VANTAGE_KEY', '')
            if not api_key:
                return format_html('<span style="color: #9ca3af;">No API Key</span>')
            
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={obj.stock_symbol}&apikey={api_key}'
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if 'Global Quote' in data and '05. price' in data['Global Quote']:
                current_price = float(data['Global Quote']['05. price'])
                return format_html(
                    '<span style="color: #0891b2; font-weight: 600;">₹{}</span>',
                    f'{current_price:,.2f}'  # Format BEFORE passing to format_html
                )
            else:
                return format_html('<span style="color: #dc2626;">N/A</span>')
        except Exception as e:
            return format_html('<span style="color: #dc2626;">Error</span>')
    
    current_price_display.short_description = 'Current Price'
    
    def profit_loss_display(self, obj):
        try:
            api_key = os.environ.get('ALPHA_VANTAGE_KEY', '')
            if not api_key:
                return format_html('<span style="color: #9ca3af;">-</span>')
            
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={obj.stock_symbol}&apikey={api_key}'
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if 'Global Quote' in data and '05. price' in data['Global Quote']:
                current_price = float(data['Global Quote']['05. price'])
                total_invested = obj.buy_price * obj.quantity
                current_value = current_price * obj.quantity
                profit_loss = current_value - total_invested
                profit_loss_pct = (profit_loss / total_invested) * 100
                
                color = '#059669' if profit_loss >= 0 else '#dc2626'
                symbol = '+' if profit_loss >= 0 else ''
                arrow = '↑' if profit_loss >= 0 else '↓'
                
                # Format ALL numbers BEFORE passing to format_html
                return format_html(
                    '<span style="color: {}; font-weight: 700;">{} {}{} ({}{}%)</span>',
                    color, 
                    arrow, 
                    symbol, 
                    f'{profit_loss:,.2f}',  # Pre-formatted
                    symbol, 
                    f'{profit_loss_pct:.2f}'  # Pre-formatted
                )
            else:
                return format_html('<span style="color: #6b7280;">-</span>')
        except:
            return format_html('<span style="color: #6b7280;">-</span>')
    
    profit_loss_display.short_description = 'Profit/Loss'
    
    # Add custom dashboard button at the top of the page
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['dashboard_url'] = reverse('portfolio_dashboard')
        return super().changelist_view(request, extra_context=extra_context)


# Register the model with custom admin
admin.site.register(Portfolio, PortfolioAdmin)

# Customize admin site headers
admin.site.site_header = "📊 Stock Portfolio Management System"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Stock Portfolio Dashboard"
