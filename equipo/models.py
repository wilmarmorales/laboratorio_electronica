from django.db import models
from django.contrib.auth.models import User


class EquipoBase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    img = models.URLField()
    cantidad = models.IntegerField(default=0, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    equipo = models.ForeignKey(EquipoBase, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    prestado = models.BooleanField(default=False)
    buscar = models.CharField(max_length=110, null=True, blank=True)

    def save(self, *args, **kwargs):
        equipobase = EquipoBase.objects.get(id=self.equipo.id)
        equipobase.cantidad = equipobase.cantidad + 1
        self.nombre = equipobase.nombre
        self.buscar = f'{self.codigo} - {self.equipo}'
        equipobase.save()
        super(Equipo, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.codigo} - {self.equipo}'
