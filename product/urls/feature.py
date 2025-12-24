
from ..views.feature import ProductFeatureListCreateAPIView, ProductFeatureDetailAPIView
from django.urls import path
urlpatterns = [
    path('', ProductFeatureListCreateAPIView.as_view(), name='feature-list-create'),
    path('<int:pk>/', ProductFeatureDetailAPIView.as_view(), name='feature-detail'),
]
