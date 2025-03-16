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

    SEMESTRE = {

        "1": "Primero",
        "2": "Segundo",
        "3": "Tercero",
        "4": "Cuarto",
        "5": "Quinto",
        "6": "Sexto",
        "7": "Septimo",
        "8": "Octavo",
        "9": "Noveno",
        "10": "Decimo"
        } 

    id_asignatura = models.CharField(max_length=10,null=False, unique=True)
    nombre_asignatura = models.CharField(primary_key=True, max_length=100)
    progr_academico = models.CharField(max_length=100)
    semestre = models.CharField(max_length=20, choices=SEMESTRE)
    num_creditos = models.IntegerField(validators=[MinValueValidator(1)])
    duracion_en_horas = models.IntegerField(validators=[MinValueValidator(1)])



    def __str__(self):
        return self.nombre_asignatura


class Horario_y_materia(models.Model):
    DIAS = [
        ("Lun", "Lunes"),
        ("Mar", "Martes"),
        ("Mie", "Miércoles"),
        ("Jue", "Jueves"),
        ("Vie", "Viernes"),
    ]
    
    id_materia = models.CharField(primary_key=True, max_length=20, null=False)

    materia = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    grupo = models.CharField(max_length=20, blank=True, null=True)  # Se puede asignar automáticamente
    dia = models.CharField(max_length=3, choices=DIAS, blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    num_estudiantes = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)

    def __str__(self):
        return f"{self.materia} - {self.dia} {self.hora_inicio}-{self.hora_fin}"

        
 

class Docentes (models.Model):
    id_docente = models.CharField(primary_key=True, max_length=12)
    nombre_docente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_docente    

class DisponibilidadDocente(models.Model):
    docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    dia = models.CharField(max_length=10, choices=(
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
    ))
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f'{self.docente.nombre_docente} - {self.dia} {self.hora_inicio}-{self.hora_fin}'

class Asignacion(models.Model):
    
    id_asignacion = models.AutoField(primary_key=True)
    nombre_asignatura = models.ForeignKey(Horario_y_materia, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario_y_materia, on_delete=models.CASCADE)
    id_aula = models.ForeignKey(Aula_o_Laboratorio, on_delete=models.CASCADE)
    id_docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)

    def __str__(self):
             return f"{self.nombre_asignatura.materia} en {self.id_aula} con el docente {self.id_docente}"
