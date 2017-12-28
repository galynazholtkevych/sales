from django.conf.urls import url

from .views import ProductsList

app_name = 'products'

urlpatterns = [
    url(r'^$', ProductsList.as_view(), name='product_list')
]