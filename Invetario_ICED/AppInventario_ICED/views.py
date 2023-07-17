from typing import Any
from django import http
from django.shortcuts import render
from AppInventario_ICED.models import *
from django.views.generic import ListView,View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json  

# class listadoEquipos(ListView):
#     model=Equipos
#     template_name="index.html"

class listadoUsuarios(ListView):
    model=Usuarios
    template_name="indexuno.html"

class listadoPrestamos(ListView):
    model=Prestamos
    template_name="indexdos.html"

class listadoSanciones(ListView):
    model=Sanciones
    template_name="indextres.html"

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
        Equ_id = datos.get('Equ_id')
        Equi_tipo = datos.get('Equi_tipo')
        Equi_modelo = datos.get('Equi_modelo')
        Equi_color = datos.get('Equi_color')
        Equi_serial = datos.get('Equi_serial')
        Equi_estado = datos.get('Equi_estado')
        equi_especialidad = datos.get('equi_especialidad')
        print("datos",request.POST)
        Equipos.objects.create(Equ_id=Equ_id,Equi_tipo=Equi_tipo,Equi_modelo=Equi_modelo,Equi_color=Equi_color,Equi_serial=Equi_serial,Equi_estado=Equi_estado,equi_especialidad=equi_especialidad)
        return JsonResponse({"mensaje":"Datos Guardados"})

        # return render(request,"formulario.html",{'mensaje':'Datos Guardados'})
        
def Equipo(request):
    return render(request,"Equipos.html")

#EQUIPOS
class ActualizarEquipo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def put(self, request,pk):
            
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
    
#USUARIOS
class ListadoUsuarios(View):
    def get (self,request):
        Datos=Usuarios.objects.all().values()
        DatosUsuarios=list(Datos)
        return JsonResponse(DatosUsuarios,safe=False)
    

class InsertarUsuarios(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self,request):
        Usu_Documento = request .POST.get('Usu_Documento')
        Usu_Nombre = request .POST.get('Usu_Nombre')
        Usu_Apellido = request .POST.get('Usu_Apellido')
        Usu_tipo = request .POST.get('Usu_tipo')
        Usu_Celular = request .POST.get('Usu_Celular')
        Usu_Correo = request .POST.get('Usu_Correo')
        Usu_Ficha = request.POST.get('Usu_Ficha')
        print("datos",request.POST)
        Usuarios.objects.create(Usu_Documento=Usu_Documento,Usu_Nombre=Usu_Nombre,Usu_Apellido=Usu_Apellido,Usu_tipo=Usu_tipo,Usu_Celular=Usu_Celular,Usu_Correo=Usu_Correo,Usu_Ficha=Usu_Ficha)
        return render(request,"formularioUsuarios.html",{'mensaje':'Datos Guardados'})
    

def formularioUsuarios(request):
    return render(request,"formularioUsuarios.html")

class ActualizarUsuarios(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def put(self, request,pk):
            
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
#PRESTAMOS

class ListadoPrestamos(View):
    def get (self,request):
        Datos=Prestamos.objects.all().values()
        DatosPrestamos=list(Datos)
        return JsonResponse(DatosPrestamos,safe=False)
    

class InsertarPrestamo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        Pres_Id = request.POST.get('Pres_Id')
        Pres_Equipos_id = request.POST.get('Pres_Equipos_id')
        Pres_Usuarios_Documento = request.POST.get('Pres_Usuarios_Documento')
        Pres_Fec_Entrega = request.POST.get('Pres_Fec_Entrega')
        Pres_Fec_Devolucion = request.POST.get('Pres_Fec_Devolucion')
        Pres_Hora_Entrega = request.POST.get('Pres_Hora_Entrega')
        Pres_Hora_Devolucion = request.POST.get('Pres_Hora_Devolucion')
        Pres_Tiempo_Limite = request.POST.get('Pres_Tiempo_Limite')
        Pres_Observaciones_entrega = request.POST.get('Pres_Observaciones_entrega')
        Pres_Observaciones_recibido = request.POST.get('Pres_Observaciones_recibido')
        try:
            usuario = Usuarios.objects.get(Usu_Documento=Pres_Usuarios_Documento)
        except Usuarios.DoesNotExist:
            return HttpResponse("No se encontró ningún usuario con el número de documento proporcionado.")

        
        # Obtén la instancia de Usuarios basada en el documento
        usuario = Usuarios.objects.get(Usu_Documento =Pres_Usuarios_Documento)
        
        # Crea una instancia de Prestamos y asígnale los valores del formulario
        prestamo = Prestamos()
        prestamo.Pres_Id = Pres_Id
        prestamo.Pres_Equipos_id = Pres_Equipos_id
        prestamo.Pres_Usuarios_Documento = usuario
        prestamo.Pres_Fec_Entrega = Pres_Fec_Entrega
        prestamo.Pres_Fec_Devolucion = Pres_Fec_Devolucion
        prestamo.Pres_Hora_Entrega = Pres_Hora_Entrega
        prestamo.Pres_Hora_Devolucion = Pres_Hora_Devolucion
        prestamo.Pres_Tiempo_Limite = Pres_Tiempo_Limite
        prestamo.Pres_Observaciones_entrega = Pres_Observaciones_entrega
        prestamo.Pres_Observaciones_recibido = Pres_Observaciones_recibido
        prestamo.save()
        
        
        return render(request, "Prestamoss.html", {'mensaje': 'Datos Guardados'})
    

def Prestamoss(request):
    return render(request,"Prestamoss.html")


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

class ListarSanciones(View):
    def get (self,request):
        Datos=Sanciones.objects.all().values()
        DatosSanciones=list(Datos)
        return JsonResponse(DatosSanciones,safe=False)

class InsertarSanciones(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def post(self,request):
        San_Pres_Id = request .POST.get('San_Pres_Id')
        San_Fecha = request .POST.get('San_Fecha')
        San_Hora = request .POST.get('San_Hora')
        San_tiempo = request .POST.get('San_tiempo')
        San_Descripcion = request .POST.get('San_Descripcion')
        print("Datos",request.POST)
        Sanciones.objects.create(San_Pres_Id=San_Pres_Id,San_Fecha=San_Fecha,San_Hora=San_Hora,San_tiempo=San_tiempo,San_Descripcion=San_Descripcion)
        return render(request,"formularioSanciones.html",{'mensaje':'Datos Guardados'})
        
def formularioSanciones(request):
    return render(request,"formularioSanciones.html")


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
        ActuSancion.San_Pres_Id=data.get('San_Pres_Id')
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
            DeleteEquipo=Equipos.objects.get(pk=pk)
        except Equipos.DoesNotExist:
            return JsonResponse({"Error":"La Sancion no existe"})
        DeleteEquipo.delete()
        return JsonResponse({"Mensaje":"Sancion Eliminada"})
    