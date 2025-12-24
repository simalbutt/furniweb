from django.urls import path

from ..views.variant import VariantDetailAPIView, VariantListCreateAPIView

urlpatterns = [
    path("", VariantListCreateAPIView.as_view(), name="variant-list-create"),
    path("<int:pk>/", VariantDetailAPIView.as_view(), name="variant-detail"),
]
