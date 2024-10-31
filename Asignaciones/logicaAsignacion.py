from .models import Aula_o_Laboratorio, Asignatura, Horario_y_materia, Asignacion




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
                id_aula=aula_disponible,
                id_horario=horario
            )

