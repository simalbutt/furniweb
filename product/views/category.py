from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from utils.response import APIResponse

from ..models import Category
from ..serializers.category import CategorySerializer
from ..serializers.product import ProductSerializer


class CategoryListCreateAPIView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return APIResponse.success(
            data=serializer.data, message="Categories fetched successfully"
        )

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data,
                message="Category created successfully",
                status_code=201,
            )

        return APIResponse.error(message="Validation error", errors=serializer.errors)


class CategoryDetailAPIView(APIView):

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(category)
        return APIResponse.success(
            message=f"{slug} fetched successfully", data=serializer.data
        )

    def put(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data, message="Category updated successfully"
            )

        return APIResponse.error(message="Validation error", errors=serializer.errors)

    def delete(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return APIResponse.success(message="Category deleted successfully")


class CategoryProductsAPIView(APIView):
    """
    Get all products of a single category using category slug
    """

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        products = category.products.all()

        serializer = ProductSerializer(products, many=True)
        return APIResponse.success(
            data=serializer.data,
            message=f"Products for category '{category.name}' fetched successfully",
        )
