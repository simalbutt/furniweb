from django.db import models

from .product import Product
from .variant import ProductVariant


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/")


class VariantImage(models.Model):
    variant = models.ForeignKey(
        ProductVariant, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="variants/")
