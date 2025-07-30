from django.db import models

class Portfolio(models.Model):
    framework = models.CharField(max_length=200)
    start_date = models.DateField()
    init_amt = models.DecimalField(max_digits=20, decimal_places=2)
    

    def __str__(self):
        return f"{self.framework} - {self.start_date}"


class Holding(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='holdings')
    ticker = models.CharField(max_length=20)  # e.g., "AAPL", "GOOG"
    buy_price = models.DecimalField(max_digits=20, decimal_places=4)
    quantity = models.DecimalField(max_digits=20, decimal_places=4)  # optional: quantity of shares bought
    buy_date = models.DateField(null=True, blank=True)  # optional: when the holding was acquired

    def __str__(self):
        return f"{self.ticker} @ {self.buy_price}"

class Framework(models.Model):
    pass

class Documents(models.Model):
    pass

