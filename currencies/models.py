from django.db import models

class Currency(models.Model):
    # According to ISO 4217 this will always be three letters
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code

class ExchangeRate(models.Model):
    rate = models.DecimalField(max_digits=19, decimal_places=10) # Reasonable assumptions
    date = models.DateField()

    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='exchange_rates'
    )

    def __str__(self):
        return f"{self.currency.code} rate at {self.date}"
