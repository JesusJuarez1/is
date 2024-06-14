from django.test import TestCase
from minuta.forms import FormMinutaCasei

class TestFormMinutaCasei(TestCase):
    def setUp(self):
        self.datos_minuta = {
            'titulominuta':'Minmuta1',
            'fechaminuta':"2024-01-01",
            'minuta':"Contenido Minuta",
            'acuerdos':"AM"
        }

    def test_minuta_form_valido(self):
        form = FormMinutaCasei(self.datos_minuta)
        self.assertTrue(form.is_valid())

    def test_minuta_form_no_titulo(self):
        self.datos_minuta['titulominuta'] = ''
        form = FormMinutaCasei(self.datos_minuta)
        self.assertFalse(form.is_valid())

    def test_minuta_form_no_fecha(self):
        self.datos_minuta['fechaminuta'] = ''
        form = FormMinutaCasei(self.datos_minuta)
        self.assertFalse(form.is_valid())

    def test_minuta_form_no_minuta(self):
        self.datos_minuta['minuta'] = ''
        form = FormMinutaCasei(self.datos_minuta)
        self.assertFalse(form.is_valid())

    def test_minuta_form_no_acuerdos(self):
        self.datos_minuta['acuerdos'] = ''
        form = FormMinutaCasei(self.datos_minuta)
        self.assertFalse(form.is_valid())