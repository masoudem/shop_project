from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^(\+98?)?{?(0?9[0-9]{9,9}}?)$',message='Hashtag doesnt comply'),], max_length=14, blank=True)
    user_type_owner_shop = models.BooleanField(default=False)
    image = models.FileField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class Address(models.Model):
    country_name = models.CharField(max_length=72)
    city_name = models.CharField(max_length=72)
    customer_address = models.CharField(max_length=72)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)