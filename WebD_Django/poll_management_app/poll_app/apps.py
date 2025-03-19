from django.apps import AppConfig

class PollAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'poll_app'

    def ready(self):
        import poll_app.signals
