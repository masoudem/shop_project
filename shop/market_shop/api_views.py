from .filters import ProductListFilter
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser, MultiPartParser


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
        return Product.objects.filter(shop__id = self.kwargs["pk"])
    

class CartItemView(generics.ListAPIView):
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated, )
    

    def get_queryset(self):
        return BasketItem.objects.filter(basket__customer__email=self.request.user)
    
    
class CartItemAddView(generics.CreateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated, )
    parser_classes = (FormParser, MultiPartParser)
    

class CartItemDelView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = BasketItem.objects.all()

    def delete(self, request,  *args, **kwargs):
        print(self.kwargs['pk'])
        email = request.user
        cart_item = BasketItem.objects.filter(basket__customer__email=email)
        target_product = get_object_or_404(cart_item, pk=self.kwargs['pk'])
        product = get_object_or_404(Product, id=target_product.product.id)
        product.product_unit = int(product.product_unit )+ int(target_product.product_count)
        product.save()
        target_product.delete()
        return Response(status=status.HTTP_200_OK, data={"detail": "deleted"})      


class BasketVerifyView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        email = request.user
        basket = Basket.objects.filter(customer__email=email)
        target_product = get_object_or_404(basket, pk=self.kwargs['pk'])
        target_product.basket_status = 'vrf'
        target_product.save()
        return Response(status=status.HTTP_200_OK, data={"detail": "verify"})      

    
class CartItemAddOneView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        print(self.kwargs)
        target_product = BasketItem.objects.get(pk=self.kwargs['pk'])
        product = get_object_or_404(Product, id=target_product.product.id)
        if product.product_unit <= 0:
            return Response(
                data={
                    "detail": "this item is sold out try another one !",
                    "code": "sold_out"})

        target_product.product_count = int(target_product.product_count) + 1
        product.product_unit = product.product_unit - 1

        product.save()
        target_product.save()
        
        return Response(
            status=status.HTTP_226_IM_USED,
            data={"detail": 'one object added', "code": "done"})

        

class CartItemReduceOneView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        
        target_product = BasketItem.objects.get(pk= self.kwargs['pk'])
        product = get_object_or_404(Product, id=target_product.product.id)
        if target_product.product_count == 0:
            return Response(
                data={
                    "detail": "there is no more item like this in tour cart",
                    "code": "no_more"})

        target_product.product_count = int(target_product.procut_count) - 1
        product.product_unit = product.product_unit + 1
        product.save()
        target_product.save()
        return Response(
            status=status.HTTP_226_IM_USED,
            data={
                "detail": 'one object deleted',
                "code": "done"
            })
        

class BasketVerify(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusSerializer
    
    def get_queryset(self):
        return Basket.objects.filter(basket_status = 'vrf', customer__email = self.request.user)
    

class BasketActive(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatusSerializer
    
    def get_queryset(self):
        return Basket.objects.filter(basket_status = 'act', customer__email = self.request.user)