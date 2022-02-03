from django.contrib import admin
from .models import CustomUser, Address, OTPRequest
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(OTPRequest)

@admin.register(CustomUser)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "user_type_owner_shop")
    list_filter = ("phone_number",)
    search_fields = ['phone_number']


@admin.register(Address)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("city_name", "country_name")
    list_filter = ("city_name",)
    search_fields = ['city_name']
