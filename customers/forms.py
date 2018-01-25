from django.forms import ModelForm

from .models import Customer


class CreateCustomerForm(ModelForm):

    class Meta:
        model = Customer
        exclude = ('user', )
