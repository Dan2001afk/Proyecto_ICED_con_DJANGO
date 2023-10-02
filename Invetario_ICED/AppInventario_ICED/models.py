from django.conf import settings
from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Usuarios(models.Model):
    Usu_Documento=models.BigIntegerField(verbose_name="N° Documento",primary_key=True,)
    Usu_Nombre=models.TextField(max_length=40)
    Usu_Apellido=models.TextField(max_length=40)
    Usu_tipo=models.TextField(max_length=40)
    Usu_Celular=models.BigIntegerField(verbose_name="N° De Celular")
    Usu_Correo=models.EmailField(max_length=50,verbose_name="Correo Electronico")
    Usu_Ficha=models.TextField(max_length=40)
    
class User(AbstractUser):
    rol = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    Documento = models.OneToOneField(Usuarios, on_delete=models.CASCADE, primary_key=True)
    
class Equipos(models.Model):
    Equ_id=models.AutoField(verbose_name="ID del equipo", primary_key=True)
    Equi_tipo=models.TextField(max_length=50)
    Equi_modelo=models.TextField(max_length=50)
    Equi_color=models.TextField(max_length=50)
    Equi_serial=models.TextField(max_length=100,unique=True)
    Equi_estado=models.TextField(max_length=20)
    equi_especialidad=models.TextField(max_length=50)


class Prestamos(models.Model):
    Pres_Id = models.AutoField(verbose_name="ID del prestamo", primary_key=True)
    Pres_Equipos = models.ForeignKey(Equipos, verbose_name="ID del equipo", on_delete=models.CASCADE)
    Pres_Usuarios_Documento = models.ForeignKey(Usuarios, verbose_name="N° Documento del usuario", on_delete=models.CASCADE)
    Pres_Fec_Entrega = models.DateField(auto_now=True)
    Pres_Hora_Entrega = models.TimeField(auto_now=True, verbose_name="Hora de Entrega")
    Pres_Tiempo_Limite = models.BigIntegerField(verbose_name="Horas Que prestara el Equipo")
    Pres_Observaciones_entrega = models.TextField(max_length=255, verbose_name="Observaciones Salida Equipo")

class Historial(models.Model):
    Dev_id = models.AutoField(verbose_name="ID de la devolucion", primary_key=True)
    Dev_Usuarios_Documento = models.ForeignKey(Usuarios, verbose_name="N° Documento del usuario",on_delete=models.PROTECT)
    Dev_Pres_id = models.ForeignKey(Prestamos, verbose_name="ID del prestamo",on_delete=models.PROTECT)
    Dev_Fec_Devolucion = models.DateField(auto_now=True)
    Dev_Hora_Devolucion = models.TimeField(auto_now=True)
    Dev_Observacion_Devolucion = models.TextField(max_length=255, verbose_name="Observacion de entrega del equipo")
    

class Sanciones(models.Model):
    San_Id = models.AutoField(verbose_name="ID de la sancion", primary_key=True)
    San_Pres = models.ForeignKey(Prestamos, verbose_name="Prestamo relacionado", on_delete=models.CASCADE)
    San_Fecha = models.DateField(auto_now=True)
    San_Hora = models.TimeField(auto_now=True)
    San_tiempo = models.BigIntegerField(verbose_name="Horas de la Sancion")
    San_Descripcion = models.TextField(max_length=1000, verbose_name="Descripcion de la Sancion")

