from django.urls import path

from authentication.views.address import AddressAPIView

urlpatterns = [
    path("", AddressAPIView.as_view()),
]
