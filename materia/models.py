from django.db import models
from django.utils.text import slugify
from datetime import date


class Materia(models.Model):
    materia=models.CharField(max_length=100)
    grupo=models.CharField(max_length=100)
    profesor=models.CharField(max_length=100)
    url = models.SlugField(max_length=100, unique=True, blank=True)
    nombre=models.CharField(max_length=150, unique=True, blank=True)
    creado = models.DateField(auto_now_add=True)
    fecha = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-fecha']

    def save(self, *args, **kwargs):
        fecha = date.today()
        año = fecha.year
        mes = fecha.month
        semestre = 'I' if 6>mes else 'II'
        self.nombre = '{} - {} {} {}'.format(self.materia, self.grupo, año,semestre)
        self.url = slugify(self.nombre)
        super(Materia, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.url


    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre=models.CharField(max_length=100)
    codigo=models.CharField(max_length=13, primary_key=True)
    materia=models.ManyToManyField(Materia, blank=True)
    url = models.SlugField(max_length=100, unique=True, blank=True)
    creado = models.DateField(auto_now_add=True)
    fecha = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.url = slugify(self.codigo)
        super(Estudiante, self).save(*args, **kwargs)

    def __str__(self):
        return "{}, {}".format(self.codigo, self.nombre)
