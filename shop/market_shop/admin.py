from django.contrib import admin
from .models import Product, Tag, Category, Basket, BasketItem, Shop
from django.utils.html import format_html


@admin.register(Shop)
class PersonAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="90" height="90"/>'.format(obj.image.url))
        else:
            return "image not found"
    list_display = ("shop_name", "shop_status",
                    "shop_type", "owner", "image_tag")
    image_tag.short_description = 'Image'
    list_editable = ("shop_status",)
    list_filter = ("shop_status",)
    search_fields = ['shop_name']
    actions = ['make_published']

    @admin.action(description='Mark selected shops as active')
    def make_published(self, request, queryset):
        queryset.update(shop_status='act')


class CategoryInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    list_filter = ("category_name",)
    search_fields = ['category_name']
    inlines = [
        CategoryInline,
    ]


@admin.register(Product)
class PersonAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="90" height="90"/>'.format(obj.image.url))

    list_display = ("product_name", "product_unit",
                    "price_per_unit", "image_tag")
    list_filter = ("product_name",)
    search_fields = ['product_name']
    image_tag.short_description = 'Image'


@admin.register(Tag)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("tag_name",)
    list_filter = ("tag_name",)
    search_fields = ['tag_name']


@admin.register(Basket)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("payment_price",)
    list_filter = ("payment_price",)
    search_fields = ['"payment_price"']


@admin.register(BasketItem)
class PersonAdmin(admin.ModelAdmin):
    pass
