from django.db import models
from .product import Product

class ProductFeature(models.Model):
    product = models.ForeignKey(Product, related_name="features", on_delete=models.CASCADE)
    feature = models.CharField(max_length=255)

    def __str__(self):
        return self.feature
