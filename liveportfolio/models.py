from django.db import models

class Portfolio(models.Model):
    stock_symbol = models.CharField(max_length=20)  # 20+ chars for long BSE/NSE codes
    quantity = models.PositiveIntegerField()
    buy_price = models.FloatField()
    buy_date = models.DateField()  # Let user/admin set purchase date

    def __str__(self):
        return f"{self.stock_symbol} ({self.quantity})"
