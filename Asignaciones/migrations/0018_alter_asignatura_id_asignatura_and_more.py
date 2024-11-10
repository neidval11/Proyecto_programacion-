# Generated by Django 5.1.2 on 2024-11-10 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asignaciones', '0017_asignatura_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='id_asignatura',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='semestre',
            field=models.CharField(choices=[('1', 'Primero'), ('2', 'Segundo'), ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto'), ('6', 'Sexto'), ('7', 'Septimo'), ('8', 'Octavo'), ('9', 'Noveno'), ('10', 'Decimo')], max_length=20),
        ),
    ]
