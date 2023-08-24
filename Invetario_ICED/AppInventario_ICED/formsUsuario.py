from django import forms
from .models import *



class UsuariosForm(forms.ModelForm):
    class Meta:
        model=Usuarios
        fields = ['Usu_Nombre', 'Usu_Apellido', 'Usu_tipo','Usu_Celular','Usu_Correo','Usu_Ficha']

        widgets = {
            'Usu_Nombre':forms.TextInput(attrs={'placeholder':'Usu_Nombre'}),
            'Usu_Apellido':forms.TextInput(attrs={'placeholder':'Usu_Apellido'}),
            'Usu_tipo':forms.TextInput(attrs={'placeholder':'Usu_tipo'}),
            'Usu_Celular':forms.TextInput(attrs={'placeholder':'Usu_Celular'}),
            'Usu_Correo':forms.TextInput(attrs={'placeholder':'Usu_Correo'}),
            'Usu_Ficha':forms.TextInput(attrs={'placeholder':'Usu_Ficha'}),
        }