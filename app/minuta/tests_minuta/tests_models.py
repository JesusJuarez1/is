from django.test import TestCase
from minuta.models import MinutasCasei, UserMinuta
from usuario.models import CaseiUser

class TestModelMinutaCasei(TestCase):
    def test_crear_minuta(self):
        MinutasCasei.objects.create(titulominuta="TM",
                                             fechaminuta="2024-01-01",
                                             minuta="TXTM",
                                             acuerdos="AM")
        MinutasCasei.objects.create(titulominuta="TM2",
                                             fechaminuta="2024-01-02",
                                             minuta="TXTM2",
                                             acuerdos="AM2")

        self.assertEqual(2,MinutasCasei.objects.count())

    def test_crear_user_minuta(self):
        usuario = CaseiUser.objects.create(nombre="Juan",
                                           email="juan@juan.com",
                                           telefono="4921234567",
                                           username="Juan123",
                                           password="juan123@")
        
        minuta = MinutasCasei.objects.create(titulominuta="TM",
                                             fechaminuta="2024-01-01",
                                             minuta="TXTM",
                                             acuerdos="AM")
        
        UserMinuta.objects.create(caseiuser=usuario, minuta=minuta)

        self.assertEqual(1,UserMinuta.objects.count())



