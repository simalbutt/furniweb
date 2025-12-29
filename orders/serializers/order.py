from rest_framework import serializers
from orders.models.order import Order
from cart.serializers.item import ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "total_amount",
            "shipping_address",
            "billing_address",
            "items",
            "created_at",
        ]
