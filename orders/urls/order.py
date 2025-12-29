from django.urls import path

from orders.views.order import PlaceOrderAPIView

urlpatterns = [
    path("place/", PlaceOrderAPIView.as_view()),
]
