from rest_framework import serializers

from ..models import ProductImage, VariantImage
from ..models.product import Product
from ..models.variant import ProductVariant


class ProductImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    image = serializers.ImageField(required=True)

    def create(self, validated_data):
        return ProductImage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product = validated_data.get("product", instance.product)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance


class VariantImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    variant = serializers.PrimaryKeyRelatedField(queryset=ProductVariant.objects.all())
    image = serializers.ImageField(required=True)

    def create(self, validated_data):
        return VariantImage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.variant = validated_data.get("variant", instance.variant)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance
