from django.db import models

class ExchangeRate(models.Model):
    currency = models.DecimalField(max_digits=4,decimal_places=2)
    data_created = models.DateTimeField(auto_now_add=True)
    date_upload =models.DateTimeField(auto_now=True)

def _str_(self):
    return self.currency