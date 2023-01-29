from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import EquipoBase, Equipo
from .forms import EquipoBaseForm, EquipoForm


@login_required
def equipo(request):
    equipos = Equipo.objects.filter(laboratorio=request.user.id)
    return render(request, 'equipo/equipo.html', {
        'equipos': equipos,
        'form': EquipoForm,
    })


@login_required
def equipo_delete(request, id):
    equipo = Equipo.objects.get(id=id)
    equipoBase = EquipoBase.objects.get(id = equipo.equipo.id)
    equipoBase.cantidad -= 1
    equipoBase.save()
    equipo.delete()
    return redirect('equipo:equipo')


@login_required
def equipo_registrar(request):
    if request.method == 'POST':
        equipo_form = EquipoForm(request.POST)
        if equipo_form.is_valid():
            equipo_form.save(commit=False)
            equipo_form.instance.laboratorio = request.user
            equipo_form.save()
            return redirect('equipo:equipo')
        equipos = Equipo.objects.filter(laboratorio=request.user.id)
        return render(request, 'equipo/equipo.html', {
            'equipos': equipos,
            'form': equipo_form,
        })


@login_required
def equipo_actualizar(request, id):
    equipo = Equipo.objects.get(id=id)
    equipos = Equipo.objects.filter(laboratorio=request.user.id)
    if request.method == 'GET':
        equipo_form = EquipoForm(instance=equipo)
        return render(request, 'equipo/equipo.html', {
            'equipos': equipos,
            'form': equipo_form
        })
    if request.method == 'POST':
        equipo_form = EquipoForm(request.POST, instance=equipo)
        if equipo_form.is_valid():
            equipo_form.save()
        else:
            return render(request, 'equipo/equipo.html', {
                'equipos': equipos,
                'form': equipo_form
            })
    return redirect('equipo:equipo')


@login_required
def equipo_base(request):
    equipos_base = EquipoBase.objects.all()
    return render(request, 'equipo/equipo_base.html', {
        'equipos_base': equipos_base,
        'form': EquipoBaseForm
    })


@login_required
def equipo_base_delete(request, id):
    equipos_base = EquipoBase.objects.get(id=id)
    equipos_base.delete()
    return redirect('equipo:equipo_base')


@login_required
def equipo_base_registrar(request):
    if request.method == 'POST':
        equipo_form = EquipoBaseForm(request.POST)
        if equipo_form.is_valid():
            equipo_form.save()
            return redirect('equipo:equipo_base')
        equipos_base = EquipoBase.objects.all()
        return render(request, 'equipo/equipo_base.html', {
            'equipos_base': equipos_base,
            'form': equipo_form
        })


@login_required
def equipo_base_actualizar(request, id):
    equipo_base = EquipoBase.objects.get(id=id)
    equipos_base = EquipoBase.objects.all()
    if request.method == 'GET':
        equipo_form = EquipoBaseForm(instance=equipo_base)
        return render(request, 'equipo/equipo_base.html', {
            'equipos_base': equipos_base,
            'form': equipo_form
        })
    if request.method == 'POST':
        equipo_form = EquipoBaseForm(request.POST, instance=equipo_base)
        if equipo_form.is_valid():
            equipo_form.save()
        else:
            return render(request, 'equipo/equipo_base.html', {
                'equipos_base': equipos_base,
                'form': equipo_form
            })
    return redirect('equipo:equipo_base')


