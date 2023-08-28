from typing import Any
from django import http
from django.shortcuts import render
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

class ContarEquipos(View):
    def get(self, request):
        cantidad_equipos = Equipos.objects.count()  # Realiza una consulta para contar los equipos
        return JsonResponse({"cantidad_equipos": cantidad_equipos})



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
    
class InsertarPrestamo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"Error":"Error en el Documento"})
        datos=json.loads(request.body)
        Pres_Equipos_id = datos.get('Pres_Equipos_id')
        Pres_Usuarios_Documento_id = datos.get('Pres_Usuarios_Documento_id')
        Pres_Tiempo_Limite = datos.get('Pres_Tiempo_Limite')
        Pres_Observaciones_entrega = datos.get('Pres_Observaciones_entrega')
        print("datos",request.POST)
        Prestamos.objects.create(Pres_Equipos_id=Pres_Equipos_id,Pres_Usuarios_Documento_id=Pres_Usuarios_Documento_id,Pres_Tiempo_Limite=Pres_Tiempo_Limite,Pres_Observaciones_entrega=Pres_Observaciones_entrega)
        return JsonResponse({"mensaje":"Datos Guardados"})

        # return render(request,"formulario.html",{'mensaje':'Datos Guardados'})
        
def Prestamo(request):
    return render(request,"Prestamos.html")


class ActualizarPrestamo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def put(self, request,pk):
            
        try:
            registro=Prestamos.objects.get(pk=pk)
        except Prestamos.DoesNotExist:
            return JsonResponse({"Error":"El Prestamo no existe"})
        data=json.loads(request.body)
        registro.Pres_Id=data.get('Pres_Id')
        registro.Pres_Equipos_id=data.get('Pres_Equipos_id')
        registro.Pres_Usuarios_Documento=data.get('Pres_Usuarios_Documento')
        registro.Pres_Fec_Entrega=data.get('Pres_Fec_Entrega')
        registro.Pres_Fec_Devolucion=data.get('Pres_Fec_Devolucion')
        registro.Pres_Hora_Entrega=data.get('Pres_Hora_Entrega')
        registro.Pres_Hora_Devolucion=data.get('Pres_Hora_Devolucion')
        registro.Pres_Tiempo_Limite=data.get('Pres_Tiempo_Limite')
        registro.Pres_Observaciones_entrega=data.get('Pres_Observaciones_entrega')
        registro.Pres_Observaciones_recibido=data.get('Pres_Observaciones_recibido')
        registro.save()
        return JsonResponse({"Mensaje":"Datos Actualizados"})
    
class EliminarPrestamo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self,request,pk):
        try:
            registro=Prestamos.objects.get(pk=pk)
        except Prestamos.DoesNotExist:
            return JsonResponse({"Error":"El Prestamo no existe"})
        registro.delete()
        return JsonResponse({"Mensaje":"Datos Eliminados"})
    

 


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
    

def Portada(request):
    return render(request,"Principal.html")

def Login(request):
    return render(request,"Inicio.html")

def Formulario(request):
    return render(request,"Usuarios.html")