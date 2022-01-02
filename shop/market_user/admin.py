from django.contrib import admin
from django.forms import fields
from .models import CustomUser, Address
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import SignUpForm

@admin.register(CustomUser)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("email","user_type_owner_shop")
    list_filter = ("email",)
    search_fields = ['email']


@admin.register(Address)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("city_name","country_name")
    list_filter = ("city_name",)
    search_fields = ['city_name']


