from rest_framework import serializers
from order.models import Cart, CartItem, Order, OrderItem


class CartSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user"]
