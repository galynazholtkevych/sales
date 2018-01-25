"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include, i18n
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.urls import path


from rest_framework.routers import DefaultRouter

from customauth import urls as auth_urls
from customers import urls as customers_urls
from products.views import ProductViewSet
from products import urls as products_urls
from orders import urls as orders_urls

from .views import IndexView


router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    url(r'^auth/', include(auth_urls, namespace='customauth')),
    url(r'^customers/', include(customers_urls, namespace='customers')),
    url(r'^orders/', include(orders_urls, namespace='orders')),
    url(r'^products/', include(products_urls, namespace='products')),
    url(r'^api-customauth/', include('rest_framework.urls',
                                     namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^$', IndexView.as_view()),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n.i18n_patterns(
    path(r'admin/', admin.site.urls),
)
