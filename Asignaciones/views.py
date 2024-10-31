
from django.shortcuts import render
from django.http import HttpResponse
from.logicaAsignacion import asignar_aulas
from.models import Asignacion



def verAsignacion(request):
    return render (request, 'Index.html')


def mostrarDashboard(request):
    asignaciones = Asignacion.objects.all()
    return render (request, 'dashboard.html', {'asignaciones': asignaciones})



def mostrarNav(request):
    return render (request, 'nav.html')

def realizarAsignacion(request):
    
    asignar_aulas()  # Llamar a la función para asignar aulas
    asignaciones = Asignacion.objects.all()
    return render(request, 'realizarasignacion.html', {'asignaciones': asignaciones})
