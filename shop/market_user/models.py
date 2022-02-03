from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from .managers import CustomUserManager
from django.utils import timezone
from .sender import send_otp
import random
import string
import uuid
from datetime import timedelta


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    phone_number = models.CharField(validators=[RegexValidator(
        regex=r'^(\+98?)?{?(0?9[0-9]{9,9}}?)$', message='Hashtag doesnt comply'), ], max_length=14, blank=True, unique=True)
    user_type_owner_shop = models.BooleanField(default=False)
    image = models.FileField(blank=True, null=True)
    # USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class Address(models.Model):
    country_name = models.CharField(max_length=72)
    city_name = models.CharField(max_length=72)
    customer_address = models.CharField(max_length=72)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    
    
    
class OtpRequestQuerySet(models.QuerySet):
    def is_valid(self, receiver, request, password):
        current_time = timezone.now()
        return self.filter(
            receiver=receiver,
            request_id=request,
            password=password,
            created__lt=current_time,
            created__gt=current_time-timedelta(seconds=120),

        ).exists()

class OTPManager(models.Manager):

    def get_queryset(self):
        return OtpRequestQuerySet(self.model, self._db)

    def is_valid(self, receiver, request, password):
        return self.get_queryset().is_valid(receiver, request, password)


    def generate(self, data):
        otp = self.model(channel=data['channel'], receiver=data['receiver'])
        otp.save(using=self._db)
        send_otp(otp)
        return otp



def generate_otp():
    rand = random.SystemRandom()
    digits = rand.choices(string.digits, k=4)
    return  ''.join(digits)


class OTPRequest(models.Model):
    class OtpChannel(models.TextChoices):
        PHONE = 'Phone'
        EMAIL = 'E-Mail'

    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    channel = models.CharField(max_length=10, choices=OtpChannel.choices, default=OtpChannel.PHONE)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=4, default=generate_otp)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = OTPManager()
