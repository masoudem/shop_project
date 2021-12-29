from django.db import models
from market_user.models import CustomUser

class Shop(models.Model):
    PUB = 'pub'
    DEL = 'del'
    NOT = 'not'
    STATUS_CHOICES = [
        (PUB,'publish'),
        (DEL,'delete'),
        (NOT,'notset'),
    ]
    
    shop_name = models.CharField(max_length=72)
    image = models.FileField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    shop_type = models.CharField(max_length=72)
    shop_status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=NOT)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    
class Basket(models.Model):
    payment_price = models.CharField(max_length=72)
    product_count = models.PositiveIntegerField()
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    
    
class BasketItem(models.Model):
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE) 
    

class Product(models.Model):
    product_name = models.CharField(max_length=72)
    product_description = models.TextField()
    product_unit = models.PositiveIntegerField()
    price_per_unit = models.CharField(max_length=72)
    basket_item = models.ForeignKey('BasketItem', on_delete=models.SET_NULL, null=True)
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tag_product = models.ManyToManyField('Tag')
    

class ProductType(models.Model):
    type_name = models.CharField(max_length=72)
    

class Tag(models.Model):
    tag_name = models.CharField(max_length=72)
    
    
class Category(models.Model):
     category = models.CharField(max_length=72)
     


     
