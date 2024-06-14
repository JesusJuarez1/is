from django.test import TestCase
from usuario.models import CaseiUser, UserTipo, Documento
from django.contrib.auth import get_user_model

class TestModelUsuarioCasei(TestCase):
    def test_crear_usuario(self):
        CaseiUser.objects.create(nombre="Juan",
                                email="juan@juan.com",
                                telefono="4921234567",
                                username="Juan123",
                                password="juan123@")
        CaseiUser.objects.create(nombre="Pepe",
                                email="pepe@pepe.com",
                                telefono="4927654321",
                                username="Pepe123",
                                password="pepe123@")
        
        self.assertEqual(2,CaseiUser.objects.count())

    def test_tipo_usuario(self):
        usuario = CaseiUser.objects.create(nombre="Juan",
                                email="juan@juan.com",
                                telefono="4921234567",
                                username="Juan123",
                                password="juan123@")
        UserTipo.objects.create(tipoUser="Docente",caseiuser=usuario)

        self.assertEqual(1,UserTipo.objects.count())

    def test_crear_superusuario(self):
        User = get_user_model()
        superusuario = User.objects.create_superuser(email='admin@admin.com', username='admin', password='adminpassword')
        
        self.assertTrue(superusuario.is_superuser)

    def test_crear_superusuario_mail(self):
        User = get_user_model()
        superusuario = User.objects.create_superuser(email='admin@admin.com', username='admin', password='adminpassword')
        
        self.assertEqual(superusuario.email, 'admin@admin.com')

    def test_crear_superusuario_username(self):
        User = get_user_model()
        superusuario = User.objects.create_superuser(email='admin@admin.com', username='admin', password='adminpassword')
        
        self.assertEqual(superusuario.username, 'admin')

    def test_crear_superusuario_password(self):
        User = get_user_model()
        superusuario = User.objects.create_superuser(email='admin@admin.com', username='admin', password='adminpassword')
        
        self.assertTrue(superusuario.check_password('adminpassword'))

class TestModelDocumento(TestCase):
    def test_subir_documento(self):
        Documento.objects.create(nombre="DocumentoTest",archivo="documents/documento_test.txt")

        self.assertEqual(1,Documento.objects.count())

