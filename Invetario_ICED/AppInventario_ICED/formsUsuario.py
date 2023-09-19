from django import forms
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth import get_user_model
from typing import Any
from .models import User

User = get_user_model()

class UsuariosForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Usu_Nombre'].widget.attrs.update({
            'required':'',
            'name':'Usu_Nombre',
            'id':'Usu_Nombre',
            'type':'text',
            'class':'form-input',
            'placeholder':'Nombre',
            'maxlength':'20',
            'minlength':'1'
        }),

        self.fields['Usu_Apellido'].widget.attrs.update({
            'required':'',
            'name':'Usu_Apellido',
            'id':'Usu_Apellido',
            'type':'text',
            'class':'form-input',
            'placeholder':'Apellido',
            'maxlength':'20',
            'minlength':'1'
        }),

        self.fields['Usu_tipo'].widget.attrs.update({
            'required':'',
            'name':'Usu_tipo',
            'id':'Usu_tipo',
            'type':'text',
            'class':'form-input',
            'placeholder':'Tipo',
            'maxlength':'20',
            'minlength':'1'
        }),

        self.fields['Usu_Celular'].widget.attrs.update({
            'required':'',
            'name':'Usu_Celular',
            'id':'Usu_Celular',
            'type':'text',
            'class':'form-input',
            'placeholder':'Celular',
            'maxlength':'20',
            'minlength':'1'
        }),

        self.fields['Usu_Correo'].widget.attrs.update({
            'required':'',
            'name':'Usu_Correo',
            'id':'Usu_Correo',
            'type':'text',
            'class':'form-input',
            'placeholder':'Correo',
            'maxlength':'20',
            'minlength':'1'
        }),

        self.fields['Usu_Ficha'].widget.attrs.update({
            'required':'',
            'name':'Usu_Ficha',
            'id':'Usu_Ficha',
            'type':'text',
            'class':'form-input',
            'placeholder':'Numero ficha',
            'maxlength':'20',
            'minlength':'1'
        })




    class Meta:
        model=Usuarios
        fields = ['Usu_Nombre', 'Usu_Apellido', 'Usu_tipo','Usu_Celular','Usu_Correo','Usu_Ficha']