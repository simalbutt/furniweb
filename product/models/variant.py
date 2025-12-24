from django.db import models

from .product import Product


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product, related_name="variants", on_delete=models.CASCADE
    )
    sku = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_at = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    stock = models.CharField(
        max_length=10,
        choices=(("in", "In Stock"), ("out", "Out of Stock")),
        default="in",
    )
