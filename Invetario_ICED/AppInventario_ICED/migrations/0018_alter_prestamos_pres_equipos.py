# Generated by Django 4.1.7 on 2023-10-14 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario_ICED', '0017_alter_prestamos_pres_equipos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='Pres_Equipos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppInventario_ICED.equipos', verbose_name='ID del equipo'),
        ),
    ]
