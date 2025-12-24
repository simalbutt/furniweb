from django.urls import path
from ..views.variant import VariantListCreateAPIView, VariantDetailAPIView

urlpatterns = [
    path('', VariantListCreateAPIView.as_view(), name='variant-list-create'),
    path('<int:pk>/', VariantDetailAPIView.as_view(), name='variant-detail'),
]
