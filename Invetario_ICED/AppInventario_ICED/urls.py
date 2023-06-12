from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path('Equipos',ListadoEquipos.as_view(),name='Equipos'),
    path('insertar/',InsertarEquipos.as_view(),name='insertar'),
    
]


""" path('index.html',listadoEquipos.as_view(),name='Equipos'),
    path('indexuno.html',listadoUsuarios.as_view(),name='Usuarios'),
    path('indexdos.html',listadoPrestamos.as_view(),name='Prestamos'),
    path('indextres.html',listadoSanciones.as_view(),name='Sanciones'),
"""
