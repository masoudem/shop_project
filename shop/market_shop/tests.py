import email
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
        self.product = mommy.make(Product, shop = self.shop)
        

    def test_shop_api_list(self):
        response = self.client.get(reverse('shop_api_list'))

        self.assertEqual(response.status_code, 200)
    
    def test_product_api_list(self):
        response = self.client.get(reverse('product_api_list', kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 200)
    
    # def test_basket_api_create(self):
    #     response = self.client.get(reverse('items', kwargs={"pk": 1}))

    #     self.assertEqual(response.status_code, 200)
        
        
        
    

    # def test_post_details(self):

    #     test = mommy.make(Post)
    #     print(test.slug)
    #     response = self.client.get(reverse("post_details", kwargs={"slug": test.slug}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_comment_details(self):
    #     mommy.make(Comment, _quantity=3)
    #     response = self.client.get(reverse('comment_details'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 3)

    # def test_comment_details(self):
    #     mommy.make(Comment, body='salam')
    #     mommy.make(Comment, _quantity=4)
    #     response = self.client.get(reverse('comment_details', kwargs={"id": 1}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 0)
    #     response2 = self.client.get(reverse('comment_details', kwargs={"id": 7}))
    #     self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    # def test_category_list(self):
    #     mommy.make(Category, _quantity=12)
    #     response = self.client.get(reverse('category_lists'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 12)

    # def test_category_list(self):
    #     mommy.make(Category, _quantity=55)
    #     response = self.client.get(reverse('category_lists'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 55)
