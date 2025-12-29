from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from utils.response import APIResponse

from cart.services import get_user_cart
from orders.models.order import Order
from orders.serializers.order import OrderSerializer


class PlaceOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        cart = get_user_cart(request.user)
        items = cart.items.select_for_update()


        if not items.exists():
            return APIResponse.error("Cart is empty")
        
        if not request.data.get("shipping_address"):
            return APIResponse.error("Shipping address is required")
        


        order = Order.objects.create(
            user=request.user,
            shipping_address_id=request.data.get("shipping_address"),
            billing_address_id=request.data.get("billing_address"),
            status="pending",
        )

        total = 0

        for item in items:
            item.cart = None
            item.order = order
            item.save()
            total += item.quantity * item.price

        order.total_amount = total
        order.save()

        serializer = OrderSerializer(order)
        return APIResponse.success(serializer.data, message="Order placed successfully")
