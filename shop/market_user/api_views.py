from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import *
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *





class SignUpApi(generics.CreateAPIView):
    
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers
    