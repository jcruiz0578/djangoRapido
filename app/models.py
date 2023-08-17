from django.db import models


# Create your models here.

class Rapido(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_establecimiento = models.CharField(max_length=150, blank=False)
    direccion = models.CharField(max_length=150, blank=False)
    cp = models.CharField(max_length=150, blank=False)
    localidad = models.CharField(max_length=150, blank=False)
    provincia = models.CharField(max_length=150, blank=False)
    persona_contacto = models.CharField(max_length=150, blank=False)
    telefono_contacto = models.CharField(max_length=150, blank=False)
    email = models.CharField(max_length=150, blank=True)
    sector_actividad = models.CharField(max_length=150, blank=False)
    TIPOTERMINAL = (
        ('N/A', 'N/A'),
        ('CAJERO', 'CAJERO'),
        ('DATAFONO', 'DATAFONO'),
    )
    tipo_terminal = models.CharField(max_length=10, choices=TIPOTERMINAL, blank=False)
    comision = models.IntegerField(blank=False)

    RETORNO = (
        ('N/A', 'N/A'),
        ('SI', 'SI'),
        ('NO', 'NO'),
    )

    retorno = models.CharField(max_length=3, choices=RETORNO, blank=False)
    fondo_inicial = models.IntegerField(blank=False)

    APORTACION = (
        ('N/A', 'N/A'),
        ('CLIENTE', 'CLIENTE'),
        ('NOSOTROS', 'NOSOTROS'),
    )

    aportacion_fondo = models.CharField(max_length=10, choices=APORTACION, blank=False)

    METODO_RE = (
        ('N/A', 'N/A'),
        ('LOOMIS', 'LOMIS'),
        ('TRASFERENCIA', 'TRASFERENCIA'),
        ('TARJETA', 'TARJETA'),
    )

    metodo_reposicion = models.CharField(max_length=15, choices=APORTACION, blank=False)

    def __str__(self):
        return self.nombre_establecimiento
