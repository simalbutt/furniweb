from django.db import models
from .catagory import Category
from .vendor import Vendor

class Product(models.Model):
    AVAILABILITY_CHOICES = (
        ("in", "In Stock"),
        ("out", "Out of Stock"),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    categories = models.ManyToManyField(Category, related_name="products")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)

    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)

    free_shipping = models.BooleanField(default=False)
    available = models.CharField(max_length=10, choices=AVAILABILITY_CHOICES, default="in")
    
    sold = models.PositiveIntegerField(default=0)
    items_in_stock = models.PositiveIntegerField(default=0)

    created_at = models.DateField()

    # buy_together = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="bought_with")
    related_products = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="related_to")

    def __str__(self):
        return self.title
