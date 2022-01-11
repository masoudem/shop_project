from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404

from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class ShopAPIList(generics.ListAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = ShopSerializer
    
    def get_queryset(self):
        return Shop.objects.all()
        

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 