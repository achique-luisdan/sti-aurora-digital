# Generated by Django 2.0.10 on 2019-01-23 03:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaDelSaber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fechareg', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechamodif', models.DateTimeField(blank=True, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.EstadoDeAcceso')),
                ('ilustracionprimaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contenidos_areadelsaber_relateda', to='usuarios.Ilustracion')),
                ('ilustracionsecundaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contenidos_areadelsaber_relatedb', to='usuarios.Ilustracion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('titulo', models.CharField(max_length=120, unique=True)),
                ('desambiguacion', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('visitas', models.IntegerField(default=0)),
                ('fechareg', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechamodif', models.DateTimeField(blank=True, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.EstadoDeAcceso')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaconsulta', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechareg', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechamodif', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElementoImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.EstadoDeAcceso')),
            ],
        ),
        migrations.CreateModel(
            name='Escrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('color', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormatoDeDuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('elemento', models.ImageField(null=True, upload_to='imagenes')),
                ('fechareg', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechamodif', models.DateTimeField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120, unique=True)),
                ('nombredeeditorial', models.CharField(blank=True, max_length=50)),
                ('isbn', models.CharField(blank=True, max_length=50)),
                ('nombredeubicacion', models.CharField(max_length=120, unique=True)),
                ('serie', models.IntegerField(default=0)),
                ('volumen', models.IntegerField(default=0)),
                ('edicion', models.IntegerField(default=0)),
                ('ao', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NivelEducativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Articulo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120, unique=True)),
                ('nivel', models.IntegerField(default=0)),
                ('texto', models.TextField(blank=True, null=True)),
                ('fechareg', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechamodif', models.DateTimeField(blank=True, null=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Articulo')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.EstadoDeAcceso')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeCita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeDensidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeSeccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeUnidadCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('creditos', models.IntegerField(default=0)),
                ('duracion', models.IntegerField(default=0)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estrategiassugeridas', models.TextField(blank=True, null=True)),
                ('fechareg', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechamodif', models.DateTimeField(blank=True, null=True)),
                ('densidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.TipoDeDensidad')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.EstadoDeAcceso')),
                ('formatodeduracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.FormatoDeDuracion')),
                ('ilustracionprimaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ilustracionprimaria', to='usuarios.Ilustracion')),
                ('ilustracionsecundaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ilustracionsecundaria', to='usuarios.Ilustracion')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.NivelEducativo')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.TipoDeUnidadCurricular')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadDidactica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fechareg', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechamodif', models.DateTimeField(blank=True, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.EstadoDeAcceso')),
                ('ilustracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Ilustracion')),
                ('unidadcurricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.UnidadCurricular')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='seccion',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.TipoDeSeccion'),
        ),
        migrations.AddField(
            model_name='escrito',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Libro'),
        ),
        migrations.AddField(
            model_name='elementoimagen',
            name='imagen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Imagen'),
        ),
        migrations.AddField(
            model_name='elementoimagen',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Seccion'),
        ),
        migrations.AddField(
            model_name='cita',
            name='escrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Escrito'),
        ),
        migrations.AddField(
            model_name='cita',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.EstadoDeAcceso'),
        ),
        migrations.AddField(
            model_name='cita',
            name='tipodecita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.TipoDeCita'),
        ),
        migrations.AddField(
            model_name='cita',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='etiqueta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.Etiqueta'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='ilustracion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Ilustracion'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='unidaddidactica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenidos.UnidadDidactica'),
        ),
    ]
