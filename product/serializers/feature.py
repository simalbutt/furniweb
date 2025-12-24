from rest_framework import serializers
from ..models.feature import ProductFeature

class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['id', 'product', 'feature']
