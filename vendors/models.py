from django.db import models


class Address(models.Model):
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    additional = models.CharField(max_length=255, blank=True, default='')


class Vendor(models.Model):
    business_code = models.CharField(max_length=100, primary_key=True)

    address = models.ForeignKey(Address, null=True,
                                on_delete=models.SET_NULL,
                                related_name='vendors')
    name = models.CharField(max_length=100, db_index=True)
    owner = models.CharField(max_length=100)
