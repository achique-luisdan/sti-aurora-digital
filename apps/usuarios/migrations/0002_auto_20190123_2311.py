# Generated by Django 2.0.10 on 2019-01-23 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='fechadeenvio',
            new_name='fecha_de_envio',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='correoelectronico',
            new_name='correo_electronico',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='estadodeacceso',
            new_name='estado_de_acceso',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='fechadeacceso',
            new_name='fecha_de_acceso',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='fechadenacimiento',
            new_name='fecha_de_nacimiento',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='fechadereg',
            new_name='fecha_de_registro',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='imagendeperfil',
            new_name='imagen_de_perfil',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='niveldeprivilegios',
            new_name='nivel_de_privilegios',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombredeusuario',
            new_name='nombre_de_usuario',
        ),
    ]
