from typing import Any
from django import http
from django.shortcuts import render
from AppInventario_ICED.models import *
from django.views.generic import ListView,View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json  

class listadoEquipos(ListView):
    model=Equipos
    template_name="index.html"

class listadoUsuarios(ListView):
    model=Usuarios
    template_name="indexuno.html"

class listadoPrestamos(ListView):
    model=Prestamos
    template_name="indexdos.html"

class listadoSanciones(ListView):
    model=Sanciones
    template_name="indextres.html"

class ListadoEquipos(View):
    def get (self,request):
        Datos=Equipos.objects.all().values()
        DatosEquipos=list(Datos)
        return JsonResponse(DatosEquipos,safe=False)

class InsertarEquipos(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self,request):
        Equ_id = request .POST.get('Equ_id')
        Equi_tipo = request .POST.get('Equi_tipo')
        Equi_modelo = request .POST.get('Equi_modelo')
        Equi_color = request .POST.get('Equi_color')
        Equi_serial = request .POST.get('Equi_serial')
        Equi_estado = request .POST.get('Equi_estado')
        equi_especialidad = request.POST.get('equi_especialidad')
        print("datos",request.POST)
        Equipos.objects.create(Equ_id=Equ_id,Equi_tipo=Equi_tipo,Equi_modelo=Equi_modelo,Equi_color=Equi_color,Equi_serial=Equi_serial,Equi_estado=Equi_estado,equi_especialidad=equi_especialidad)
        return render(request,"formulario.html",{'mensaje':'Datos Guardados'})
        

