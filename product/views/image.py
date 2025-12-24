from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from rest_framework import status
from ..models import ProductImage
from ..serializers.image import ProductImageSerializer
from utils.response import APIResponse


class ProductImageListCreateAPIView(APIView):
    """
    List all product images or create a new one.
    """

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        images = ProductImage.objects.all()
        serializer = ProductImageSerializer(images, many=True)
        return APIResponse.success(data=serializer.data)

    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(data=serializer.data, status_code=status.HTTP_201_CREATED)
        return APIResponse.error(message="Validation error", errors=serializer.errors)

class ProductImageDetailAPIView(APIView):
    """
    Retrieve, update, or delete a product image.
    """

    parser_classes = [MultiPartParser, FormParser] 

    def get(self, request, pk):
        image = get_object_or_404(ProductImage, pk=pk)
        serializer = ProductImageSerializer(image)
        return APIResponse.success(
            data=serializer.data,
            message="Product image fetched successfully"
        )

    def put(self, request, pk):
        image = get_object_or_404(ProductImage, pk=pk)
        serializer = ProductImageSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data,
                message="Product image updated successfully"
            )
        return APIResponse.error(
            message="Validation error",
            errors=serializer.errors
        )

    def delete(self, request, pk):
        image = get_object_or_404(ProductImage, pk=pk)
        image.delete()
        return APIResponse.success(
            message="Product image deleted successfully"
        )
