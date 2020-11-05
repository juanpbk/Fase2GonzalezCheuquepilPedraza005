from django.test import TestCase
from login.models import Juego,Compañia

class JuegoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Juego.objects.create(codigo='4b2fc439-53e4-4e9a-9893-a6359b3034f5', nombre='good of war', fecha='2020-10-06', juego='Adultos+18'  )
    
    def test_nombre_juego_label(self):
        juego = Juego.objects.get(codigo='4b2fc439-53e4-4e9a-9893-a6359b3034f5')
        field_label = juego._meta.get_field('nombre').verbose_name
        self.assertEqual(field_label, 'nombre') 

    def test_fecha_juego_label(self):   
        juego = Juego.objects.get(codigo='4b2fc439-53e4-4e9a-9893-a6359b3034f5')
        field_label = juego._meta.get_field('fecha').verbose_name
        self.assertEqual(field_label, 'fecha') 

    def test_clasificacion_juego_label(self):
        juego = Juego.objects.get(codigo='4b2fc439-53e4-4e9a-9893-a6359b3034f5')
        field_label = juego._meta.get_field('juego').verbose_name
        self.assertEqual(field_label, 'juego') 

class CompañiaModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Compañia.objects.create(id_compañia='c931489c-6906-4b42-b63f-17b0f0edf9a2', nombre_compañia='MIHOYO')

    def test_nombre_juego_label(self):
        comp = Compañia.objects.get(id_compañia='c931489c-6906-4b42-b63f-17b0f0edf9a2')
        field_label = comp._meta.get_field('nombre_compañia').verbose_name
        self.assertEqual(field_label, 'nombre compañia') 