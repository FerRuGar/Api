from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


# class Registro_Form(forms.ModelForm):   
#     class Meta:
#         model = RegistrarForm
#         fields = '_all_'

# class register(UserCreationForm):
#     email=forms.EmailField()
#     password1=forms.CharField(label='contraseña', widget=forms.PasswordInput)
#     password2=forms.CharField(label='contraseña_rep', widget=forms.PasswordInput)
#     class Meta: 
#         model= User
#         fields= ['username', 'email', 'password1', 'password2']
#         help_texts = {k: "" for k in fields}