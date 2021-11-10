from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


class LoginViewTest(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(username='engel', password='1234')
		self.user.first_name = 'Engel'
		self.user.last_name = 'Pinto'
		self.user.save()
		self.url = reverse('usuarios:buscar-usuario', kwargs={'nombre': self.user.username})

	def test_buscar_usuario_existente_da_200(self):
		response = self.client.get(self.url)

		self.assertEqual(200, response.status_code)

	def test_buscar_usuario_inexistente_da_404(self):
		username = 'Desconocido'

		response = self.client.get(reverse('usuarios:buscar-usuario', \
			kwargs={'nombre': username}))

		self.assertEqual(404, response.status_code)

	def test_el_nombre_completo_del_usuario_engel_es_Engel_Pinto(self):

		self.assertEqual('Engel Pinto', self.user.get_full_name())

	def test_el_password_del_usuario_engel_es_1234(self):

		self.assertEqual('1234', self.user.password)	
