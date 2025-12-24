from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from utils.response import APIResponse
from ..models import Product
from ..serializers.product import ProductSerializer


class ProductListCreateAPIView(APIView):
    """
    List all products or create a new product
    """

    def get(self, request):
        products = Product.objects.prefetch_related("variants", "images", "features").all()
        serializer = ProductSerializer(products, many=True)
        return APIResponse.success(
            data=serializer.data,
            message="Products fetched successfully"
        )

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data,
                message="Product created successfully",
                status_code=201
            )
        return APIResponse.error(
            message="Validation error",
            errors=serializer.errors
        )


class ProductDetailAPIView(APIView):
    """
    Retrieve, update or delete a product by slug
    """

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(product)
        return APIResponse.success(
            data=serializer.data,
            message=f"{slug} fetched successfully"
        )

    def put(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data,
                message="Product updated successfully"
            )
        return APIResponse.error(
            message="Validation error",
            errors=serializer.errors
        )

    def delete(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        return APIResponse.success(
            message="Product deleted successfully"
        )
