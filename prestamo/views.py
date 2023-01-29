from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from equipo.models import Equipo
from .models import Prestamo
from .forms import PrestamoForm

@login_required
def prestamos_list(request):
    prestamos = Prestamo.objects.filter(laboratorio=request.user.id).filter(entregado=True)
    prestamoform = PrestamoForm()
    prestamoform.fields["equipo"].queryset = Equipo.objects.filter(laboratorio=request.user.id).filter(prestado=False)

    return render(request, 'prestamo/prestamo_list.html',{
        'prestamos':prestamos,
        'form': prestamoform,
    })

@login_required
def prestamos_list_all(request):
    prestamos = Prestamo.objects.filter(laboratorio=request.user.id)
    return render(request, 'prestamo/prestamo_list.html',{
        'prestamos':prestamos,
        'form': PrestamoForm,
    })

@login_required
def entrega(request, id):
    prestamo=Prestamo.objects.get(id=id)
    equipo=Equipo.objects.get(id=prestamo.equipo.pk)
    equipo.prestado = False
    equipo.save()
    prestamo.entregado = False
    prestamo.save()
    return redirect('prestamo:prestamo')

@login_required
def registrar(request):
    if request.method == 'POST':
        prestamo_form = PrestamoForm(request.POST)
        if prestamo_form.is_valid():
            prestamo_form.save(commit=False)
            equipo = Equipo.objects.get(buscar=prestamo_form.cleaned_data['equipo'])
            equipo.prestado = True
            equipo.save()
            prestamo_form.instance.laboratorio = request.user
            prestamo_form.save()
            return redirect('prestamo:prestamo')
        prestamos = Prestamo.objects.filter(laboratorio=request.user.id).filter(entregado=True)
        return render(request, 'prestamo/prestamo_list.html', {
            'prestamos': prestamos,
            'form': prestamo_form,
        })
