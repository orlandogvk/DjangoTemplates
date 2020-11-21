from django.shortcuts import render
from estudiantes.models import Estudiante


# Create your views here.

def home(request):
    return render(request, 'main/index.html', {})

def get_estudiantes(request):

    estudiantes=Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {'estudiantes':estudiantes})

def get_estudiante(request, estudiante_id):

    estudiante=Estudiante.objects.get(id=estudiante_id)
    return render(request, 'estudiantes/detalle.html', {'estudiante': estudiante})

