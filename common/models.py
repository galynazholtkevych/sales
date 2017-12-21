from django.db import models


class Address(models.Model):
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    additional = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return f"{self.city}, {self.street_name}, {self.street_number}"

