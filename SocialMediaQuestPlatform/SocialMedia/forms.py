from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

# class CreationUserForm(forms.ModelForm):
#     class Meta:
#         model =  User
#         fields = ["username", "password", "email"]