from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.serializers import Serializer
from .filters import ProductListFilter
# Create your views here.
from rest_framework import generics, status, mixins
from rest_framework.generics import get_object_or_404

from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter


class ShopAPIList(generics.ListAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = ShopSerializer
    
    def get_queryset(self):
        return Shop.objects.all()
    
class ProductAPIList(generics.ListAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductListFilter
    
    def get_queryset(self):
        print(self.kwargs["pk"])
        return Product.objects.filter(shop__id = self.kwargs["pk"])
    

class BasketAPIList(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializer
    
    def create(self):
        basket = Basket.objects.create(customer__email = self.request.user)
        basket.save()
        return basket
    
    
class ItemAPIList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        self.pk = self.kwargs['pk']
        return BasketItem.objects.filter(basket__customer__email = self.request.user, product__shop__pk = self.kwargs['pk']).exclude(basket__basket_status = 'vrf')
    
    def create(self, request, *args, **kwargs):
        print(kwargs)
        basket = Basket.objects.filter(basket_status = 'vrf', basketitem__product__shop__pk = self.kwargs['pk'], customer__email = self.request.user)
        if basket:
            BasketAPIList()
            basket = Basket.objects.filter(basket__basketitem__product__shop__pk = self.kwargs['pk'], customer__email = self.request.user).exclude(basket_status = 'vrf')
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save(basket= basket)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BasketVerify(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializer
    
    def get_queryset(self):
        return Basket.objects.filter(basket_stauts = 'vrf', customer__email = self.request.user)
    

class BasketActive(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializer
    
    def get_queryset(self):
        return Basket.objects.filter(basket_stauts = 'act', customer__email = self.request.user)