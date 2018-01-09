from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .forms import OrderForm



class OrderCreateView(FormView):
    form_class = OrderForm
    fields = ('customer', 'custom_address', 'product')
    template_name = 'orders/templates/form_order.html'
    success_url = reverse_lazy('orders:success_order')
 

class OrderSuccessView(TemplateView):
    template_name = 'orders/templates/success_order.html'