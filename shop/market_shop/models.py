from django.db import models
from market_user.models import CustomUser

class Shop(models.Model):
    PUB = 'pub'
    DEL = 'del'
    NOT = 'not'
    ACT = 'act'
    STATUS_CHOICES = [
        (PUB,'publish'),
        (DEL,'delete'),
        (NOT,'notset'),
        (ACT,'active'),
    ]
    
    shop_name = models.CharField(max_length=72)
    image = models.FileField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    shop_type = models.CharField(max_length=72)
    shop_status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=NOT)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.shop_name
    
    
class Basket(models.Model):
    payment_price = models.CharField(max_length=72)
    product_count = models.PositiveIntegerField()
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    
    
class BasketItem(models.Model):
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    

class Product(models.Model):
    product_name = models.CharField(max_length=72)
    image = models.FileField(null=True, blank=True)
    product_description = models.TextField()
    product_unit = models.PositiveIntegerField()
    price_per_unit = models.CharField(max_length=72)
    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tag_product = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.product_name

class ProductType(models.Model):
    type_name = models.CharField(max_length=72)
    

class Tag(models.Model):
    tag_name = models.CharField(max_length=72)
    
    def __str__(self):
        return self.tag_name
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=72)
     
    def __str__(self):
        return self.category_name

     
