from django.apps import AppConfig


    #   aqui se va a configurar la aplicaciones definidas para el proyecto

class AsignacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Asignaciones'
    verbose_name = 'Asignaciones Realizadas'

    def ready(self):
        import Asignaciones.signals
