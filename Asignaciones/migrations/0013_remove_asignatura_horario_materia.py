# Generated by Django 5.1.2 on 2024-11-05 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asignaciones', '0012_alter_horario_y_materia_materia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='horario_materia',
        ),
    ]
