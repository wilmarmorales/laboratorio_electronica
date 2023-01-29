#from django.forms import modelform_factory
from django import forms
from .models import Prestamo
from equipo.models import Equipo


class PrestamoForm(forms.ModelForm):

    """ def __init__(self,request=None ,request_user=False, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)
        if request_user!=False:
            self.fields["equipo"].queryset = Equipo.objects.filter(laboratorio=request_user.user.id).filter(prestado=False) """

    class Meta:
        model = Prestamo
        fields = '__all__'
        exclude = ['laboratorio', 'entregado']

# PrestamoForm = modelform_factory(Prestamo,fields='__all__',exclude = ['laboratorio', 'entregado'])
