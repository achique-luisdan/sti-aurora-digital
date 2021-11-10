from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.usuarios.models import Ilustracion, EstadoDeAcceso 

class NivelEducativo (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre	

class AreaDelSaber (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True,)
    ilustracion_primaria = models.ImageField(upload_to='../media/ilustraciones', 
                                             blank=True,
                                             max_length=255,
                                             default='../media/default/Iconopropio.jpg')
    ilustracion_secundaria = models.ImageField(upload_to='../media/ilustraciones',
                                               max_length=255,
                                               blank=True,
                                               default='../media/default/Iconopropio.jpg')
    estado = models.ForeignKey(EstadoDeAcceso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_de_registro = models.DateTimeField(default=timezone.now)
    fecha_de_modificacion = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class TipoDeUnidadCurricular (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class TipoDeDensidad (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class FormatoDeDuracion (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class UnidadCurricular (models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120, unique=True)
    nivel = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoDeUnidadCurricular, on_delete=models.CASCADE)
    creditos = models.IntegerField(default=0)
    densidad = models.ForeignKey(TipoDeDensidad, on_delete=models.CASCADE)
    duracion = models.IntegerField(default=0)
    formatodeduracion = models.ForeignKey(FormatoDeDuracion, on_delete=models.CASCADE)
    descripcion= models.TextField(blank=True, null=True)
    ilustracionprimaria = models.ForeignKey(Ilustracion, on_delete=models.CASCADE, related_name="ilustracionprimaria")
    ilustracionsecundaria = models.ForeignKey(Ilustracion, on_delete=models.CASCADE, related_name="ilustracionsecundaria")
    estrategiassugeridas = models.TextField(blank=True, null=True)
    estado = models.ForeignKey(EstadoDeAcceso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fechareg = models.DateTimeField(default=timezone.now)
    fechamodif = models.DateTimeField(blank=True, null=True)

class UnidadDidactica (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    unidadcurricular = models.ForeignKey(UnidadCurricular, on_delete=models.CASCADE)
    ilustracion = models.ForeignKey(Ilustracion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoDeAcceso, on_delete=models.CASCADE)
    fechareg = models.DateTimeField(default=timezone.now)
    fechamodif = models.DateTimeField(blank=True, null=True)

class Etiqueta (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    color =  models.CharField(max_length=120, unique=True)

class Articulo (models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=120, unique=True)
    desambiguacion = models.CharField(max_length=120, unique=True)
    unidaddidactica = models.ForeignKey(UnidadDidactica, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    ilustracion = models.ForeignKey(Ilustracion, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    visitas = models.IntegerField(default=0)
    estado = models.ForeignKey(EstadoDeAcceso, on_delete=models.CASCADE)
    fechareg = models.DateTimeField(default=timezone.now)
    fechamodif = models.DateTimeField(blank=True, null=True)

class Publicacion (models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
   
class TipoDeSeccion (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)

class Seccion (models.Model):
    titulo = models.CharField(max_length=120, unique=True)
    tipo = models.ForeignKey(TipoDeSeccion, on_delete=models.CASCADE)
    nivel = models.IntegerField(default=0)
    texto = models.TextField(blank=True, null=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoDeAcceso, on_delete=models.CASCADE)
    fechareg = models.DateTimeField(default=timezone.now)
    fechamodif = models.DateTimeField(blank=True, null=True)

class Libro (models.Model):
    titulo = models.CharField(max_length=120, unique=True)
    nombredeeditorial= models.CharField(max_length=50, blank=True)
    isbn = models.CharField(max_length=50, blank=True)
    nombredeubicacion = models.CharField(max_length=120, unique=True)
    serie = models.IntegerField(default=0)
    volumen = models.IntegerField(default=0)
    edicion = models.IntegerField(default=0)
    ao = models.IntegerField(default=0)

class Autor (models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)

class Escrito (models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

class TipoDeCita (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)

class Cita (models.Model):
    escrito = models.ForeignKey(Escrito, on_delete=models.CASCADE)
    tipodecita = models.ForeignKey(TipoDeCita, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoDeAcceso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fechaconsulta = models.DateTimeField(default=timezone.now)
    fechareg = models.DateTimeField(default=timezone.now)
    fechamodif = models.DateTimeField(blank=True, null=True)

class Imagen (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    elemento = models.ImageField(upload_to='imagenes', null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fechareg = models.DateTimeField(default=timezone.now)
    fechamodif = models.DateTimeField(blank=True, null=True)

class ElementoImagen (models.Model):		
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoDeAcceso, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)