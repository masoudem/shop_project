from django.contrib import admin
from .models import Product, Tag, Category, Basket, BasketItem, Shop


@admin.register(Shop)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("shop_name","shop_status","shop_type","owner")
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
    list_display = ("product_name","product_unit","price_per_unit")
    list_filter = ("product_name",)
    search_fields = ['product_name']


@admin.register(Tag)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("tag_name",)
    list_filter = ("tag_name",)
    search_fields = ['tag_name']


@admin.register(Basket)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("payment_price","product_count")
    list_filter = ("payment_price",)
    search_fields = ['"payment_price"']


@admin.register(BasketItem)
class PersonAdmin(admin.ModelAdmin):
    pass
