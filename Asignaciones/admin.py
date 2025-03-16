from django.contrib import admin
from Asignaciones.models import Asignacion, Asignatura, Aula_o_Laboratorio, Horario_y_materia, Docentes, DisponibilidadDocente
from django.http import HttpResponse
from .formulario import HorarioForm
from django.db import transaction
from django.utils.html import format_html
import openpyxl 
from .models import Asignacion
from .logicaAsignacion import asignar_horarios_y_aulas 
from django.shortcuts import render

def asignar_horarios(modeladmin, request, queryset):
    
    #Función que ejecuta la asignación automática de horarios y aulas.
    
    asignar_horarios_y_aulas()
    modeladmin.message_user(request, "Horarios y aulas asignados correctamente.")

    # Renderiza la plantilla directamente para mostrar los resultados en el admin
    docentes = Docentes.objects.all()
    disponibilidad = DisponibilidadDocente.objects.all()
    return render(request, "admin/docentes_change_list.html", {
        "docentes": docentes,
        "disponibilidad": disponibilidad,
    })

@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ['id_asignacion', 'get_nombre_asignatura', 'id_aula', 'id_docente']
    
    def get_nombre_asignatura(self, obj):
        return obj.nombre_asignatura.materia.nombre_asignatura  # Accede al nombre real de la asignatura
    
    get_nombre_asignatura.short_description = "Asignatura"  # Nombre de la columna en el admin


@admin.register(Docentes)
class DocentesAdmin(admin.ModelAdmin):
    change_list_template = "admin/docentes_change_list.html"

    def changelist_view(self, request, extra_context=None):
        """
        Vista personalizada del listado de docentes en el admin.
        """
        docentes = Docentes.objects.all()
        disponibilidad = DisponibilidadDocente.objects.all()
        extra_context = extra_context or {}
        extra_context["docentes"] = docentes
        extra_context["disponibilidad"] = disponibilidad
        return super().changelist_view(request, extra_context=extra_context)
    


class HorarioAdmin(admin.ModelAdmin): form = HorarioForm 


# Función para exportar las asignaciones seleccionadas a Excel
def exportar_asignaciones_a_excel(modeladmin, request, queryset):
    # Crear un libro de trabajo y una hoja de trabajo
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Asignaciones"

    # Encabezados para el archivo Excel
    encabezados = ['ID Asignación', 'Materia', 'Grupo', 'Día', 'Hora de Inicio', 'Hora de Fin', 'Número de Estudiantes', 'Aula', 'Docente']
    ws.append(encabezados)

    # Añadir los datos de las asignaciones seleccionadas
    for asignacion in queryset:
        fila = [
            asignacion.id_asignacion,
            asignacion.nombre_asignatura.materia.nombre_asignatura,  # Nombre de la asignatura
            asignacion.nombre_asignatura.grupo,  # Grupo
            asignacion.nombre_asignatura.dia,  # Día
            asignacion.nombre_asignatura.hora_inicio,  # Hora de inicio
            asignacion.nombre_asignatura.hora_fin,  # Hora de fin
            asignacion.nombre_asignatura.num_estudiantes,  # Número de estudiantes
            asignacion.id_aula.id_aula,  # ID del aula
            asignacion.id_docente.nombre_docente,  # Nombre del docente
        ]
        ws.append(fila)

    # Preparar la respuesta HTTP para descargar el archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=asignaciones.xlsx'

    # Guardar el libro en la respuesta HTTP
    wb.save(response)

    return response

# Registrar el modelo en el admin
#@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ['id_asignacion', 'nombre_asignatura', 'id_aula', 'id_docente']  # Campos a mostrar en el admin
    actions = [exportar_asignaciones_a_excel]  # Agregar la acción personalizada

# Register your models here.

admin.site.register(Asignatura)
admin.site.register(Aula_o_Laboratorio)
admin.site.register(Horario_y_materia, HorarioAdmin)
#admin.site.register(Docentes)
admin.site.register(DisponibilidadDocente)