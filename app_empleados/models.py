from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=100)
    apellido_empleado = models.CharField(max_length=100)
    rfc_empleado = models.CharField(max_length=13, unique=True)
    puesto_empleado = models.CharField(max_length=100)
    contratacion_empleado = models.DateField()

    def __str__(self):
        return f'Empleado: {self.nombre_empleado} {self.apellido_empleado} ({self.puesto_empleado})'
