from django.db import models

class Return(models.Model):
    date = models.DateField()
    strategy_name = models.CharField(max_length=100)
    return_percent = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.strategy_name}: {self.return_percent}%"



