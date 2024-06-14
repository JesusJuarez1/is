from django.test import Client, TestCase
from django.urls import reverse
from usuario.views import *
from usuario.models import CaseiUser
from django.contrib.messages import get_messages
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class TestViewsUsuarios(TestCase):
    def setUp(self):
        self.usuario = CaseiUser.objects.create_user(nombre="Juan",
                                email="juan@juan.com",
                                telefono="4921234567",
                                username="Juan123",
                                password="juan123@")
        
        self.tipo = UserTipo.objects.create(
            tipoUser="coordinador",
            caseiuser=self.usuario
        )
        self.client = Client()


    def login(self):
        self.client.login(username="Juan123", password="juan123@")
    
    def test_lista_usuarios_estatus(self):
        self.login()
        response = self.client.get('/usuario/')
        self.assertEqual(200,response.status_code)

    def test_lista_usuarios_template(self):
        self.login()
        response = self.client.get('/usuario/')
        self.assertIn(b'Lista de usuarios',response.content)

    def test_lista_usuarios_url(self):
        self.login()
        response = self.client.get(reverse('index'))
        self.assertEqual(200,response.status_code)

    def test_agregar_usuario_estatus(self):
        response = self.client.get('/usuario/registro/')
        self.assertEqual(200,response.status_code)

    def test_agrega_usuario_template(self):
        response = self.client.get('/usuario/registro/')
        self.assertIn(b'Nombre', response.content)

    def test_agrega_usuario_url(self):
        response = self.client.get(reverse('registrar'))
        self.assertEqual(200,response.status_code)

    def test_agregar_usuario(self):
        datos_usuario = {
            'nombre':"Juan",
            'email':"juan@juan.com",
            'telefono':"4921234567",
            'username':"Juan123",
            'password':"juan123@"
        }
        response = self.client.post('/usuario/registro/', datos_usuario)
        self.assertEqual(CaseiUser.objects.count(),1)

    def test_eliminar_usuario_estatus(self):
        usuario = CaseiUser.objects.get(nombre="Juan")

        response = self.client.post(f'/usuario/eliminar/{usuario.id}')

        self.assertEqual(302,response.status_code)

    def test_eliminar_usuario_object(self):
        self.login()
        usuario = CaseiUser.objects.get(nombre="Juan")

        self.client.post(f'/usuario/eliminar/{usuario.id}')
        self.assertEqual(CaseiUser.objects.count(), 0)

    def test_obtener_usuario_estatus(self):
        self.login()
        usuario = CaseiUser.objects.get(nombre='Juan')

        response = self.client.post(f'/usuario/info/{usuario.id}')
        self.assertEqual(200,response.status_code)

    def test_editar_usuario_estatus(self):
        self.login()
        id_usuario = self.usuario.id

        datos_usuario_nuevo = {
            'nombre': 'Juan',
            'email': 'juan@juan.com',
            'telefono': '4921234567',
            'username': 'Juan456',
            'password': 'juan123@',
        }

        response = self.client.post(f'/usuario/editar/{id_usuario}',datos_usuario_nuevo)

        self.assertEqual(200,response.status_code)

    def test_editar_usuario_datos_nuevos_nombre(self):
        id_usuario = self.usuario.id

        datos_usuario_nuevo = {
            'nombre': 'Juan',
            'email': 'juan@juan.com',
            'telefono': '4921234567',
            'username': 'Juan456',
            'password': 'juan123@',
        }

        response = self.client.post(f'/usuario/editar/{id_usuario}',datos_usuario_nuevo)

        usuario_actualizado = CaseiUser.objects.get(id=id_usuario)
        self.assertEqual(usuario_actualizado.nombre, 'Juan')

    def test_editar_usuario_datos_nuevos_email(self):
        id_usuario = self.usuario.id

        datos_usuario_nuevo = {
            'nombre': 'Juan',
            'email': 'juan@juan.com',
            'telefono': '4921234567',
            'username': 'Juan456',
            'password': 'juan123@',
        }

        response = self.client.post(f'/usuario/editar/{id_usuario}',datos_usuario_nuevo)

        usuario_actualizado = CaseiUser.objects.get(id=id_usuario)
        self.assertEqual(usuario_actualizado.email, 'juan@juan.com')

    def test_editar_usuario_datos_nuevos_telefono(self):
        id_usuario = self.usuario.id

        datos_usuario_nuevo = {
            'nombre': 'Juan',
            'email': 'juan@juan.com',
            'telefono': '4921234567',
            'username': 'Juan456',
            'password': 'juan123@',
        }

        response = self.client.post(f'/usuario/editar/{id_usuario}',datos_usuario_nuevo)

        usuario_actualizado = CaseiUser.objects.get(id=id_usuario)
        self.assertEqual(usuario_actualizado.telefono, '4921234567')

    def test_editar_usuario_datos_nuevos_username(self):
        id_usuario = self.usuario.id

        datos_usuario_nuevo = {
            'nombre': 'Juan',
            'email': 'juan@juan.com',
            'telefono': '4921234567',
            'username': 'Juan456',
            'password': 'juan123@',
        }

        response = self.client.post(f'/usuario/editar/{id_usuario}',datos_usuario_nuevo)

        usuario_actualizado = CaseiUser.objects.get(id=id_usuario)
        self.assertEqual(usuario_actualizado.username, 'Juan123')

    def test_editar_usuario_datos_nuevos_password(self):
        id_usuario = self.usuario.id

        datos_usuario_nuevo = {
            'nombre': 'Juan',
            'email': 'juan@juan.com',
            'telefono': '4921234567',
            'username': 'Juan456',
            'password': 'juan123@',
        }

        response = self.client.post(f'/usuario/editar/{id_usuario}',datos_usuario_nuevo)

        usuario_actualizado = CaseiUser.objects.get(id=id_usuario)
        self.assertTrue(check_password('juan123@', usuario_actualizado.password))

    def test_eviar_correo_usuario_estatus(self):
        self.login()
        response = self.client.get('/usuario/enviar_correo/')

        self.assertEqual(200,response.status_code)

    def test_enviar_correo_usuario_template(self):
        self.login()
        response = self.client.get('/usuario/enviar_correo/')

        self.assertIn(b'Asunto:',response.content)

    @patch('usuario.functions.enviar_correo')
    def test_enviar_correo_usuario_mensaje(self, mock_enviar_correo):
        data = {'asunto': 'Test', 'mensaje': 'Test message', 'tipo_usuario': 'Estudiante'}

        response = self.client.post('/enviar_correo/', data)
        
        mock_enviar_correo.assert_not_called()

        messages = list(get_messages(response.wsgi_request))
        # El assert es False para verificar que si no se envia el corroeo no se manda el mensaje de exito
        self.assertFalse(any(message.message == 'Se ha enviado notificación correctamente.' for message in messages))

    def test_perfil_usuario_estatus(self):
        self.login()
        url = reverse('perfil_usuario', kwargs={'pk': self.usuario.pk})
        
        response = self.client.get(url)
    
        self.assertEqual(response.status_code, 200)

    def test_perfil_usuario_template(self):
        self.login()
        url = reverse('perfil_usuario', kwargs={'pk': self.usuario.pk})
        
        response = self.client.get(url)
    
        self.assertIn(b'Perfil de', response.content)

    def test_login_estatus(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        self.client.post(reverse('login'), {'username': self.usuario.username, 'password': self.usuario.password})
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_subir_documento_estatus(self):
        archivo = open('usuario/tests_usuario/prueba.txt', 'r')
        data = {'nombre': 'Documento de prueba', 'archivo': archivo}
        response = self.client.post(reverse('subir_documento'), data)
        self.assertEqual(response.status_code, 302)

    def test_subir_documento(self):
        archivo = open('usuario/tests_usuario/prueba.txt', 'rb')
        data = {'nombre': 'Documento de prueba', 'archivo': archivo}
        response = self.client.post(reverse('subir_documento'), data, format='multipart')
        self.assertTrue(1,Documento.objects.count())

    def test_eliminar_documento(self):
        self.login()
        documento = Documento.objects.create(nombre='Documento de prueba', archivo=SimpleUploadedFile('prueba.txt', b'Contenido de prueba'))

        response = self.client.post(reverse('eliminar_documento', kwargs={'pk': documento.pk}))

        self.assertFalse(Documento.objects.filter(pk=documento.pk).exists())

    def test_lista_documentos_estatus(self):
        self.login()
        response = self.client.get(reverse('lista_documentos'))

        self.assertEqual(200,response.status_code)

    def test_lista_documentos_template(self):
        self.login()
        response = self.client.get(reverse('lista_documentos'))

        self.assertIn(b'No hay documentos para mostrar',response.content)

    def test_confirmacion(self): # Prueba Temporal -> Falta implementar funcionalidad
        self.login()
        response = self.client.get(reverse('confirmacion'))

        self.assertEqual(200,response.status_code)

    def test_evaluaciones(self): # Prueba Temporal -> Falta implementar funcionalidad
        response = self.client.get(reverse('evaluaciones'))

        self.assertEqual(200,response.status_code)

    def test_historial_alumno(self): # Prueba Temporal -> Falta implementar funcionalidad
        response = self.client.get(reverse('historial_alumno'))

        self.assertEqual(200,response.status_code)
    
    def test_actividades(self): # Prueba Temporal -> Falta implementar funcionalidad
        response = self.client.get(reverse('actividades'))

        self.assertEqual(200,response.status_code)