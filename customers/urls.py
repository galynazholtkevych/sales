from django.conf.urls import url

from .views import CreateCustomer


app_name = 'customers'

urlpatterns = [
   url(r'^create-customer/$', CreateCustomer.as_view(),
       name='create_customer'),
]

