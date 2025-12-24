from django.contrib import admin

from cart.models import Item

from .models import Order


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
