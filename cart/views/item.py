from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from cart.models.item import Item
from utils.response import APIResponse


class CartItemDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        item = get_object_or_404(Item, id=item_id, cart__user=request.user)
        item.delete()
        return APIResponse.success(message="Item removed")
