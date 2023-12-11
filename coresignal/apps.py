from django.apps import AppConfig


class CoresignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coresignal'

    # def ready(self):
    #     # Import the signal and the receiver to ensure they are registered
    #     import coresignal.handlesignal