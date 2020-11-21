from django.db import models
from estudiantes.models import Estudiante

# Create your models here.



class Clase(models.Model):
    nombre=models.CharField(max_length=50)
    salon=models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    estudiantes = models.ManyToManyField(Estudiante, related_name='estudiantes')

