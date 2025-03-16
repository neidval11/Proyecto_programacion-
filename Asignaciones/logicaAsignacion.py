from .models import Aula_o_Laboratorio, Asignatura, Horario_y_materia, Asignacion, Docentes, DisponibilidadDocente
from django.db import transaction
from datetime import timedelta, datetime

def asignar_horarios_y_aulas():
    # Obtener todas las asignaturas sin asignación
    asignaturas = Asignatura.objects.all()
    
    # Obtener todas las aulas ordenadas por capacidad (de menor a mayor)
    aulas = Aula_o_Laboratorio.objects.order_by('capacidad_Estudiantes')

    with transaction.atomic():  # Garantiza que la asignación sea segura y se haga en bloque
        for asignatura in asignaturas:
            # Buscar un docente disponible para esta asignatura
            docente_disponible = None
            disponibilidad_docente = None
            
            for docente in Docentes.objects.all():
                disponibilidad = DisponibilidadDocente.objects.filter(docente=docente)
                if disponibilidad.exists():
                    docente_disponible = docente
                    disponibilidad_docente = disponibilidad.first()
                    break  # Se elige el primer docente disponible
            
            if not docente_disponible:
                print(f"No hay docentes disponibles para la asignatura {asignatura.nombre_asignatura}")
                continue

            # Elegir un aula con capacidad suficiente
            aula_asignada = None
            for aula in aulas:
                if aula.capacidad_Estudiantes >= 30:  # Se puede ajustar según el número de estudiantes
                    aula_asignada = aula
                    break

            if not aula_asignada:
                print(f"No hay aulas disponibles para la asignatura {asignatura.nombre_asignatura}")
                continue
            
            # Calcular horario basado en la disponibilidad del docente
            hora_inicio = disponibilidad_docente.hora_inicio
            hora_fin = (datetime.combine(datetime.today(), hora_inicio) + timedelta(hours=2)).time()  # Ejemplo: 2 horas de clase

            # Crear el horario de la materia
            horario = Horario_y_materia.objects.create(
                materia=asignatura,
                grupo="Grupo1",
                dia=disponibilidad_docente.dia,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                num_estudiantes=30  # Número de estudiantes por defecto (puede ser variable)
            )

            # Crear la asignación de aula y docente
            Asignacion.objects.create(
                horario=horario,
                id_aula=aula_asignada,
                id_docente=docente_disponible
            )

            print(f"Asignación creada para {asignatura.nombre_asignatura}: {docente_disponible.nombre_docente} en {aula_asignada.id_aula}")

