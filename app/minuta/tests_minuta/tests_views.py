import datetime
from django.test import TestCase
from django.urls import reverse
from minuta.views import *
from minuta.models import MinutasCasei

class TestViewsMinutas(TestCase):
    def setUp(self):
        self.minuta = MinutasCasei.objects.create(
            titulominuta='TituloM1',
            fechaminuta=datetime.date(2024, 1, 1),
            minuta='ContentMinuta',
            acuerdos='AcuerdosMinuta'
        )

    def test_lista_minutas_estatus(self):
        response = self.client.get('/minutas/')
        self.assertEqual(200,response.status_code)

    def test_lista_minutas_template(self):
        response = self.client.get('/minutas/')
        self.assertIn(b'Minutas', response.content)

    def test_url_lista_minutas(self):
        response = self.client.get(reverse('consulta_minutas'))
        self.assertEqual(200,response.status_code)

    def test_agregar_minuta_estatus(self):
        response = self.client.get('/minutas/agregar/')
        self.assertEqual(200,response.status_code)

    def test_agregar_minuta_template(self):
        response = self.client.get('/minutas/agregar/')
        self.assertIn(b'Agregar Minuta', response.content)

    def test_agregar_minuta_url(self):
        response = self.client.get(reverse('agregar_minuta'))
        self.assertEqual(200,response.status_code)

    def test_agregar_minuta(self):
        datos_minuta = {
            'titulominuta':'TituloM1',
            'fechaminuta':'2024-01-01',
            'minuta':'ContentMinuta',
            'acuerdos':'AcuerdosMinuta',
        }
        response = self.client.post('/minutas/agregar/',datos_minuta)
        self.assertEqual(MinutasCasei.objects.count(),2)

    def test_eliminar_minuta_estatus(self):
        minuta = MinutasCasei.objects.get(titulominuta='TituloM1')

        response = self.client.post(f'/minutas/eliminar/{minuta.id}')

        self.assertEqual(302,response.status_code)

    def test_eliminar_minuta_object(self):
        minuta = MinutasCasei.objects.get(titulominuta='TituloM1')

        response = self.client.post(f'/minutas/eliminar/{minuta.id}')
        self.assertEqual(MinutasCasei.objects.count(), 0)

    def test_editar_minuta_estatus(self):
        id_minuta = self.minuta.id

        datos_minuta_nueva = {
            'titulominuta': 'TituloModificado',
            'fechaminuta': '2024-02-01',
            'minuta': 'ContentMinuta actualizada',
            'acuerdos': 'AcuerdosMinuta actualizados',
        }

        response = self.client.post(f'/minutas/editar/{id_minuta}',datos_minuta_nueva)

        self.assertEqual(302,response.status_code)

    def test_editar_minuta_datos_nuevos_titulo_minuta(self):
        id_minuta = self.minuta.id

        datos_minuta_nueva = {
            'titulominuta': 'TituloModificado',
            'fechaminuta': '2024-02-01',
            'minuta': 'ContentMinuta actualizada',
            'acuerdos': 'AcuerdosMinuta actualizados',
        }

        response = self.client.post(f'/minutas/editar/{id_minuta}',datos_minuta_nueva)

        minuta_actualizada = MinutasCasei.objects.get(id=id_minuta)
        self.assertEqual(minuta_actualizada.titulominuta, 'TituloModificado')

    def test_editar_minuta_datos_nuevos_fecha(self):
        id_minuta = self.minuta.id

        datos_minuta_nueva = {
            'titulominuta': 'TituloModificado',
            'fechaminuta': '2024-02-01',
            'minuta': 'ContentMinuta actualizada',
            'acuerdos': 'AcuerdosMinuta actualizados',
        }

        response = self.client.post(f'/minutas/editar/{id_minuta}',datos_minuta_nueva)

        minuta_actualizada = MinutasCasei.objects.get(id=id_minuta)

        self.assertEqual(minuta_actualizada.fechaminuta.strftime('%Y-%m-%d'), '2024-02-01')

    def test_editar_minuta_datos_nuevos_minuta(self):
        id_minuta = self.minuta.id

        datos_minuta_nueva = {
            'titulominuta': 'TituloModificado',
            'fechaminuta': '2024-02-01',
            'minuta': 'ContentMinuta actualizada',
            'acuerdos': 'AcuerdosMinuta actualizados',
        }

        response = self.client.post(f'/minutas/editar/{id_minuta}',datos_minuta_nueva)

        minuta_actualizada = MinutasCasei.objects.get(id=id_minuta)

        self.assertEqual(minuta_actualizada.minuta, 'ContentMinuta actualizada')

    def test_editar_minuta_datos_nuevos_acuerdos(self):
        id_minuta = self.minuta.id

        datos_minuta_nueva = {
            'titulominuta': 'TituloModificado',
            'fechaminuta': '2024-02-01',
            'minuta': 'ContentMinuta actualizada',
            'acuerdos': 'AcuerdosMinuta actualizados',
        }

        response = self.client.post(f'/minutas/editar/{id_minuta}',datos_minuta_nueva)

        minuta_actualizada = MinutasCasei.objects.get(id=id_minuta)

        self.assertEqual(minuta_actualizada.acuerdos, 'AcuerdosMinuta actualizados')
    
    def test_generar_pdf_minuta_estatus(self):
        url = reverse('generar_pdf_minuta', args=[self.minuta.id])
        response = self.client.get(url)
    
        self.assertEqual(response.status_code, 200)

    def test_generar_pdf_minuta_contenido(self):
        url = reverse('generar_pdf_minuta', args=[self.minuta.id])
        response = self.client.get(url)

        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_generar_pdf_minuta_nombre_archivo(self):
        url = reverse('generar_pdf_minuta', args=[self.minuta.id])
        response = self.client.get(url)

        nombre_archivo = f"{self.minuta.titulominuta}.pdf"
        self.assertIn(f'inline; filename="{nombre_archivo}"', response['Content-Disposition'])

    def test_generar_pdf_minuta_contenido_no_vacio(self):
        url = reverse('generar_pdf_minuta', args=[self.minuta.id])
        response = self.client.get(url)

        self.assertTrue(response.content)


