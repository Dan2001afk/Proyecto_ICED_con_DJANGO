from typing import Any
from django import http
from django.shortcuts import get_object_or_404, render
from AppInventario_ICED.models import *
from django.views.generic import *
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json  

# class listadoEquipos(ListView):
#     model=Equipos
#     template_name="index.html"


#class listadoUsuarios(ListView):
#   model=Usuarios
#   template_name="indexuno.html"

#class listadoPrestamos(ListView):
#    model=Prestamos
#    template_name="indexdos.html"

#class listadoSanciones(ListView):
#    model=Sanciones
#    template_name="indextres.html"

#VistasUsuarios
def VistasUsuarios(request):
    return render(request,"VistasUsuarios.html")

class ListadoDatos(View):
    def get(self, request):
        if request.user.is_authenticated:
            usuario = request.user.Documento
            prestamos = Prestamos.objects.filter(Pres_Usuarios_Documento=usuario)
            Datos = []

            for prestamo in prestamos:
                equipo = prestamo.Pres_Equipos
                usuario_dict = usuario.to_dict()  # Llama al método to_dict para serializar el usuario
                Datos.append({
                    'Dispositivo': f"{equipo.Equi_tipo} {equipo.Equi_modelo}",
                    'Observaciones': prestamo.Pres_Observaciones_entrega,
                    'Serial': equipo.Equi_serial,
                    'Especialidad': equipo.equi_especialidad,
                    'Usuario': usuario_dict,  # Usa el diccionario del usuario en lugar del objeto
                    'Pres_Hora_Entrega': prestamo.Pres_Hora_Entrega
                })

            return JsonResponse(Datos, safe=False)
        else:
            return JsonResponse([], safe=False) 

def listar_prestamos_usuario(request, usuario_id):
    usuario = Usuarios.objects.get(pk=usuario_id)
    prestamos = Prestamos.objects.filter(Pres_Usuarios_Documento=usuario)
    return render(request, 'VistasUsuarios.html', {'usuario': usuario, 'prestamos': prestamos})
#equipos
class ListadoEquipos(ListView):
    def get(self,request):
        datos=Equipos.objects.all()
        Datos_Equipos=[]
        for i in datos:
            Datos_Equipos.append({
                'Equ_id':i.Equ_id,
                'Equi_tipo':i.Equi_tipo,
                'Equi_modelo':i.Equi_modelo,
                'Equi_color':i.Equi_color,
                'Equi_serial':i.Equi_serial,
                'Equi_estado':i.Equi_estado,
                'equi_especialidad':i.equi_especialidad
            })
        # DatosEquipos=list(Datos)
        return JsonResponse(Datos_Equipos,safe=False)

class InsertarEquipos(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"Error":"Error en el Documento"})
        datos=json.loads(request.body)
        Equi_tipo = datos.get('Equi_tipo')
        Equi_modelo = datos.get('Equi_modelo')
        Equi_color = datos.get('Equi_color')
        Equi_serial = datos.get('Equi_serial')
        Equi_estado = datos.get('Equi_estado')
        equi_especialidad = datos.get('equi_especialidad')
        print("datos",request.POST)
        Equipos.objects.create(Equi_tipo=Equi_tipo,Equi_modelo=Equi_modelo,Equi_color=Equi_color,Equi_serial=Equi_serial,Equi_estado=Equi_estado,equi_especialidad=equi_especialidad)
        return JsonResponse({"mensaje":"Datos Guardados"})

        # return render(request,"formulario.html",{'mensaje':'Datos Guardados'})
        
def Equipo(request):
    return render(request,"Equipos.html")

