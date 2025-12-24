from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from ..models import ProductFeature
from ..serializers.feature import ProductFeatureSerializer
from utils.response import APIResponse


class ProductFeatureListCreateAPIView(APIView):
    """List all product features or create a new one"""

    def get(self, request):
        features = ProductFeature.objects.all()
        serializer = ProductFeatureSerializer(features, many=True)
        return APIResponse.success(
            data=serializer.data,
            message="Product features fetched successfully"
        )

    def post(self, request):
        serializer = ProductFeatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data,
                message="Product feature created successfully",
                status_code=status.HTTP_201_CREATED
            )
        return APIResponse.error(
            message="Validation error",
            errors=serializer.errors
        )


class ProductFeatureDetailAPIView(APIView):
    """Retrieve, update, or delete a product feature"""

    def get(self, request, pk):
        feature = get_object_or_404(ProductFeature, pk=pk)
        serializer = ProductFeatureSerializer(feature)
        return APIResponse.success(data=serializer.data)

    def put(self, request, pk):
        feature = get_object_or_404(ProductFeature, pk=pk)
        serializer = ProductFeatureSerializer(feature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data,
                message="Product feature updated successfully"
            )
        return APIResponse.error(
            message="Validation error",
            errors=serializer.errors
        )

    def delete(self, request, pk):
        feature = get_object_or_404(ProductFeature, pk=pk)
        feature.delete()
        return APIResponse.success(message="Product feature deleted successfully")