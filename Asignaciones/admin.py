from django.contrib import admin
from Asignaciones.models import Asignacion, Asignatura, Aula_o_Laboratorio, Horario_y_materia, Docentes
from .logicaAsignacion import asignar_aulas
from .formulario import HorarioForm

def realizar_asignaciones(modeladmin, request, queryset):
    asignar_aulas()
    modeladmin.message_user(request, "Asignaciones realizadas exitosamente")


realizar_asignaciones.short_description = "Realizar Asignaciones Automáticamente"

class Horario_y_materiaAdmin(admin.ModelAdmin, admin.TabularInline):
    actions = [realizar_asignaciones]
    list_display = ["nombre_asignatura", "id_aula", "id_docente"]

class HorarioAdmin(admin.ModelAdmin): form = HorarioForm 

# Register your models here.
admin.site.register(Asignacion)
admin.site.register(Asignatura)
admin.site.register(Aula_o_Laboratorio)
admin.site.register(Horario_y_materia, HorarioAdmin)
admin.site.register(Docentes)


