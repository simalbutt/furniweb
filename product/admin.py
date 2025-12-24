from django.contrib import admin

from .models import (Category, Product, ProductFeature, ProductImage,
                     ProductVariant, VariantImage)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "vendername",
        "min_price",
        "max_price",
        "available",
        "items_in_stock",
        "sold",
    )
    list_filter = ("available", "categories")
    search_fields = ("title", "description", "vendername")
    inlines = [ProductImageInline, ProductFeatureInline, ProductVariantInline]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("sku", "product", "title", "price", "compare_at", "stock")
    list_filter = ("stock", "product")
    search_fields = ("sku", "title", "product__title")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image")


@admin.register(VariantImage)
class VariantImageAdmin(admin.ModelAdmin):
    list_display = ("variant", "image")


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ("product", "feature")
