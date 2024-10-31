from django.contrib import admin
from Asignaciones.models import Asignacion, Asignatura, Aula_o_Laboratorio, Horario_y_materia
from .logicaAsignacion import asignar_aulas

def realizar_asignaciones(modeladmin, request, queryset):
    asignar_aulas()
    modeladmin.message_user(request, "Asignaciones realizadas exitosamente")

realizar_asignaciones.short_description = "Realizar Asignaciones Automáticamente"

class Horario_y_materiaAdmin(admin.ModelAdmin):
    actions = [realizar_asignaciones]

    

# Register your models here.
admin.site.register(Asignacion)
admin.site.register(Asignatura)
admin.site.register(Aula_o_Laboratorio)
admin.site.register(Horario_y_materia)


