from django.contrib import admin

from .models import Cart, Item


class CartItemInline(admin.TabularInline):
    model = Item
    fk_name = "cart"
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "session_key", "created_at", "updated_at")
    search_fields = ("user__email", "session_key")
    inlines = [CartItemInline]
