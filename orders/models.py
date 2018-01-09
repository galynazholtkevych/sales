from django.db import models
from common.models import Address
from customers.models import Customer
from products.models import Product


class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='orders')
    product = models.ManyToManyField(Product, related_name='orders')
    custom_address = models.ForeignKey(Address, on_delete=models.SET_NULL,
                                       null=True)
