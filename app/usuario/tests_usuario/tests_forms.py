from django.test import TestCase
from usuario.forms import RegistrarUsuarioForm, DocumentoForm, LoginForm, NotificacionForm, SolicitudCambioActividadesForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from usuario.models import UserTipo, CaseiUser

User = get_user_model()

class TestRegistrarUsuarioForm(TestCase):
    def setUp(self):
        self.datos_usuario = {
            'nombre':"Juan",
            'email':"juan@juan.com",
            'telefono':"4921234567",
            'username':"Juan123",
            'password':"juan123@"
        }

    def test_registrar_usuario_form_valido(self):
        self.datos_usuario['tipo_user'] = 'estudiante'
        form = RegistrarUsuarioForm(self.datos_usuario)
        self.assertTrue(form.is_valid())

    def test_usuario_no_nombre(self):
        self.datos_usuario['nombre'] = ''
        form = RegistrarUsuarioForm(self.datos_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_no_email(self):
        self.datos_usuario['email'] = ''
        form = RegistrarUsuarioForm(self.datos_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_email_invalido(self):
        self.datos_usuario['email'] = 'juan'
        form = RegistrarUsuarioForm(self.datos_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_no_telefono(self):
        self.datos_usuario['telefono'] = ''
        form = RegistrarUsuarioForm(self.datos_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_telefono_invalido(self):
        self.datos_usuario['telefono'] = '1234'
        form = RegistrarUsuarioForm(self.datos_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_no_username(self):
        self.datos_usuario['username'] = ''
        form = RegistrarUsuarioForm(self.datos_usuario)
        self.assertFalse(form.is_valid())

    def test_usuario_no_password(self):
        self.datos_usuario['password'] = ''
        form = RegistrarUsuarioForm(self.datos_usuario)
        self.assertFalse(form.is_valid())

class TestDocumentoForm(TestCase):
    def setUp(self):
        self.archivo = SimpleUploadedFile('documento_test.txt', b'Contenido del archivo')
        self.datos = {
            'nombre': "Doc1",
            'archivo': self.archivo
        }

    def test_documento_form_valido(self):
        form = DocumentoForm(data=self.datos, files={'archivo': self.archivo})
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_documento_no_nombre(self):
        self.datos['nombre'] = ''
        form = DocumentoForm(data=self.datos, files={'archivo': self.archivo})
        self.assertFalse(form.is_valid())

class TestLoginForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@test.com', nombre='Test User', telefono='+1234567890')

    def test_login_form_valido(self):
        datos = {'username': 'testuser', 'password': 'testpassword'}

        form = LoginForm(data=datos)

        self.assertTrue(form.is_valid())

    def test_login_form_no_valido_usuario(self):
        datos = {'username': 'usuario_invalido', 'password': 'testpassword'}
        form = LoginForm(data=datos)

        self.assertFalse(form.is_valid())

    def test_login_form_no_valido_mensaje(self):
        datos = {'username': 'usuario_invalido', 'password': 'testpassword'}
        form = LoginForm(data=datos)

        self.assertIn('Usuario o contraseña incorrectos', form.errors['__all__'])

    def test_login_form_invalido_password(self):
        datos = {'username': 'testuser', 'password': 'test123'}
        form = LoginForm(data=datos)
        
        self.assertFalse(form.is_valid())

    def test_login_form_invalido_mensaje_password(self):
        datos = {'username': 'testuser', 'password': 'test123'}
        form = LoginForm(data=datos)

        self.assertIn('Usuario o contraseña incorrectos', form.errors['__all__'])

    def test_login_form_no_username(self):
        datos = {'password': 'testpassword'}
        form = LoginForm(data=datos)
        
        self.assertFalse(form.is_valid())

    def test_login_form_no_username_mensaje(self):
        datos = {'password': 'testpassword'}
        form = LoginForm(data=datos)

        self.assertIn('This field is required.', form.errors['username'])

    def test_login_form_no_password(self):
        datos = {'username': 'testuser'}
        form = LoginForm(data=datos)
        
        self.assertFalse(form.is_valid())

    def test_login_form_no_password_mensaje(self):
        datos = {'username': 'testuser'}
        form = LoginForm(data=datos)
        
        self.assertIn('This field is required.', form.errors['password'])

class TestNotificacionForm(TestCase):
    def setUp(self):
        self.datos_notificacion = {
            'asunto': 'Reunión',
            'mensaje': 'Habra una reunion el lunes a las 10',
            'tipo_usuario': 'tutor'
        }

    def test_notificacion_form_valido(self):
        form = NotificacionForm(self.datos_notificacion)

        self.assertTrue(form.is_valid())

    def test_notificacion_no_asunto(self):
        self.datos_notificacion['asunto'] = ''
        form = NotificacionForm(self.datos_notificacion)
        self.assertFalse(form.is_valid())

    def test_notificacion_no_mensaje(self):
        self.datos_notificacion['mensaje'] = ''
        form = NotificacionForm(self.datos_notificacion)
        self.assertFalse(form.is_valid())

    def test_notificacion_no_tipo_usuario(self):
        self.datos_notificacion['tipo_usuario'] = ''
        form = NotificacionForm(self.datos_notificacion)
        self.assertFalse(form.is_valid())

class TestCambioActividades(TestCase):
    def setUp(self):
        self.estudiante = CaseiUser.objects.create_user(username='testuser', password='testpassword', email='test@test.com', nombre='Test User', telefono='+1234567890')

        self.tipo_estudiante = UserTipo.objects.create(tipoUser='estudiante', caseiuser=self.estudiante)

    def test_cambio_actividades_form_valid(self):
        datos_cambio = {
            'asunto': 'Cambio actividad',
            'mensaje': 'Solicito cambio de actividad',
            'estudiante': self.estudiante.id
        }

        form = SolicitudCambioActividadesForm(data=datos_cambio)

        self.assertTrue(form.is_valid())

    def test_cambio_actividades_no_asunto(self):
        datos_cambio = {
            'asunto': '',
            'mensaje': 'Solicito cambio de actividad',
            'estudiante': self.estudiante.id
        }
        form = SolicitudCambioActividadesForm(data=datos_cambio)

        self.assertFalse(form.is_valid())

    def test_cambio_actividades_no_mensaje(self):
        datos_cambio = {
            'asunto': 'Cambio actividad',
            'mensaje': '',
            'estudiante': self.estudiante.id
        }
        form = SolicitudCambioActividadesForm(data=datos_cambio)

        self.assertFalse(form.is_valid())

    def test_cambio_actividades_no_estudiante(self):
        datos_cambio = {
            'asunto': 'Cambio actividad',
            'mensaje': 'Solicito cambio de actividad',
        }
        form = SolicitudCambioActividadesForm(data=datos_cambio)

        self.assertFalse(form.is_valid())