from django.urls import path

from ..views.feature import (ProductFeatureDetailAPIView,
                             ProductFeatureListCreateAPIView)

urlpatterns = [
    path("", ProductFeatureListCreateAPIView.as_view(), name="feature-list-create"),
    path("<int:pk>/", ProductFeatureDetailAPIView.as_view(), name="feature-detail"),
]
