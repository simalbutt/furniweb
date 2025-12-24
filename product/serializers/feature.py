from rest_framework import serializers

from ..models.feature import ProductFeature
from ..models.product import Product


class ProductFeatureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    feature = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        """
        Customize the output structure for a ProductFeature instance.
        """
        return {
            "id": instance.id,
            "feature": instance.feature,
            "product": {
                "id": instance.product.id,
                "name": instance.product.title,
                "slug": instance.product.slug,
            },
        }

    def create(self, validated_data):
        return ProductFeature.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product = validated_data.get("product", instance.product)
        instance.feature = validated_data.get("feature", instance.feature)
        instance.save()
        return instance
