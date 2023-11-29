from django.db import models

# Create your models here.
class Formulario(models.Model):
    id_p = models.IntegerField(primary_key=True)
    notificaciones = models.CharField(max_length=255)
    ofertas = models.CharField(max_length=255)
    satisfaccion = models.IntegerField()
    productosservicios = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    dispositivos = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    def __str__(self):
        return f"Encuentas Sitio Web: {self.pk}"
    