class ActualizarEquipo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request,pk):
            
        try:
            ActuEquipo=Equipos.objects.get(pk=pk)
        except Equipos.DoesNotExist:
            return JsonResponse({"Error":"El documento no existe"})
        data=json.loads(request.body)
        ActuEquipo.Equ_id=data.get('Equ_id')
        ActuEquipo.Equi_tipo=data.get('Equi_tipo')
        ActuEquipo.Equi_modelo=data.get('Equi_modelo')
        ActuEquipo.Equi_color=data.get('Equi_color')
        ActuEquipo.Equi_serial=data.get('Equi_serial')
        ActuEquipo.Equi_estado=data.get('Equi_estado')
        ActuEquipo.equi_especialidad=data.get('equi_especialidad')
        ActuEquipo.save()
        return JsonResponse({"Mensaje":"Datos Actualizados"})

class EliminarEquipo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self,request,pk):
        try:
            DeleteEquipo=Equipos.objects.get(pk=pk)
        except Equipos.DoesNotExist:
            return JsonResponse({"Error":"El Equipo no existe"})
        DeleteEquipo.delete()
        return JsonResponse({"Mensaje":"Equipo Eliminado"})
    
class BuscarEquipo(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, equi_serial):
        try:
            equipo = Equipos.objects.get(Equi_serial=equi_serial)
        except Equipos.DoesNotExist:
            return JsonResponse({"Error": "El equipo no existe"})
        
        datos_equipo = {
            'Equ_id': equipo.Equ_id,
            'Equi_tipo': equipo.Equi_tipo,
            'Equi_modelo': equipo.Equi_modelo,
            'Equi_color': equipo.Equi_color,
            'Equi_serial': equipo.Equi_serial,
            'Equi_estado': equipo.Equi_estado,
            'equi_especialidad': equipo.equi_especialidad
        }
        
        return JsonResponse(datos_equipo)
    
