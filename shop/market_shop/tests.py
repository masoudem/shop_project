import email
from itertools import product
from urllib import response
from django.http import request
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.test.client import Client
from market_user.models import CustomUser
from .serializers import *
from rest_framework.authtoken.models import Token


# Create your tests here.

class TestPost(APITestCase):

    def setUp(self):

        self.user = CustomUser.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@email.com',
            password='test',
            phone_number='09122222222'
        )
        token, created = Token.objects.get_or_create(user=self.user)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        self.shop = mommy.make(Shop)
        self.product = mommy.make(Product, shop=self.shop)
        self.basket = mommy.make(Basket, customer = self.user)
        self.basket_item = mommy.make(BasketItem, product = self.product, basket = self.basket)
        self.product_id = str(self.product.id)
        
        
    def test_shop_api_list(self):
        response = self.client.get(reverse('shop_api_list'))

        self.assertEqual(response.status_code, 200)

    def test_product_api_list(self):
        response = self.client.get(
            reverse('product_api_list', kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 200)

    def test_cart_item_view(self):
        response = self.client.get(reverse('cart_item', request=['test@email.com']))

        self.assertEqual(response.status_code, 200)
        
    def test_cart_item_add_view(self):
        response = self.client.post(reverse('cart_add'), data={'product_id':self.product_id, 'product_count':'3'})
        
        self.assertEqual(response.status_code, 200)



