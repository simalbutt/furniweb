from django.urls import path

from cart.views.cart import CartAPIView
from cart.views.item import CartItemDeleteAPIView

urlpatterns = [
    path("", CartAPIView.as_view()),
    path("item/<int:item_id>/", CartItemDeleteAPIView.as_view()),
]
