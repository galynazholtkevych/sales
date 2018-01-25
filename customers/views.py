from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateCustomerForm


class CreateCustomer(CreateView):
    form_class = CreateCustomerForm
    template_name = 'customers/templates/create_customer.html'
    success_url = reverse_lazy('orders:create_order')
