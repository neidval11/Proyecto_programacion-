
from django.shortcuts import render
from django.http import HttpResponse
from.logicaAsignacion import asignar_aulas
from.models import Asignacion, Aula_o_Laboratorio
import matplotlib as plt
import io
import urllib, base64
import matplotlib.pyplot as plt


    #   aqui se definen los metodos que van a ser llamados desde las urls,
    #   tambien estos mismos metodos van a llamar a los archivos HTML con el contenido de cada vista

def verAsignacion(request):
    asignaciones = Asignacion.objects.all()
    return render (request, 'Index.html', {'asignaciones': asignaciones})


def mostrarDashboard(request):

    #Grafico ocupacion de aulas

    asignaciones = Asignacion.objects.all() 
    aulas = Aula_o_Laboratorio.objects.all()

    ocupacion_aulas = {aula.id_aula: 0 for aula in aulas} 
    for asignacion in asignaciones: ocupacion_aulas[asignacion.id_aula.id_aula] += 1

    fig, ax = plt.subplots() 
    aulas_ids = list(ocupacion_aulas.keys()) 
    ocupaciones = list(ocupacion_aulas.values())
    ax.bar(aulas_ids, ocupaciones)
    ax.set_xlabel('Aulas')
    ax.set_ylabel('Cantidad de Asignaciones')
    ax.set_title('Ocupación Actual de Aulas')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    context = { 'asignaciones': asignaciones, 'ocupacion_aulas': ocupacion_aulas, 'graph': uri}


    return render(request, 'dashboard.html', context)


def mostrarNav(request):
    return render (request, 'nav.html')

def realizarAsignacion(request):
    
    asignar_aulas()  #  se llama a la función para asignar aulas
    asignaciones = Asignacion.objects.all()
    return render(request, 'realizarasignacion.html', {'asignaciones': asignaciones})


