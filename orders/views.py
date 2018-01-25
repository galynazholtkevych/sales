from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import OrderForm


class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = 'orders/templates/form_order.html'
    success_url = reverse_lazy('orders:success_order')


class OrderSuccessView(TemplateView):
    template_name = 'orders/templates/success_order.html'
