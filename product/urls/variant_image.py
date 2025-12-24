from django.urls import path

from ..views.variant_image import (VariantImageDetailAPIView,
                                   VariantImageListCreateAPIView)

urlpatterns = [
    path("", VariantImageListCreateAPIView.as_view(), name="variant-image-list-create"),
    path("<int:pk>/", VariantImageDetailAPIView.as_view(), name="variant-image-detail"),
]
