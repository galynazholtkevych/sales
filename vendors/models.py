from django.db import models

from common.models import Address


class Vendor(models.Model):
    business_code = models.CharField(max_length=100, primary_key=True)

    address = models.ForeignKey(Address, null=True,
                                on_delete=models.SET_NULL,
                                related_name='vendors')
    name = models.CharField(max_length=100, db_index=True)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.name
