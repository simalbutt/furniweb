from rest_framework import serializers

from cart.models.item import Item


class ItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            "id",
            "product",
            "variant",
            "quantity",
            "price",
            "subtotal",
        ]

    def get_subtotal(self, obj):
        return obj.quantity * obj.price
