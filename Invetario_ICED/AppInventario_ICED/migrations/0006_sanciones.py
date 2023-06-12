# Generated by Django 4.1.7 on 2023-05-23 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario_ICED', '0005_prestamos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sanciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('San_Fecha_Hora', models.TimeField(auto_now=True)),
                ('San_tiempo', models.BigIntegerField(verbose_name='Horas de la Sancion')),
                ('San_Descripcion', models.TextField(max_length=1000, verbose_name='Descripcion de la Sancion')),
                ('San_Pres_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppInventario_ICED.prestamos', verbose_name='ID de la sancion')),
            ],
        ),
    ]
