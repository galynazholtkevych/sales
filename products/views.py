from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from django.views.generic import ListView


class ProductViewSet(ModelViewSet):

    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsList(ListView):
    template_name = 'products/templates/products.html'
    model = Product
