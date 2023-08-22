from django.urls import path
from .views import *
from . import views

urlpatterns=[
    #PORTADA PRINCIPAL
    path('Portada',views.Portada,name='Portada'),
    #LOGIN
    path('Login',views.Login,name='Login'),
    #FORMULARIO
    path('Formulario',views.Formulario,name='Formulario'),
    #CRUD EQUIPOS
    path('Equipo',views.Equipo,name='Equipo'),
    path('ListarEquipos',ListadoEquipos.as_view(),name='ListarEquipos'),
    path('insertar/',InsertarEquipos.as_view(),name='insertar'),
    path('ActualizarEquipo/<pk>',ActualizarEquipo.as_view(),name='actualizar'),
    path('EliminarEquipo/<pk>',EliminarEquipo.as_view(),name='eliminar'),
    path('BuscarEquipo/<int:pk>', BuscarEquipo.as_view(), name='buscar-equipo'),
    path('ContarEquipos', ContarEquipos.as_view(), name='contar-equipos'),

    
    #CRUD USUARIOS
    path('Usuario',views.Usuario,name='Usuario'),
    path('ListarUsuarios', ListarUsuarios.as_view(), name='ListarUsuarios'),
    path('insertarUsuario/', InsertarUsuarios.as_view(), name='insertarUsuario'),
    path('ActualizarUsuario/<int:pk>', ActualizarUsuarios.as_view(), name='actualizarUsuario'),
    path('EliminarUsuario/<int:pk>', EliminarUsuario.as_view(), name='eliminarUsuario'),
    path('BuscarUsuario/<int:pk>', views.BuscarUsuario.as_view(), name='buscarUsuario'),  # Nueva ruta
    
    #CRUD PRESTAMOS
    path('Prestamo',views.Prestamo,name='Prestamo'),
    path('ListarPrestamos',ListadoPrestamos.as_view(),name='Prestamos'),
    path('insertarPrestamo/',InsertarPrestamo.as_view(),name='insertarPrestamo'),
    path('ActualizarPrestamo/<pk>',ActualizarPrestamo.as_view(),name='actualizarPrestamo'),
    path('EliminarPrestamo/<pk>',EliminarPrestamo.as_view(),name='eliminarPrestamo'),

    #CRUD SANCIONES
    path('Sancion',views.Sancion,name='Sancion'),
    path('ListarSanciones',ListarSanciones.as_view(),name='Sanciones'),
    path('insertarSancion/',InsertarSanciones.as_view(),name='insertar'),
    path('ActualizarSanciones/<pk>',ActualizarSanciones.as_view(),name='Actualizar'),
    path('EliminarSancion/<pk>',EliminarSanciones.as_view(),name='Eliminar'),
]

""" path('index.html',listadoEquipos.as_view(),name='Equipos'),
    path('indexuno.html',listadoUsuarios.as_view(),name='Usuarios'),
    path('indexdos.html',listadoPrestamos.as_view(),name='Prestamos'),
    path('indextres.html',listadoSanciones.as_view(),name='Sanciones'),
"""
