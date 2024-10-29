from django.apps import AppConfig


class DatabaseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'databaseApp'



from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'databaseApp'

    def ready(self):
        import databaseApp.signals