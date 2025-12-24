from rest_framework import serializers
from ..models import Product, Category
from .variant import ProductVariantSerializer
from .image import ProductImageSerializer
from .feature import ProductFeatureSerializer
from .category import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories_detail = CategorySerializer(source='categories', many=True, read_only=True)

    # vendername = serializers.CharField()

    variants = ProductVariantSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    features = ProductFeatureSerializer(many=True, read_only=True)

    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'slug', 'description', 'categories', 'categories_detail',
            'vendername',
            'min_price', 'max_price', 'free_shipping', 'available',
            'sold', 'items_in_stock', 'variants', 'images', 'features'
        ]

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        product = Product.objects.create(**validated_data)
        product.categories.set(categories_data)
        return product

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if categories_data is not None:
            instance.categories.set(categories_data)
        return instance
