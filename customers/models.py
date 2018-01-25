from django.db import models

from common.models import Address
from customauth.models import CustomUser


class Customer(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),
                      ('O', 'Other'))
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                related_name='customer')
    address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                related_name='customers')
    phone_number = models.CharField(max_length=15,
                                    verbose_name='Phone Number')
    gender = models.CharField(max_length=2, verbose_name='Gender',
                              choices=GENDER_CHOICES)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
