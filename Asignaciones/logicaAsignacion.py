from .models import Aula_o_Laboratorio, Asignatura, Horario_y_materia, Asignacion, Docentes, DisponibilidadDocente
from django.db import transaction
from datetime import datetime

def asignar_horarios_y_aulas():
    # Obtener todos los docentes y su disponibilidad
    docentes = Docentes.objects.all()

    # Obtener las asignaturas que necesitan asignación
    asignaturas = Asignatura.objects.all()

    # Crear la asignación de horarios
    for asignatura in asignaturas:
        for docente in docentes:
            # Obtener la disponibilidad del docente
            disponibilidad = DisponibilidadDocente.objects.filter(docente=docente)

            for disponibilidad_docente in disponibilidad:
                # Verificar si el docente está disponible para la asignatura (aquí puedes agregar lógica personalizada)
                if True:  # Si el docente está disponible en ese día y hora
                    # Aquí se puede agregar la lógica para asignar el aula
                    aula = Aula_o_Laboratorio.objects.first()  # Ejemplo: seleccionar la primera aula disponible (esto se puede optimizar)
                    
                    # Crear la asignación
                    Horario_y_materia.objects.create(
                        materia=asignatura,
                        grupo="Grupo1",  # Aquí puedes definir la lógica del grupo
                        dia=disponibilidad_docente.dia,
                        hora_inicio=disponibilidad_docente.hora_inicio,
                        hora_fin=disponibilidad_docente.hora_fin,
                        num_estudiantes=30  # Ejemplo: número de estudiantes (puedes ajustarlo)
                    )

                    # Crear la asignación de aula y docente
                    Asignacion.objects.create(
                        nombre_asignatura=Horario_y_materia.objects.last(),
                        id_aula=aula,
                        id_docente=docente
                    )

                    # Salir del bucle cuando se asigna un docente y aula
                    break


'''def realizar_asignaciones(modeladmin, request, queryset):
    asignar_aulas()
    modeladmin.message_user(request, "Asignaciones realizadas exitosamente")

def asignar_aulas():
    horarios = Horario_y_materia.objects.all()

    for horario in horarios:
        # Obtener las aulas ya asignadas para el horario
        aulas_asignadas = Asignacion.objects.filter(id_horario=horario).values_list('id_aula', flat=True)
        
        # Buscar aula disponible con la capacidad suficiente
        aula_disponible = Aula_o_Laboratorio.objects.exclude(id_aula__in=aulas_asignadas).filter(
            capacidad_Estudiantes__gte=horario.num_estudiantes
        ).first()
        
        if aula_disponible:
            # Buscar docentes que estén disponibles para el horario
            docentes_disponibles = docente.objects.exclude(
                id_docente__in=Asignacion.objects.filter(id_horario=horario).values_list('id_docente', flat=True)
            )
            
            # Verificar que el docente no esté asignado a otra clase en el mismo horario
            for docente in docentes_disponibles:
                if not Asignacion.objects.filter(id_docente=docente, id_horario__horario=horario.horario).exists():
                    # Crear la asignación de la clase
                    Asignacion.objects.create(
                        nombre_asignatura=horario,
                        id_aula=aula_disponible,
                        id_docente=docente
                    )
                    break  # Se asigna el aula y docente, se rompe el ciclo
                else:
                    continue  # Si el docente ya está ocupado, se continúa buscando otro

        else:
            print(f"No se encontró aula disponible para el horario {horario.horario}.")
'''

'''

def asignar_aulas():
    horarios = Horario_y_materia.objects.all()

    for horario in horarios:
        aulas_asignadas = Asignacion.objects.filter(id_horario=horario).values_list('id_aula', flat=True)
        aula_disponible = Aula_o_Laboratorio.objects.exclude(id_aula__in=aulas_asignadas).filter(
            capacidad_Estudiantes__gte=horario.num_estudiantes
        ).first()

        if aula_disponible:
            Asignacion.objects.create(
                nombre_asignatura=horario,
                id_aula=aula_disponible
                
            )
            break

'''