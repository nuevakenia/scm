from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Empleado(models.Model):

    nombre = models.CharField(max_length=300)
    rut = models.CharField(max_length=10)
    telefono = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"

class Ingreso(models.Model):
    empleado = models.ForeignKey(Empleado, related_name='ingresos_empleado', on_delete=models.CASCADE)
    dispositivo = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='fotos/ingresos/', null=True, blank=True)
    ingreso = models.DateTimeField(null=True, blank=True)
    salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.empleado}_{self.ingreso}"
    