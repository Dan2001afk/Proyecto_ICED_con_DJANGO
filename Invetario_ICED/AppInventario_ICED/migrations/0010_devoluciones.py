# Generated by Django 4.1.7 on 2023-09-18 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario_ICED', '0009_alter_prestamos_pres_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devoluciones',
            fields=[
                ('Dev_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la devolucion')),
                ('Dev_Fec_Devolucion', models.DateField(auto_now=True)),
                ('Dev_Hora_Devolucion', models.TimeField(auto_now=True)),
                ('Dev_Observacion_Devolucion', models.TextField(max_length=255, verbose_name='Observacion de entrega del equipo')),
                ('Dev_Pres_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppInventario_ICED.prestamos', verbose_name='ID del prestamo')),
            ],
        ),
    ]
