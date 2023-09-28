from django import forms
from .models import *



class UsuariosForm(forms.ModelForm):
    
    class Meta:
        model=Usuarios
        fields = ['Usu_Nombre', 'Usu_Apellido', 'Usu_tipo','Usu_Celular','Usu_Correo','Usu_Ficha']
