from rest_framework import serializers
from django.shortcuts import get_object_or_404
from market_user.models import CustomUser
from .models import Basket, BasketItem, Product, Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = "__all__"


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(
        required=True

    )

    class Meta:
        model = BasketItem
        fields = ['product_id', 'product_count']
        extra_kwargs = {
            'product_id': {'required': True},
            'product_count': {'required': True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.get(email=self.context['request'].user)
        product = get_object_or_404(Product, id=validated_data['product_id'])
        if product.product_unit == 0:
            raise serializers.ValidationsError(
                {'not available': 'the product is not available.'})
        basket = Basket.objects.filter(
            basketitem__product=product, customer=user).exclude(basket_status='vrf')
        if basket is not None:
            basket = Basket.objects.create(customer=user)
            basket.save()
        cart_item = BasketItem.objects.create(
            basket=basket,
            product=product,
            product_count=validated_data['product_count']
        )
        cart_item.save()
        cart_item.add_amount()
        product.product_unit = product.product_unit - cart_item.product_count
        product.save()
        return cart_item
