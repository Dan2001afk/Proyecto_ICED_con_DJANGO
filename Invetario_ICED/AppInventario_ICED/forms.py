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
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'Nombre',
            'id':'Nombre',
            'type':'text',
            'class':'form-input',
            'placeholder':'nombre de usuario',
            'maxlength':'20',
            'minlength':'1'
        })

        self.fields['email'].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'type':'text',
            'class':'form-input',
            'placeholder':'Correo',
            'maxlength':'50',
            'minlength':'1'
        })

        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'text',
            'class':'form-input',
            'placeholder':'Contraseña',
            'maxlength':'20',
            'minlength':'1'
        })

        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'text',
            'class':'form-input',
            'placeholder':'Confirmar Contraseña',
            'maxlength':'20',
            'minlength':'1'
        })

        self.fields['rol'].widget.attrs.update({
            'required':'',
            'name':'rol',
            'id':'rol',
            'type':'text',
            'class':'form-input',
            'placeholder':'Rol',
            'maxlength':'20',
            'minlength':'1'
        })

        self.fields['imagen'].widget.attrs.update({
            'required':'',
            'name':'imagen',
            'id':'imagen',
            'type':'text',
            'class':'form-input',
            'placeholder':'Imagen Perfil',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
             'name':'user',
             'id':'user',
             'type':'text',
             'class':'form-input',
             'placeholder':'Usuario',
             'maxlength':'20',
             'minlength':'1'
    })
        

        self.fields['password'].widget.attrs.update({
            'required':'',
             'name':'pass',
             'id':'pass',
             'type':'text',
             'class':'form-input',
             'placeholder':'Contraseña',
             'maxlength':'20',
             'minlength':'1'
    })

    class Meta:
        fields = ['username' , 'password']