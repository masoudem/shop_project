from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    phone_regex = RegexValidator(regex=r'/^(\+98?)?{?(0?9[0-9]{9,9}}?)$/gm', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email' or 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email