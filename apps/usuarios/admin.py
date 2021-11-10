from django.contrib import admin
from apps.usuarios.models import TipoDeDisponibilidad, Ilustracion, TipoDePrivilegios, EstadoDeAcceso, Perfil, EstadoDeSolicitud, Solicitud 

admin.site.register(TipoDeDisponibilidad)
admin.site.register(Ilustracion)
admin.site.register(TipoDePrivilegios)
admin.site.register(EstadoDeAcceso)
admin.site.register(Perfil)
admin.site.register(EstadoDeSolicitud)
admin.site.register(Solicitud)