# Generated by Django 4.1.7 on 2023-06-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario_ICED', '0007_remove_sanciones_id_alter_sanciones_san_pres_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sanciones',
            old_name='San_Fecha_Hora',
            new_name='San_Hora',
        ),
        migrations.AddField(
            model_name='sanciones',
            name='San_Fecha',
            field=models.DateField(auto_now=True),
        ),
    ]
