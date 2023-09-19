from django.urls import path
from .views import *
from . import views
from AppInventario_ICED.viewsLogin import *
from django.conf import *
from django.conf.urls.static import *


urlpatterns=[
    
    #PORTADA PRINCIPAL
    path('Portada',views.Portada,name='Portada'),
    #LOGIN
    path('registro/',RegistrarUsuarioView.as_view(),name="registrar_usuario"),
    path('iniciarSesion/',IniciarSesionView.as_view(),name="iniciar_sesion"),
    path('ActualizarUsuario/',PerfilClienteView.as_view(),name="perfil_usuario"),
    path('Login',views.Login,name='Login'),
    path('VistasUsuarios',VistasUsuarios,name="VistaUsarios"),
    #FORMULARIO
    path('Formulario',views.Formulario,name='Formulario'),
    
    
    
    
    #CRUD EQUIPOS
    path('Equipo',views.Equipo,name='Equipo'),
    path('ListarEquipos',ListadoEquipos.as_view(),name='ListarEquipos'),
    path('insertar/',InsertarEquipos.as_view(),name='insertar'),
    path('ActualizarEquipo/<int:pk>',ActualizarEquipo.as_view(),name='actualizar'),
    path('EliminarEquipo/<int:pk>',EliminarEquipo.as_view(),name='eliminar'),
    path('BuscarEquipo/<int:pk>', BuscarEquipo.as_view(), name='buscar-equipo'),
    path('ContarEquipos', ContarEquipos.as_view(), name='contar-equipos'),
    path('ContarActivos', ContarActivos.as_view(), name='contar-activos'),
    path('ContarInactivos', ContarInactivos.as_view(), name='contar-inactivos'),

    #CRUD USUARIOS
    path('Usuario',views.Usuario,name='Usuario'),
    path('ListarUsuarios', ListarUsuarios.as_view(), name='ListarUsuarios'),
    path('insertarUsuario/', InsertarUsuarios.as_view(), name='insertarUsuario'),
    path('formularioInsertar',views.Formulario,name="insertarf"),
    path('ActualizarUsuario/<int:pk>', ActualizarUsuarios.as_view(), name='actualizarUsuario'),
    path('EliminarUsuario/<int:pk>', EliminarUsuario.as_view(), name='eliminarUsuario'),
    path('BuscarUsuario/<int:pk>', views.BuscarUsuario.as_view(), name='buscarUsuario'),  # Nueva ruta
    path('ContarUsuarios', ContarUsuarios.as_view(), name='cantidad_usuarios'),
    path('ContarAprendices', ContarAprendices.as_view(), name='cantidad_aprendices'),
    
    #CRUD PRESTAMOS
    path('Prestamo',views.Prestamo,name='Prestamo'),
    path('ListarPrestamos',ListadoPrestamos.as_view(),name='Prestamos'),
    path('insertarPrestamo/',InsertarPrestamos.as_view(),name='insertarPrestamo'),
    path('ActualizarPrestamo/<int:pk>',ActualizarPrestamo.as_view(),name='actualizarPrestamo'),
    path('BuscarPrestamo/<int:pk>', BuscarPrestamo.as_view(), name='buscar-prestamo'),
    path('EliminarPrestamo/<int:pk>',EliminarPrestamo.as_view(),name='eliminarPrestamo'),
    path('verificarPrestamo/', VerificarPrestamo.as_view(), name='verificar-prestamo'),
    path('ContarPrestamos', ContarPrestamos.as_view(), name='cantidad_prestamos'),

    #CRUD SANCIONES
    path('Sancion',views.Sancion,name='Sancion'),
    path('ListarSanciones',ListarSanciones.as_view(),name='Sanciones'),
    path('insertarSancion/',InsertarSanciones.as_view(),name='insertar'),
    path('ActualizarSanciones/<pk>',ActualizarSanciones.as_view(),name='Actualizar'),
    path('EliminarSancion/<pk>',EliminarSanciones.as_view(),name='Eliminar'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" path('index.html',listadoEquipos.as_view(),name='Equipos'),
    path('indexuno.html',listadoUsuarios.as_view(),name='Usuarios'),
    path('indexdos.html',listadoPrestamos.as_view(),name='Prestamos'),
    path('indextres.html',listadoSanciones.as_view(),name='Sanciones'),
"""
