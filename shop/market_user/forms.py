from django import forms
from .models import CustomUser


class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'user_type_owner_shop', 'phone_number', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form_control','placeholder':'نام'}),
            'last_name': forms.TextInput(attrs={'class':'form_control','placeholder':'نام خانوادگی'}),
            'email': forms.TextInput(attrs={'class':'form_control','placeholder':'ایمیل'}),
            'user_type_owner_shop': forms.CheckboxInput(attrs={'class':'form_control'}),
            'phone_number': forms.TextInput(attrs={'class':'form_control','placeholder':'شماره همراه'}),
            'password': forms.PasswordInput(attrs={'class':'form_control','placeholder':'رمز '}),
        }
        
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
        
class SignInForm(forms.Form):
    
    email_login = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'نام کاربر', 'class': 'form_control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز کاربر', 'class': 'form_control'}))
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignInForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    