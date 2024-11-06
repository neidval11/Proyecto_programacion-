
from django.shortcuts import render
from django.http import HttpResponse
from.logicaAsignacion import asignar_aulas
from.models import Asignacion

    #   aqui se definen los metodos que van a ser llamados desde las urls,
    #   tambien estos mismos metodos van a llamar a los archivos HTML con el contenido de cada vista

def verAsignacion(request):
    asignaciones = Asignacion.objects.all()
    return render (request, 'Index.html', {'asignaciones': asignaciones})


def mostrarDashboard(request):

    return render (request, 'dashboard.html')



def mostrarNav(request):
    return render (request, 'nav.html')

def realizarAsignacion(request):
    
    asignar_aulas()  #  se llama a la función para asignar aulas
    asignaciones = Asignacion.objects.all()
    return render(request, 'realizarasignacion.html', {'asignaciones': asignaciones})
