from django.urls import path
from ..views.image import ProductImageListCreateAPIView, ProductImageDetailAPIView
urlpatterns = [
    path('', ProductImageListCreateAPIView.as_view(), name='image-list-create'),
    path('<int:pk>/', ProductImageDetailAPIView.as_view(), name='image-detail'),
]
