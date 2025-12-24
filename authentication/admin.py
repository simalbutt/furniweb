from django.contrib import admin

from .models import Address, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "is_staff", "is_superuser")
    search_fields = ("email", "phone")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "get_full_name",
        "address_type",
        "address",
        "city",
        "postal_code",
        "phone",
        "email",
        "is_default",
    )
    list_filter = ("address_type", "is_default")
    search_fields = ("user__email", "first_name", "last_name", "city", "postal_code")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    get_full_name.short_description = "Full Name"
