from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from cart.models.item import Item
from cart.serializers.cart import CartSerializer
from cart.services import get_user_cart
from product.models.product import Product
from product.models.variant import ProductVariant
from utils.response import APIResponse


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = get_user_cart(request.user)
        serializer = CartSerializer(cart)
        return APIResponse.success(serializer.data)

    def post(self, request):
        cart = get_user_cart(request.user)

        product = Product.objects.get(id=request.data["product"])
        variant = ProductVariant.objects.get(id=request.data["variant"])

        item, created = Item.objects.get_or_create(
            cart=cart,
            product=product,
            variant=variant,
            defaults={
                "quantity": request.data.get("quantity", 1),
                "price": request.data["price"],
            },
        )

        if not created:
            item.quantity += int(request.data.get("quantity", 1))
            item.save()

        return APIResponse.success(message="Item added to cart")
