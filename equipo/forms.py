from django import forms
from .models import EquipoBase, Equipo


class EquipoBaseForm(forms.ModelForm):
    class Meta:
        model = EquipoBase
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                "autocomplete": "off", "type": "text", "class": "form-control", "id": "nombreEquipoBase",
                "placeholder": "Osciloscopio",
            }),
            'descripcion': forms.Textarea(attrs={
                "class": "form-control", "id": "descripcionEquipoBase", "rows": "3",
            }),
            'img': forms.TextInput(attrs={
                "autocomplete": "off", "type": "text", "class": "form-control", "id": "urlImagenEquipoBase",
                "placeholder": "https://www.imagenes.com/imagen.jpg",
            }),
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={
                "autocomplete": "off", "type": "text", "class": "form-control", "id": "codigoEquipo",
                "placeholder": "123456789",
            }),
            'equipo': forms.Select(attrs={
                "class": "form-control", "id": "Equipo",
            }),
        }