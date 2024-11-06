from django.db import models
from django.core.validators import MinValueValidator


    #   aqui se definen los modelos o tablas de la base de datos, que luego al aplicar migraciones 

    #   se van a crear en la base de datos de django que en este caso utiliza SQLite

class Aula_o_Laboratorio(models.Model):

    id_aula = models.CharField(primary_key=True, max_length=10, null=False)
    piso = models.IntegerField()
    num_proyector = models.IntegerField()
    televisor = models.BooleanField()
    capacidad_Estudiantes = models.IntegerField()
    num_equipos = models.IntegerField()

    def __str__(self):
         return self.id_aula



class Asignatura (models.Model):

    id_asignatura = models.CharField(max_length=10,null=False)
    nombre_asignatura = models.CharField(primary_key=True, max_length=100)
    progr_academico = models.CharField(max_length=100)
    num_creditos = models.IntegerField(validators=[MinValueValidator(1)])
    duracion_en_horas = models.IntegerField(validators=[MinValueValidator(1)])



    def __str__(self):
        return self.nombre_asignatura


class Horario_y_materia(models.Model):
    
    DIAS = {

        "Lun": "Lunes",
        "Mar": "Martes",
        "Mie": "Miercoles",
        "Jue": "Jueves",
        "Vie": "Viernes"
    } 

    id_materia = models.CharField(primary_key=True, max_length=20,null=False)
    materia = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    grupo = models.CharField(max_length=20)
    dia = models.CharField(max_length=3, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    num_estudiantes = models.IntegerField(validators=[MinValueValidator(1)])



    def __str__(self):
        return self.id_materia


class Docentes (models.Model):
    id_docente = models.CharField(primary_key=True, max_length=12)
    nombre_docente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_docente    



class Asignacion (models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    nombre_asignatura = models.ForeignKey(Horario_y_materia, on_delete=models.CASCADE)
    id_aula = models.ForeignKey(Aula_o_Laboratorio, on_delete=models.CASCADE)
    id_docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    
    


    def __str__(self): return f'Asignación {self.nombre_asignatura}'

