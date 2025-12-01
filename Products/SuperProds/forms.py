from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Product, Profile
from django.contrib.auth.models import User
from captcha.fields import CaptchaField



class ProductForm(forms.Modelform):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    description = forms.CharField(max_length=300, widget=forms.TextInput(attrs={"class": "form-control"}))
    
    email =  forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Електрона пошта")
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Введіть пароль")
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Повторіть пароль")
    
    
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
        
        
class  SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={"class": "form-control"}), 
        label="Логін",
        help_text="Введіть імя користувача, максимум 50 символів"
    )
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Ім'я")
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Прізвище")
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Електрона пошта")
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={"class": "form-control"}), label="Номер телефону")
    adress = forms.CharField(max_length=750, required=False, widget=forms.TextInput(attrs={"class": "form-control"}), label="Адреса")
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Введіть пароль")
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Повторіть пароль")
        
        
class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), required=False)
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    captcha = CaptchaField(label="Введіть символи", error_messages={"invalid": "Неправильно ввіли симвооли"})
    
    
class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}),required=False )
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class": "form-control"}), required=False)
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    class Meta:
        model = Profile 
        exclude = ["user"]
        
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))