# Generated by Django 2.1.2 on 2019-01-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenidos', '0002_auto_20190125_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areadelsaber',
            name='ilustracion_primaria',
            field=models.ImageField(default='../../sti_aurora_digital/media/default/Iconopropio.png', max_length=255, upload_to='../media/ilustraciones'),
        ),
        migrations.AlterField(
            model_name='areadelsaber',
            name='ilustracion_secundaria',
            field=models.ImageField(default='../../sti_aurora_digital/media/default/Iconopropio.png', max_length=255, upload_to='../media/ilustraciones'),
        ),
    ]
