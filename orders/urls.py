from django.conf.urls import url

from .views import OrderCreateView, OrderSuccessView

app_name = 'orders'

urlpatterns = [
    url(r'^$', OrderCreateView.as_view(), name='create_order'),
    url(r'^success$', OrderSuccessView.as_view(), name='success_order')
]