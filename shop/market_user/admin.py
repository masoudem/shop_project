from django.contrib import admin
from .models import CustomUser, Address
#jsdldflsjfljs

@admin.register(CustomUser)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("email",)
    list_filter = ("email",)
    search_fields = ['email']


@admin.register(Address)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("city_name","country_name")
    list_filter = ("city_name",)
    search_fields = ['city_name']