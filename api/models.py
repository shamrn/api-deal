from django.db import models


class DealData(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    spent_money = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    gems = models.CharField(max_length=200, blank=True, null=True)
