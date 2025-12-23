from django.contrib import admin
from .models import Order
from cart.models import Item


class OrderItemInline(admin.TabularInline):
    model = Item
    fk_name = "order"
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total_amount", "created_at")
    list_filter = ("status",)
    search_fields = ("user__email",)
    inlines = [OrderItemInline]
