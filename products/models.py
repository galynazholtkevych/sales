from django.db import models
from vendors.models import Vendor


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    price = models.IntegerField()
    stock_available = models.IntegerField(default=0)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,
                               related_name='products')

    def __str__(self):
        return self.name
