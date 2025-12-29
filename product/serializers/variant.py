from rest_framework import serializers
from ..models.product import Product
from ..models.variant import ProductVariant

class ProductVariantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    sku = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    compare_at = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False, allow_null=True
    )
    stock = serializers.ChoiceField(choices=[("in", "In Stock"), ("out", "Out of Stock")])

    def create(self, validated_data):
        return ProductVariant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product = validated_data.get("product", instance.product)
        instance.sku = validated_data.get("sku", instance.sku)
        instance.title = validated_data.get("title", instance.title)
        instance.price = validated_data.get("price", instance.price)
        instance.compare_at = validated_data.get("compare_at", instance.compare_at)
        instance.stock = validated_data.get("stock", instance.stock)
        instance.save()
        return instance
