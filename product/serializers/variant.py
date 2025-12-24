from rest_framework import serializers
from ..models.variant import ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'product', 'sku', 'title', 'price', 'compare_at', 'stock']
