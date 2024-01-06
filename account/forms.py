from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Account


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['first_name','last_name','username','email','phone_number','password1','password2']

    #for custom css 
    first_name =forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'First Name'
        })
    )
    last_name =forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Last Name'
        })
    )
    username=forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Last Name'
        })
    )
    phone_number =forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Last Name',
            
        })
    )
    email =forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Email Address'
        })
    )
    password1 =forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Create Password',
            # 'type':'password'
        })
    )
    password2 =forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Confirm Password',
            # 'type':'password'
        })
    )

class UserLoginForm(AuthenticationForm):
    email= forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'})
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password'})
    )