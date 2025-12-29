from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from cart.services import get_user_cart
from orders.emails.order_confirmation import send_order_confirmation_email
from orders.models.order import Order
from orders.serializers.order import OrderSerializer
from utils.response import APIResponse


class PlaceOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        cart = get_user_cart(request.user)
        items = cart.items.select_for_update()

        if not items.exists():
            return APIResponse.error("Cart is empty")

        shipping_id = request.data.get("shipping_address")
        billing_id = request.data.get("billing_address")

        if not shipping_id:
            return APIResponse.error("Shipping address is required")

        order = Order.objects.create(
            user=request.user,
            shipping_address_id=shipping_id,
            billing_address_id=billing_id,
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

        send_order_confirmation_email(order)

        serializer = OrderSerializer(order)
        return APIResponse.success(serializer.data, message="Order placed successfully")
