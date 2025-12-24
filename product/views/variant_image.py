from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView

from utils.response import APIResponse

from ..models import VariantImage
from ..serializers.image import VariantImageSerializer


class VariantImageListCreateAPIView(APIView):
    """
    List all variant images or create a new one.
    """

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        images = VariantImage.objects.all()
        serializer = VariantImageSerializer(images, many=True)
        return APIResponse.success(data=serializer.data)

    def post(self, request):
        serializer = VariantImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data, status_code=status.HTTP_201_CREATED
            )
        return APIResponse.error(message="Validation error", errors=serializer.errors)


class VariantImageDetailAPIView(APIView):
    """
    Retrieve, update, or delete a variant image.
    """

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, pk):
        image = get_object_or_404(VariantImage, pk=pk)
        serializer = VariantImageSerializer(image)
        return APIResponse.success(
            data=serializer.data, message="Variant image fetched successfully"
        )

    def put(self, request, pk):
        image = get_object_or_404(VariantImage, pk=pk)
        serializer = VariantImageSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                data=serializer.data, message="Variant image updated successfully"
            )
        return APIResponse.error(message="Validation error", errors=serializer.errors)

    def delete(self, request, pk):
        image = get_object_or_404(VariantImage, pk=pk)
        image.delete()
        return APIResponse.success(message="Variant image deleted successfully")
