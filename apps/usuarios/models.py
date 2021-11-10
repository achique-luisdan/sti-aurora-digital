from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group

class Ilustracion(models.Model):
    imagen = models.ImageField(upload_to='ilustraciones', null=True)

class TipoDePrivilegios (models.Model):
    especificador = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.especificador

class TipoDeDisponibilidad (models.Model):
    tipo = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.tipo

class EstadoDeAcceso (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class Perfil (models.Model):
    GENDER_CHOICES = (('M', 'Masculino',), ('F', 'Femenino',))
    sexo = models.CharField('Sexo', max_length=1, choices=GENDER_CHOICES,
                            blank=True)
    fecha_de_nacimiento = models.DateField(blank=True)
    imagen_de_perfil = models.ImageField(upload_to='../media/perfiles', 
                                         blank=True,
                                         max_length=255, 
                                         default='../media/default/perfil.png')
    disponibilidad = models.ForeignKey(TipoDeDisponibilidad, 
                                       on_delete=models.CASCADE)
    estado_de_acceso = models.ForeignKey(EstadoDeAcceso, 
                                         on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)                                     
    def __str__(self):
        return format("Perfil de "+self.usuario.username)

class EstadoDeSolicitud (models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class Solicitud (models.Model):
    aspiraciones = models.ForeignKey(Group,
                                      on_delete=models.CASCADE, blank=False)
    comentario = models.TextField(blank=True, null=True)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_de_envio= models.DateTimeField(default=timezone.now, blank=True,
                                         null=True)
    estado = models.ForeignKey(EstadoDeSolicitud, on_delete=models.CASCADE)
    def __str__(self):
        return 'Solicitud de '+self.aspiraciones.name +' ('+self.solicitante.username +') '+self.fecha_de_envio.strftime('%m/%d/%Y-%H:%M:%S')
    def set_fecha_de_envio(self):
        self.fecha_de_envio = timezone.now()