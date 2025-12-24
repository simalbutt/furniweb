from rest_framework import serializers

from ..models import Category, Product
from .category import CategorySerializer
from .feature import ProductFeatureSerializer
from .image import ProductImageSerializer
from .variant import ProductVariantSerializer


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    description = serializers.CharField()
    vendername = serializers.CharField(max_length=255)
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    free_shipping = serializers.BooleanField()
    available = serializers.BooleanField()
    sold = serializers.IntegerField()
    items_in_stock = serializers.IntegerField()

    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, write_only=True
    )

    categories_detail = CategorySerializer(
        source="categories", many=True, read_only=True
    )
    variants = ProductVariantSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    features = ProductFeatureSerializer(many=True, read_only=True)

    def create(self, validated_data):
        categories_data = validated_data.pop("categories", [])
        product = Product.objects.create(**validated_data)
        product.categories.set(categories_data)
        return product

    def update(self, instance, validated_data):
        categories_data = validated_data.pop("categories", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if categories_data is not None:
            instance.categories.set(categories_data)
        return instance

    def to_representation(self, instance):
        """
        Fully custom output structure similar to ModelSerializer behavior
        """
        return {
            "id": instance.id,
            "title": instance.title,
            "slug": instance.slug,
            "description": instance.description,
            "vendername": instance.vendername,
            "min_price": str(instance.min_price),
            "max_price": str(instance.max_price),
            "free_shipping": instance.free_shipping,
            "available": instance.available,
            "sold": instance.sold,
            "items_in_stock": instance.items_in_stock,
            "categories": [cat.id for cat in instance.categories.all()],
            "categories_detail": CategorySerializer(
                instance.categories.all(), many=True
            ).data,
            "variants": ProductVariantSerializer(
                instance.variants.all(), many=True
            ).data,
            "images": ProductImageSerializer(instance.images.all(), many=True).data,
            "features": ProductFeatureSerializer(
                instance.features.all(), many=True
            ).data,
        }
