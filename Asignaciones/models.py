from django.db import models

class Aula_o_Laboratorio(models.Model):

    id_aula = models.CharField(primary_key=True, max_length=10, null=False)
    piso = models.IntegerField()
    num_proyector = models.IntegerField()
    televisor = models.BooleanField()
    capacidad_Estudiantes = models.IntegerField()
    num_equipos = models.IntegerField()

    def __str__(self):
         return self.id_aula

'''
class Horario(models.Model):
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]'''

class Horario_y_materia(models.Model):
    id_horario = models.CharField(primary_key=True, max_length=20,null=False)
    materia = models.CharField(max_length=100, null= False)
    dia = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    grupo = models.CharField(max_length=20)
    docente = models.CharField(max_length=100)
    num_estudiantes = models.IntegerField()



    def __str__(self):
        return self.materia

    


class Asignatura (models.Model):

    id_asignatura = models.CharField(primary_key=True, max_length=10,null=False)
    nombre_asignatura = models.CharField(max_length=100)
    docente_asignatura = models.CharField(max_length=60)
    progr_academico = models.CharField(max_length=100)
    num_creditos = models.IntegerField()
    duracion_en_horas = models.IntegerField()
    horario_materia = models.CharField(max_length=100, null= True)


    def __str__(self):
        return self.nombre_asignatura

class Asignacion (models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    nombre_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    id_aula = models.ForeignKey(Aula_o_Laboratorio, on_delete=models.CASCADE)
    id_horario = models.ForeignKey(Horario_y_materia, on_delete=models.CASCADE)


    def __str__(self): return f'Asignación {self.id_asignacion}'