from django.db import models

# Create your models here.


class EMPLEADO(models.Model):
    ID = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=35)
    departamento = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)

