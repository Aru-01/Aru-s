from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from order.models import Cart, CartItem, Order, OrderItem
from order.serializers import CartSerialzer


# Create your views here.
class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerialzer
