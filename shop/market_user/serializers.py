from django.conf import settings
from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'password2']
        
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
    
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number',)
    
    