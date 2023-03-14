from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()
    fecha_inicio = models.DateField(null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.comision}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)
    comision = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)
    profesion = models.CharField(max_length=128, null=True)
    bio = models.TextField(null=True)
    comision = models.CharField(max_length=256, null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"