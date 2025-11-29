from django.db.models import Count
from rest_framework.generics import ListCreateAPIView
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


# Create your views here.
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count("products")).all()
    serializer_class = CategorySerializer
