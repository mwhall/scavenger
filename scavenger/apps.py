from django.apps import AppConfig


class ScavengerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scavenger'

    def ready(self):
        pass
        #import scavenger.signals
