from django.shortcuts import render
from clases.models import Clase

# Create your views here.


def get_clases(request):

    clases = Clase.objects.all()
    return render(request, 'clases/lista.html', {'clases': clases})

def get_clase(request, clase_id):

    clase = Clase.objects.get(id=clase_id)
    estudiantes = clase.estudiantes.all()
    return render(request, 'clases/detalle.html', {'estudiantes': estudiantes, 'clase': clase})


