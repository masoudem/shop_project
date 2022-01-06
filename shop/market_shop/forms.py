from django import forms

from .models import Product, Shop, Category, Tag



class ShopForm(forms.ModelForm):
    
    class Meta:
        model = Shop
        fields = ['shop_name', 'image','shop_type']
        widgets = {
            'shop_name': forms.TextInput(attrs={'class':'form_control','placeholder':' نام فروشگاه'}),
            'image': forms.FileInput(attrs={'class':'form_control'}),
            'shop_type': forms.TextInput(attrs={'class':'form_control','placeholder':'درباره ی فروشگاه'}),
        }


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['product_name', 'image','product_description', 'product_unit', 'price_per_unit', 'category', 'tag_product']
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form_control','placeholder':' نام محصول'}),
            'image': forms.FileInput(attrs={'class':'form_control'}),
            'product_description': forms.Textarea(attrs={'class':'form_control','placeholder':'توضیح محصول'}),
            'product_unit': forms.NumberInput(attrs={'class':'form_control'}),
            'price_per_unit': forms.TextInput(attrs={'class':'form_control','placeholder':'قیمت محصول'}),
            'category': forms.Select(attrs={'class':'form_control'}),
            'tag_product': forms.SelectMultiple(attrs={'class':'form_control'}),
        }
        

class CategoryForm(forms.ModelForm):
   
    class Meta :
        model = Category
        fields = '__all__'
        

class TagForm(forms.ModelForm):
   
    class Meta :
        model = Tag
        fields = '__all__'

