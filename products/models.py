from django.db import models
from django.utils.translation import ugettext_lazy as _
from vendors.models import Vendor


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    category_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    code = models.IntegerField()


class Product(models.Model):
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    price = models.IntegerField()
    stock_available = models.IntegerField(default=0)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,
                               related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')

    def __str__(self):
        return self.name
