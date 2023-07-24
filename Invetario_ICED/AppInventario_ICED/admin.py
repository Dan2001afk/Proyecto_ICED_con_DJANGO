from django.contrib import admin
from AppInventario_ICED.models import *

@admin.register(Equipos)
class ListaEquipos(admin.ModelAdmin):
    list_display=('Equ_id', 'Equi_tipo', 'Equi_modelo', 'Equi_color','Equi_serial','Equi_estado','equi_especialidad')
    
@admin.register(Usuarios)
class ListaUsuarios(admin.ModelAdmin):
    list_display=('Usu_Documento', 'Usu_Nombre', 'Usu_Apellido', 'Usu_tipo','Usu_Celular','Usu_Correo','Usu_Ficha')

@admin.register(Prestamos)
class ListaPrestamos(admin.ModelAdmin):
    list_display=('Pres_Id', 'Pres_Equipos', 'Pres_Usuarios_Documento', 'Pres_Fec_Entrega','Pres_Hora_Entrega','Pres_Tiempo_Limite','Pres_Observaciones_entrega')

@admin.register(Sanciones)
class ListaSanciones(admin.ModelAdmin):
    list_display=('San_Pres', 'San_Fecha', 'San_Hora','San_tiempo','San_Descripcion')




