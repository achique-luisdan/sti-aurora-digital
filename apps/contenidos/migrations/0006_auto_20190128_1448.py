# Generated by Django 2.1.2 on 2019-01-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenidos', '0005_auto_20190128_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areadelsaber',
            name='ilustracion_primaria',
            field=models.ImageField(blank=True, default='../media/default/Iconopropio.jpg', max_length=255, upload_to='../media/ilustraciones'),
        ),
        migrations.AlterField(
            model_name='areadelsaber',
            name='ilustracion_secundaria',
            field=models.ImageField(blank=True, default='../media/default/Iconopropio.jpg', max_length=255, upload_to='../media/ilustraciones'),
        ),
    ]
