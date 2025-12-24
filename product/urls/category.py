from django.urls import path

from ..views.category import (CategoryDetailAPIView, CategoryListCreateAPIView,
                              CategoryProductsAPIView)

urlpatterns = [
    path("", CategoryListCreateAPIView.as_view(), name="category-list-create"),
    path("<slug:slug>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path(
        "<slug:slug>/products/",
        CategoryProductsAPIView.as_view(),
        name="category-products",
    ),
]
