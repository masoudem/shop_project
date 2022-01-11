from django.conf import settings
from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Shop
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class ShopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shop
        fields = "__all__"
