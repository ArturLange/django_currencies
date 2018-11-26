from django.db import models

class Currency(models.Model):
    # According to ISO 4217 this will always be three letters
    code = models.CharField(max_length=3)

class ExchangeRate(models.Model):
    rate = models.DecimalField(max_digits=19, decimal_places=10) # Reasonable assumptions
    date = models.DateField()

    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE
    )