class BuscarEquipoID(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        try:
            equipo = Equipos.objects.get(pk=pk)
        except Equipos.DoesNotExist:
            return JsonResponse({"Error": "El equipo no existe"})
        
        datos_equipo = {
            'Equ_id': equipo.Equ_id,
            'Equi_tipo': equipo.Equi_tipo,
            'Equi_modelo': equipo.Equi_modelo,
            'Equi_color': equipo.Equi_color,
            'Equi_serial': equipo.Equi_serial,
            'Equi_estado': equipo.Equi_estado,
            'equi_especialidad': equipo.equi_especialidad
        }
        
        return JsonResponse(datos_equipo)  
#metodos adicionales

class ContarActivos(View):
    def get(self, request):
        cantidad_equipos_activos = Equipos.objects.filter(Equi_estado='Activo').count()
        return JsonResponse({"cantidad_equipos_activos": cantidad_equipos_activos})


class ContarEquipos(View):
    def get(self, request):
        cantidad_equipos = Equipos.objects.count() 
        return JsonResponse({"cantidad_equipos": cantidad_equipos})


class ContarInactivos(View):
    def get(self, request):
        cantidad_equipos_Inactivos = Equipos.objects.filter(Equi_estado='Inactivo').count()
        return JsonResponse({"cantidad_equipos_Inactivos": cantidad_equipos_Inactivos})



#USUARIOS
class ListarUsuarios(View):
    def get(self, request):
        datos = Usuarios.objects.all()
        Datos_usuarios = []
        for i in datos:
            Datos_usuarios.append({
                'Usu_Documento': i.Usu_Documento,
                'Usu_Nombre': i.Usu_Nombre,
                'Usu_Apellido': i.Usu_Apellido,
                'Usu_tipo': i.Usu_tipo,
                'Usu_Celular': i.Usu_Celular,
                'Usu_Correo': i.Usu_Correo,
                'Usu_Ficha': i.Usu_Ficha
            })
        return JsonResponse(Datos_usuarios, safe=False)

class InsertarUsuarios(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def post(self,request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"Error":"Error en el Documento"})
        datos=json.loads(request.body)

        Usu_Documento = datos.get('Usu_Documento')
        Usu_Nombre = datos.get('Usu_Nombre')
        Usu_Apellido = datos.get('Usu_Apellido')
        Usu_tipo = datos.get('Usu_tipo')
        Usu_Celular = datos.get('Usu_Celular')
        Usu_Correo = datos.get('Usu_Correo')
        Usu_Ficha = datos.get('Usu_Ficha')
        print("datos",request.POST)
        Usuarios.objects.create(Usu_Documento=Usu_Documento,Usu_Nombre=Usu_Nombre,Usu_Apellido=Usu_Apellido,Usu_tipo=Usu_tipo,Usu_Celular=Usu_Celular,Usu_Correo=Usu_Correo,Usu_Ficha=Usu_Ficha)
        return JsonResponse({"mensaje":"Datos Guardados"})
    
def Usuario(request):
    return render(request,"Usuarios.html")

class ActualizarUsuarios(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request,pk):
            
        try:
            registro=Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return JsonResponse({"Error":"El Usuario no existe"})
        data=json.loads(request.body)
        registro.Usu_Documento=data.get('Usu_Documento')
        registro.Usu_Nombre=data.get('Usu_Nombre')
        registro.Usu_Apellido=data.get('Usu_Apellido')
        registro.Usu_tipo=data.get('Usu_tipo')
        registro.Usu_Celular=data.get('Usu_Celular')
        registro.Usu_Correo=data.get('Usu_Correo')
        registro.Usu_Ficha=data.get('Usu_Ficha')
        registro.save()
        return JsonResponse({"Mensaje":"Datos Actualizados"})
    
class EliminarUsuario(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self,request,pk):
        try:
            registro=Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return JsonResponse({"Error":"El Usuario no existe"})
        registro.delete()
        return JsonResponse({"Mensaje":"Datos Eliminados"})

class BuscarUsuario(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return JsonResponse({"Error": "El Usuario no existe"})
        datos_usuario = {
            'Usu_Documento': usuario.Usu_Documento,
            'Usu_Nombre': usuario.Usu_Nombre,
            'Usu_Apellido': usuario.Usu_Apellido,
            'Usu_tipo': usuario.Usu_tipo,
            'Usu_Celular': usuario.Usu_Celular,
            'Usu_Correo': usuario.Usu_Correo,
            'Usu_Ficha': usuario.Usu_Ficha
        }
        return JsonResponse(datos_usuario)

#metodos adicionales
class ContarUsuarios(View):
    def get(self, request):
        cantidad_usuarios=Usuarios.objects.count()
        return JsonResponse({"cantidad_usuarios":cantidad_usuarios}) 

class ContarAprendices(View):
    def get(self, request):
        cantidad_aprendices=Usuarios.objects.filter(Usu_tipo='Aprendiz').count()
        return JsonResponse({"cantidad_aprendices":cantidad_aprendices}) 

class ContarInstructor(View):
    def get(self, request):
        cantidad_instructores=Usuarios.objects.filter(Usu_tipo='Instructor').count()
        return JsonResponse({"cantidad_instructores":cantidad_instructores}) 





#PRETAMOS
class ListadoPrestamos(ListView):
    def get(self,request):
        datos=Prestamos.objects.all()
        Datos_Prestamos=[]
        for i in datos:
            Datos_Prestamos.append({
                'Pres_Id':i.Pres_Id,
                'Pres_Equipos_id':i.Pres_Equipos_id,
                'Pres_Usuarios_Documento_id':i.Pres_Usuarios_Documento_id,
                'Pres_Fec_Entrega':i.Pres_Fec_Entrega,
                'Pres_Hora_Entrega':i.Pres_Hora_Entrega,
                'Pres_Tiempo_Limite':i.Pres_Tiempo_Limite,
                'Pres_Observaciones_entrega':i.Pres_Observaciones_entrega,
            })
        # DatosEquipos=list(Datos)
        return JsonResponse(Datos_Prestamos,safe=False)    
    
class InsertarPrestamos(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            datos = json.loads(request.body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({"Error": "Error en el Documento"})

        Pres_Equipos_serial = datos.get('Pres_Equipos_serial')  # Cambiado a Pres_Equipos_serial en lugar de Pres_Equipos_id
        Pres_Usuarios_Documento_id = datos.get('Pres_Usuarios_Documento_id')
        Pres_Tiempo_Limite = datos.get('Pres_Tiempo_Limite')

        # Validación extra si existe algún equipo o usuario que ya tenga un préstamo
        if Prestamos.objects.filter(Pres_Equipos__Equi_serial=Pres_Equipos_serial).exists():
            return JsonResponse({"Error": "El equipo ya está en préstamo"})
        
        if Prestamos.objects.filter(Pres_Usuarios_Documento_id=Pres_Usuarios_Documento_id).exists():
            return JsonResponse({"Error": "El usuario ya tiene un préstamo activo"})

        equipo = get_object_or_404(Equipos, Equi_serial=Pres_Equipos_serial)  # Buscar por número de serie en lugar de ID
        usuario = get_object_or_404(Usuarios, Usu_Documento=Pres_Usuarios_Documento_id)
        
        # Definir el campo automático
        pres_observaciones_entrega = "En buen estado"

        Prestamos.objects.create(
            Pres_Equipos=equipo,
            Pres_Usuarios_Documento=usuario,
            Pres_Tiempo_Limite=Pres_Tiempo_Limite,
            Pres_Observaciones_entrega=pres_observaciones_entrega,
        )

        # Actualizar el estado del equipo
        equipo.Equi_estado = "En préstamo"
        equipo.save()

        return JsonResponse({"mensaje": "Préstamo registrado"})

def Prestamo(request):
    return render(request,"Prestamos.html")

class ActualizarPrestamo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request,pk):
            
        try:
            registro=Prestamos.objects.get(pk=pk)
        except Prestamos.DoesNotExist:
            return JsonResponse({"Error":"El Prestamo no existe"})
        data=json.loads(request.body)
        registro.Pres_Id=data.get('Pres_Id')
        registro.Pres_Equipos_id=data.get('Pres_Equipos_id')
        registro.Pres_Usuarios_Documento_id=data.get('Pres_Usuarios_Documento_id')
        registro.Pres_Fec_Entrega=data.get('Pres_Fec_Entrega')
        registro.Pres_Hora_Entrega=data.get('Pres_Hora_Entrega')
        registro.Pres_Tiempo_Limite=data.get('Pres_Tiempo_Limite')
        registro.Pres_Observaciones_entrega=data.get('Pres_Observaciones_entrega')
        registro.save()
        return JsonResponse({"Mensaje":"Datos Actualizados"})
    
class EliminarPrestamo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, pk):
        try:
            prestamo = Prestamos.objects.get(pk=pk)
        except Prestamos.DoesNotExist:
            return JsonResponse({"Error": "El Prestamo no existe"})

        # Crear un nuevo objeto Historial antes de eliminar el préstamo
        Historial.objects.create(
            Pres_Equipos=prestamo.Pres_Equipos,
            Pres_Usuarios_Documento=prestamo.Pres_Usuarios_Documento,
            Pres_Fec_Entrega=prestamo.Pres_Fec_Entrega,
            Pres_Hora_Entrega=prestamo.Pres_Hora_Entrega,
            Pres_Tiempo_Limite=prestamo.Pres_Tiempo_Limite,
            Pres_Observaciones_entrega=prestamo.Pres_Observaciones_entrega
        )

        # Recupera el equipo asociado al préstamo
        equipo = prestamo.Pres_Equipos

        # Cambia el estado del equipo de nuevo a "Activo"
        equipo.Equi_estado = "Activo"
        equipo.save()

        # Luego, elimina el préstamo
        prestamo.delete()

        return JsonResponse({"Mensaje": "Datos Eliminados"})
      
class BuscarPrestamo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        try:
            prestamo = Prestamos.objects.get(pk=pk)
        except Prestamos.DoesNotExist:
            return JsonResponse({"Error": "El Prestamo no existe"})
        
        datos_prestamo = {
            'Pres_Id': prestamo.Pres_Id,
            'Pres_Equipos_id': prestamo.Pres_Equipos_id,
            'Pres_Usuarios_Documento_id': prestamo.Pres_Usuarios_Documento_id,
            'Pres_Fec_Entrega': prestamo.Pres_Fec_Entrega,
            'Pres_Hora_Entrega': prestamo.Pres_Hora_Entrega,
            'Pres_Tiempo_Limite': prestamo.Pres_Tiempo_Limite,
            'Pres_Observaciones_entrega': prestamo.Pres_Observaciones_entrega
        }
        
        return JsonResponse(datos_prestamo)

class VerificarPrestamo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            datos = json.loads(request.body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({"Error": "Error en el Documento"})

        Pres_Equipos_serial = datos.get('Pres_Equipos_serial')
        Pres_Usuarios_Documento_id = datos.get('Pres_Usuarios_Documento_id')

        response_data = {}  # Respuesta que enviarás al cliente

        # Validación para verificar si el equipo ya está en préstamo
        if Prestamos.objects.filter(Pres_Equipos__Equi_serial=Pres_Equipos_serial).exists():
            response_data["error"] = "El equipo ya está en préstamo"

        # Validación para verificar si el usuario ya tiene un préstamo activo
        if Prestamos.objects.filter(Pres_Usuarios_Documento_id=Pres_Usuarios_Documento_id).exists():
            response_data["error"] = "El usuario ya tiene un préstamo activo"

        return JsonResponse(response_data)
   
#metodos adicionales
class ContarPrestamos(View):
    def get(self, request):
        cantidad_prestamos=Prestamos.objects.count()
        return JsonResponse({"cantidad_prestamos":cantidad_prestamos}) 



#SANCIONES
class ListarSanciones(ListView):
    def get(self,request):
        datos=Sanciones.objects.all()
        Datos_Sanciones=[]
        for i in datos:
            Datos_Sanciones.append({
                'San_Id':i.San_Id,
                'San_Pres_id':i.San_Pres_id,
                'San_Fecha':i.San_Fecha,
                'San_Hora':i.San_Hora,
                'San_tiempo':i.San_tiempo,
                'San_Descripcion':i.San_Descripcion,

            })
        # DatosEquipos=list(Datos)
        return JsonResponse(Datos_Sanciones,safe=False)

class InsertarSanciones(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"Error":"Error en el Documento"})
        datos=json.loads(request.body)
        San_Pres_id = datos.get('San_Pres_id')
        San_tiempo = datos.get('San_tiempo')
        San_Descripcion = datos.get('San_Descripcion')
        print("datos",request.POST)
        Sanciones.objects.create(San_Pres_id=San_Pres_id,San_tiempo=San_tiempo,San_Descripcion=San_Descripcion)
        return JsonResponse({"mensaje":"Datos Guardados"})
        
def Sancion(request):
    return render(request,"Sanciones.html")

class ActualizarSanciones(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def put(self, request,pk):
            
        try:
            ActuSancion=Sanciones.objects.get(pk=pk)
        except Sanciones.DoesNotExist:
            return JsonResponse({"Error":"la sancion no existe"})
        data=json.loads(request.body)
        ActuSancion.San_Pres_id=data.get('San_Pres_id')
        ActuSancion.San_Fecha=data.get('San_Fecha')
        ActuSancion.San_Hora=data.get('San_Hora')
        ActuSancion.San_tiempo=data.get('San_tiempo')
        ActuSancion.San_Descripcion=data.get('San_Descripcion')
        ActuSancion.save()
        return JsonResponse({"Mensaje":"Datos Actualizados"})
    
class EliminarSanciones(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self,request,pk):
        try:
            Delete=Sanciones.objects.get(pk=pk)
        except Sanciones.DoesNotExist:
            return JsonResponse({"Error":"La Sancion no existe"})
        Delete.delete()
        return JsonResponse({"Mensaje":"Sancion Eliminada"})

class BuscarSancion(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        try:
            sancion = Sanciones.objects.get(pk=pk)
        except Sanciones.DoesNotExist:
            return JsonResponse({"Error": "La sanción no existe"})
        
        datos_sancion = {
            'San_Id': sancion.San_Id,
            'San_Pres_id': sancion.San_Pres_id,
            'San_Fecha': sancion.San_Fecha,
            'San_Hora': sancion.San_Hora,
            'San_tiempo': sancion.San_tiempo,
            'San_Descripcion': sancion.San_Descripcion,
        }
        
        return JsonResponse(datos_sancion)

#HISTORIAL DE LOS PRESTAMOS

class ListarHistorial(View):
    def get(self, request):
        historial = Historial.objects.all()
        Datos_Historial = []

        for registro in historial:
            Datos_Historial.append({
                'Pres_Id': registro.Pres_Id,
                'Pres_Equipos_id': registro.Pres_Equipos_id,
                'Pres_Usuarios_Documento_id': registro.Pres_Usuarios_Documento_id,
                'Pres_Fec_Entrega': registro.Pres_Fec_Entrega,
                'Pres_Hora_Entrega': registro.Pres_Hora_Entrega,
                'Pres_Tiempo_Limite': registro.Pres_Tiempo_Limite,
                'Pres_Observaciones_entrega': registro.Pres_Observaciones_entrega
            })

        return JsonResponse(Datos_Historial, safe=False)

class EliminarHistorial(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, pk):
        try:
            historial = Historial.objects.get(pk=pk)
        except Historial.DoesNotExist:
            return JsonResponse({"Error": "El Prestamo no existe"})
        historial.delete()
        return JsonResponse({"Mensaje":"Datos Eliminados"})


class BuscarHistorial(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        try:
            historial = Historial.objects.get(pk=pk)
        except Historial.DoesNotExist:
            return JsonResponse({"Error": "El Prestamo no existe"})
        
        datos_historial = {
            'Pres_Id': historial.Pres_Id,
            'Pres_Equipos_id': historial.Pres_Equipos_id,
            'Pres_Usuarios_Documento_id': historial.Pres_Usuarios_Documento_id,
            'Pres_Fec_Entrega': historial.Pres_Fec_Entrega,
            'Pres_Hora_Entrega': historial.Pres_Hora_Entrega,
            'Pres_Tiempo_Limite': historial.Pres_Tiempo_Limite,
            'Pres_Observaciones_entrega': historial.Pres_Observaciones_entrega
        }
        
        return JsonResponse(datos_historial)
    
def Portada(request):
    return render(request,"Principal.html")

def Informacion(request):
    return render(request,"Informacion.html")

def RecuperarContraseña(request):
    return render(request, "RecuperarContraseña.html")

def Nosotros(request):
    return render(request,"Nosotros.html")

def Login(request):
    return render(request,"Inicio.html")

def Formulario(request):
    return render(request,"Usuarios.html")

def historial(request):
    return render(request,"historial.html")



#cargar archivos excel

from django.shortcuts import render
from .forms import ExcelUploadForm
import pandas as pd
from .models import Usuarios  # Importa el modelo Usuarios

def subir_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            
            # Procesar el archivo Excel con pandas
            df = pd.read_excel(excel_file)
            
            # Iterar sobre las filas del DataFrame y guardar los datos en la base de datos
            for _, row in df.iterrows():
                usuario = Usuarios(
                    Usu_Documento=row['Documento'],
                    Usu_Nombre=row['Nombre'],
                    Usu_Apellido=row['Apellido'],
                    Usu_tipo=row['tipo'],
                    Usu_Celular=row['Celular'],
                    Usu_Correo=row['Correo'],
                    Usu_Ficha=row['Ficha']
                )
                usuario.save()
            
            # Redirigir a una página de éxito o realizar alguna otra acción
            return render(request, 'exito.html')
    else:
        form = ExcelUploadForm()
    
    return render(request, 'subir_excel.html', {'form': form})



# logout django

from django.contrib.auth import logout
from django.shortcuts import redirect


def user_logout(request):
    # Use the logout() function to log the user out
    logout(request)
    
    # Redirect to a success page, e.g., the homepage
    return redirect('Principal')  # Replace 'home' with the name of your desired view or URL
