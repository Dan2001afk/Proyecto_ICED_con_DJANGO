# Generated by Django 4.1.7 on 2023-10-14 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario_ICED', '0013_historial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='Pres_Tiempo_Limite',
            field=models.TextField(verbose_name='Horas Que prestara el Equipo'),
        ),
    ]
