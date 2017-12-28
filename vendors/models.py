from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.models import Address


class Vendor(models.Model):
    class Meta:
        verbose_name = _('Vendor')
        verbose_name_plural = _('Vendors')

    business_code = models.CharField(max_length=100, primary_key=True)

    address = models.ForeignKey(Address, null=True,
                                on_delete=models.SET_NULL,
                                related_name='vendors')
    name = models.CharField(max_length=100, db_index=True)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.name
