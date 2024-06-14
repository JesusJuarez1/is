from django.test import TestCase
from django.urls import reverse
from Titulacion.views import *


class TestViewsTitulacion(TestCase):
    
    def test_info_titulacion_estatus(self):
        response = self.client.get('/titulacion/')
        self.assertEqual(200,response.status_code)

    def test_info_titulacion_template(self):
        response = self.client.get('/titulacion/')
        self.assertIn(b'Opciones',response.content)

    def test_url_info_titulacion(self):
        response = self.client.get(reverse('mostrar_titulacion'))
        self.assertEqual(200,response.status_code)
