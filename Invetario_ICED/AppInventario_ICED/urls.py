from django.urls import path
from .views import *
from . import views

urlpatterns=[
    #CRUD Equipos
    path('Equipo',views.Equipo,name='Equipo'),
    path('ListarEquipos',ListadoEquipos.as_view(),name='ListarEquipos'),
    path('insertar/',InsertarEquipos.as_view(),name='insertar'),
    path('ActualizarEquipo',ActualizarEquipo.as_view(),name='actualizar'),
    path('EliminarEquipo/<pk>',EliminarEquipo.as_view(),name='eliminar'),
    #CRUD Usuarios
    path('ListarUsuarios',ListadoUsuarios.as_view(),name='Usuarios'),
    path('insertarUsuario/',InsertarUsuarios.as_view(),name='insertarUsuario'),
    path('formularioUsuarios',views.formularioUsuarios,name='insertarUsuario'),
    path('ActualizarUsuario',ActualizarUsuarios.as_view(),name='actualizarUsuario'),
    path('EliminarUsuario/<pk>',EliminarUsuario.as_view(),name='eliminarUsuario'),
    #CRUD Prestamos
    path('Prestamoss',views.Prestamoss,name='insertarPrestamo'),
    path('ListarPrestamos',ListadoPrestamos.as_view(),name='Prestamos'),
    path('insertarPrestamo/',InsertarPrestamo.as_view(),name='insertarPrestamo'),
    path('ActualizarPrestamo/<pk>',ActualizarPrestamo.as_view(),name='actualizarPrestamo'),
    path('EliminarPrestamo/<pk>',EliminarPrestamo.as_view(),name='eliminarPrestamo'),
    #CRUD Sanciones
    path('ListarSanciones',ListarSanciones.as_view(),name='Sanciones'),
    path('insertarSancion/',InsertarSanciones.as_view(),name='insertar'),
    path('formularioSanciones',views.formularioSanciones,name='insertar'),
    path('ActualizarSanciones/<pk>',ActualizarSanciones.as_view(),name='Actualizar'),
    path('EliminarUsuario/<pk>',EliminarSanciones.as_view(),name='Eliminar'),
]

""" path('index.html',listadoEquipos.as_view(),name='Equipos'),
    path('indexuno.html',listadoUsuarios.as_view(),name='Usuarios'),
    path('indexdos.html',listadoPrestamos.as_view(),name='Prestamos'),
    path('indextres.html',listadoSanciones.as_view(),name='Sanciones'),
"""
