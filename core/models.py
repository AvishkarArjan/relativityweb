from django.db import models

class Framework(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="Framework description")

    def __str__(self):
        return f"{self.name}"

class DataSource(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="Data Source description")

    def __str__(self):
        return f"{self.name}"
    
class Portfolio(models.Model):
    name = models.CharField(max_length=200, default="Name")
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, related_name="framework") 
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name="data_source") # YFinance, Screener, Voyager
    start_date = models.DateField()
    init_amt = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class Holding(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='holdings')
    ticker = models.CharField(max_length=20)  # e.g., "AAPL", "GOOG"
    buy_price = models.DecimalField(max_digits=20, decimal_places=4)
    quantity = models.DecimalField(max_digits=20, decimal_places=4)  # optional: quantity of shares bought
    buy_date = models.DateField(null=True, blank=True)  # optional: when the holding was acquired

    def __str__(self):
        return f"{self.ticker} @ {self.buy_price}"


