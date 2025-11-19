from django.db import models

class Portfolio(models.Model):
    stock_symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    buy_price = models.FloatField()
    buy_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock_symbol} ({self.quantity})"
