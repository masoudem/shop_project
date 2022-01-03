from django import forms
from .models import Shop



class ShopForm(forms.ModelForm):
    
    class Meta:
        model = Shop
        fields = ['shop_name', 'image','shop_type']
        widgets = {
            'shop_name': forms.TextInput(attrs={'class':'form_control','placeholder':' نام فروشگاه'}),
            'image': forms.FileInput(attrs={'class':'form_control'}),
            'shop_type': forms.TextInput(attrs={'class':'form_control','placeholder':'درباره ی فروشگاه'}),
        }