from django.contrib import admin
from Asignaciones.models import Asignacion, Asignatura, Aula_o_Laboratorio, Horario_y_materia, Docentes, DisponibilidadDocente
from django.http import HttpResponse
from .formulario import HorarioForm

import openpyxl 
from .models import Asignacion
from .logicaAsignacion import asignar_horarios_y_aulas 



def asignar_horarios(modeladmin, request, queryset):
    asignar_horarios_y_aulas()
    modeladmin.message_user(request, "Horarios y aulas asignados correctamente.")
    
@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ['id_asignacion', 'nombre_asignatura', 'id_aula', 'id_docente']  # Campos a mostrar en el admin
    actions = [asignar_horarios]  # Agregar la acción personalizada


@admin.register(Docentes)
class DocentesAdmin(admin.ModelAdmin):
    change_list_template = 'admin/docentes_change_list.html'  # Usamos un template personalizado para docentes

    def changelist_view(self, request, extra_context=None):
        docentes = Docentes.objects.all()
        disponibilidad = DisponibilidadDocente.objects.all()
        extra_context = extra_context or {}
        extra_context['docentes'] = docentes
        extra_context['disponibilidad'] = disponibilidad
        return super().changelist_view(request, extra_context=extra_context)


'''def realizar_asignaciones(modeladmin, request, queryset):
    
    modeladmin.message_user(request, "Asignaciones realizadas exitosamente")
'''
'''
realizar_asignaciones.short_description = "Realizar Asignaciones Automáticamente"

class Horario_y_materiaAdmin(admin.ModelAdmin):
    actions = [realizar_asignaciones]
    list_display = ["nombre_asignatura", "id_aula", "id_docente"]
'''
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


