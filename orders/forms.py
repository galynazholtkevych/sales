from django import forms
from common.models import Address
from customers.models import Customer
from products.models import Product


class OrderForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    address = forms.ModelChoiceField(queryset=Address.objects.all())
    product = forms.ModelMultipleChoiceField(queryset=Product.objects.all())
