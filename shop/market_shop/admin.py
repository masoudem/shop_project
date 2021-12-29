from django.contrib import admin
from .models import Product, Tag, Category, Basket, BasketItem, Shop



@admin.register(Shop)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(BasketItem)
class PersonAdmin(admin.ModelAdmin):
    pass
