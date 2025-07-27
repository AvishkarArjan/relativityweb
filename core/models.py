from django.db import models

class Return(models.Model):
    framework = models.CharField(max_length=200)
    start_date = models.DateField()
    period = models.DecimalField(max_digits=5, decimal_places=2)
    arr = models.DecimalField(max_digits=5, decimal_places=2)
    crr = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.start_date} - {self.framework}"



