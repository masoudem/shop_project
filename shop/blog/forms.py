from django import forms
from market_user.models import CustomUser
from .models import Comment, Post, Tag, Category, UserProfile
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description',
                  'bodytext', 'category', 'tag', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'خلاصه'}),
            'bodytext': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(),
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['post']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربر'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'نام کاربر', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'رمز کاربر', 'class': 'form-control'}))


class UserFormModel(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'email', 'password']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز کاربر'}),
        }


class AvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']


class NewPasswordForm(forms.Form):

    password = forms.CharField(widget=forms.PasswordInput)
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password_1 = cleaned_data.get("password_1")
        password_2 = cleaned_data.get("password_2")

        if password_1 != password_2:
            raise ValidationError(
                "password1 and password2  not equal"
            )
        if password_1 == '1234':
            raise ValidationError(
                "password1  have not 1234"
            )
