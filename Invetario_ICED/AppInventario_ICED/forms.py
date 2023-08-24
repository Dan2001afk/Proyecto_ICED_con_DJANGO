from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth import get_user_model
from typing import Any
from .models import User

User = get_user_model()

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Documento'].widget.attrs.update({
            'required':'',
             'name':'doc',
             'id':'doc',
             'type':'text',
             'class':'form-input',
             'placeholder':'Documento',
             'maxlength':'20',
             'minlength':'1'
        })    

    rol=forms.CharField(max_length=100)
    imagen=forms.ImageField(required=False)
    Documento = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['Documento','username','email','password1','password2','rol','imagen',]

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username' , 'password']