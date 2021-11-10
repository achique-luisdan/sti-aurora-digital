from django.test import TestCase
from datetime import date
from ..forms import LoginForm
from ..models import EstadoDeAcceso
from ..models import Ilustracion
from ..models import TipoDePrivilegios
from ..models import TipoDeDisponibilidad
from ..models import Usuario


class LoginTest(TestCase):
    
    def setUp(self):
        disponibilidad = TipoDeDisponibilidad.objects.create(tipo='Disponible', \
        descripcion='Sin')
        estado = EstadoDeAcceso.objects.create(nombre='Activo')
        avatar = Ilustracion.objects.create(imagen='django.jpg.png')
        privilegios = TipoDePrivilegios.objects.create(especificador='E')

        self.usuario = Usuario.objects.create(nombre_de_usuario="aurora",\
         contrasea="1234", fecha_de_nacimiento=date(2018,12,1),\
         disponibilidad=disponibilidad, estado_de_acceso=estado,\
         imagen_de_perfil=avatar, privilegios=privilegios)
        self.form = None

    def test_usuario_con_clave_incorrecta(self): 
        data = {'nombre': 'aurora', 'clave': '1223'}
        self.form = LoginForm(data=data)
        
        self.assertFalse(self.form.is_valid())

    def test_usuario_con_nombre_incorrecto(self):
        data = {'nombre': 'Angel', 'clave': '1234'}
        self.form = LoginForm(data=data)
        
        self.assertFalse(self.form.is_valid())

    def test_usuario_con_datos_correctos(self):
        data = {'nombre': 'aurora', 'clave': '1234'}
        self.form = LoginForm(data=data)

        self.assertTrue(self.form.is_valid())                 
