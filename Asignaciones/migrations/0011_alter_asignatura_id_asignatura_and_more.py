# Generated by Django 5.1.2 on 2024-11-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asignaciones', '0010_docentes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='id_asignatura',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='nombre_asignatura',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]