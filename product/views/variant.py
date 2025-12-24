from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import ProductVariant
from ..serializers.variant import ProductVariantSerializer
from utils.response import APIResponse


class VariantListCreateAPIView(APIView):
    """List all product variants or create a new variant"""

    def get(self, request):
        variants = ProductVariant.objects.all()
        serializer = ProductVariantSerializer(variants, many=True)
        return APIResponse.success(
            data=serializer.data,
            message="Product variants fetched successfully"
        )

    def post(self, request):
        serializer = ProductVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data,
                message="Product variant created successfully",
                status_code=status.HTTP_201_CREATED
            )
        return APIResponse.error(
            message="Validation error",
            errors=serializer.errors
        )


class VariantDetailAPIView(APIView):
    """Retrieve, update, or delete a product variant"""

    def get(self, request, pk):
        variant = get_object_or_404(ProductVariant, pk=pk)
        serializer = ProductVariantSerializer(variant)
        return APIResponse.success(
            data=serializer.data,
            message=" variant fetched  successfully"
            )

    def put(self, request, pk):
        variant = get_object_or_404(ProductVariant, pk=pk)
        serializer = ProductVariantSerializer(variant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data,
                message="Product variant updated successfully"
            )
        return APIResponse.error(
            message="Validation error",
            errors=serializer.errors
        )

    def delete(self, request, pk):
        variant = get_object_or_404(ProductVariant, pk=pk)
        variant.delete()
        return APIResponse.success(message="Product variant deleted successfully")
