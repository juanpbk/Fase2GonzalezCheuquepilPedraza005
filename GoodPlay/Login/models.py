from django.db import models
from django.urls import reverse  		#redirecciona una url de un libro al browser 
import uuid  							#se utiliza para definir atributos clave (pk)

# Create your models here.

class Juego(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Indique el Codigo del VideoJuego')
    nombre = models.CharField(max_length=60, help_text="Ingrese el Nombre del VideoJuego")
    compañia = models.ForeignKey('Compañia', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(null=True, blank=True)

    CLASIFICACION_JUEGO = (
        ('E','Todos'),
        ('E+10','Todos + 10'),
        ('T','Adolecentes'),
        ('M','Maduro +17'),
        ('A','Adultos +18'),
        ('RP','Clasificacion Pendiente'),
    )
    
    juego = models.CharField(
        max_length= 4,
        choices= CLASIFICACION_JUEGO,
        default='E',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.nombre},({self.compañia}),{self.codigo}'

class Compañia(models.Model):
    id_compañia = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Indique el Nombre de la Compañia')
    nombre_compañia = models.CharField(max_length=60, help_text="Ingrese el Nombre de la Compañia")

    def __str__(self):
        return self.nombre_compañia


