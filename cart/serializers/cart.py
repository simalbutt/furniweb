from rest_framework import serializers

from cart.models.cart import Cart
from cart.serializers.item import ItemSerializer


class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "items", "total"]

    def get_total(self, obj):
        return sum(item.quantity * item.price for item in obj.items.all())
