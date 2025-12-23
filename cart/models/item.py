from django.db import models
from django.conf import settings
from product.models.product import Product
from product.models.variant import ProductVariant
from cart.models.cart import Cart
from orders.models.order import Order  

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, related_name="items")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name="items")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} x {self.quantity}"
