from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Estudiante, Materia
from .forms import EstudianteForm, MateriaForm


@login_required
def materia(request):
    materias = Materia.objects.all()
    return render(request, 'materia/materia.html', {
        'materias': materias,
        'form': MateriaForm,
    })


@login_required
def materia_delete(request, id):
    materia = Materia.objects.get(id=id)
    materia.delete()
    return redirect('materia:materia')


@login_required
def materia_registrar(request):
    if request.method == 'POST':
        materia_form = MateriaForm(request.POST)
        if materia_form.is_valid():
            materia_form.save()
            materia = Materia.objects.first()
            return redirect('materia:estudiante', materia.url)
        materias = Materia.objects.all()
        return render(request, 'materia/materia.html', {
            'materias': materias,
            'form': materia_form,
        })


@login_required
def materia_actualizar(request, id):
    materia = Materia.objects.get(id=id)
    materias = Materia.objects.all()
    if request.method == 'GET':
        materia_form = MateriaForm(instance=materia)
        return render(request, 'materia/materia.html', {
            'materias': materias,
            'form': materia_form,
        })
    if request.method == 'POST':
        materia_form = MateriaForm(request.POST, instance=materia)
        if materia_form.is_valid():
            materia_form.save()
        else:
            return render(request, 'materia/materia.html', {
                'materias': materias,
                'form': materia_form,
            })
    return redirect('materia:materia')


@login_required
def estudiante(request, url):
    materia = Materia.objects.get(url=url)
    estudiantes = Estudiante.objects.filter(materia=materia.pk)
    return render(request, 'materia/estudiante.html', {
        'estudiantes': estudiantes,
        'form': EstudianteForm,
        'materia': materia,
    })


@login_required
def estudiante_delete(request, id, materia_id):
    materia = Materia.objects.get(id=materia_id)
    estudiante = Estudiante.objects.get(codigo=id)
    estudiante.materia.remove(materia.pk)
    return redirect('materia:estudiante', materia.url )


@login_required
def estudiante_registrar(request, id):
    if request.method == 'POST':
        materia = Materia.objects.get(id=id)
        estudiante_form = EstudianteForm(request.POST)
        codigo =   estudiante_form.data['codigo']
        try:
            existe = Estudiante.objects.get(codigo=codigo)
            existe.materia.add(materia.pk)  
            return redirect('materia:estudiante', materia.url)          
        except:
            nombre = estudiante_form.data['nombre']
            guardar_estudiante = Estudiante(
                nombre = nombre,
                codigo = codigo,
            )
            guardar_estudiante.save()
            guardar_estudiante.materia.add(materia.pk)
            return redirect('materia:estudiante', materia.url)


@login_required
def estudiante_actualizar(request, id, materia_id):
    estudiante = Estudiante.objects.get(codigo=id)
    estudiantes = Estudiante.objects.filter(materia=materia_id)
    materia = Materia.objects.get(id=materia_id)
    if request.method == 'GET':
        estudiante_form = EstudianteForm(instance=estudiante)
        return render(request, 'materia/estudiante.html', {
            'estudiantes': estudiantes,
            'form': estudiante_form,
            'materia':materia,
        })
    if request.method == 'POST':
        estudiante_form = EstudianteForm(request.POST, instance=estudiante)
        nombre = estudiante_form.data['nombre']
        codigo = int(estudiante_form.data['codigo'])
        if estudiante_form.is_valid():
            estudiante.nombre = nombre
            if codigo != id:
                copia = Estudiante.objects.get(codigo=id)
                estudiante.codigo = codigo
                estudiante.save()
                for a in copia.materia.all():
                    estudiante.materia.add(a.pk)
                copia.delete()
            else:
                estudiante.save()
            
        else:
            return render(request, 'materia/estudiante.html', {
                'estudiantes': estudiantes,
                'form': estudiante_form,
                'materia':materia,
            })
    return redirect('materia:estudiante', materia.url)
