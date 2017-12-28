from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    additional = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return f"{self.city}, {self.street_name}, {self.street_number}"

