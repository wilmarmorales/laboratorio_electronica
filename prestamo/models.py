from django.db import models
from equipo.models import Equipo
from django.contrib.auth.models import User
from materia.models import Materia, Estudiante


class Prestamo(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    entregado = models.BooleanField(default=True)

    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.estudiante}, {self.equipo}, {self.entregado}'

    class Meta:
        ordering = ['-fecha']
    