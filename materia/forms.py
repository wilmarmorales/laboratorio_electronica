from django import forms
from .models import Materia, Estudiante


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'
        widgets = {
            'materia': forms.TextInput(attrs={
                "autocomplete": "off", "type": "text", "class": "form-control", "id": "materia",
                "placeholder": "Osciloscopio",
            }),
            'grupo': forms.TextInput(attrs={
                "autocomplete": "off", "type": "text", "class": "form-control", "id": "grupoMateria",
                "placeholder": "Osciloscopio",
            }),
            'profesor': forms.TextInput(attrs={
                "autocomplete": "off", "type": "text", "class": "form-control", "id": "profesorMateria",
                "placeholder": "Osciloscopio",
            }),
        }
    

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                "autocomplete": "off", "type": "text", "class": "form-control", "id": "nombreEstudiante",
                "placeholder": "Osciloscopio",
            }),
            'codigo': forms.TextInput(attrs={
                "autocomplete": "off", "type": "text", "class": "form-control", "id": "codigoEstudiante",
                "placeholder": "Osciloscopio",
            }),
        }
        