from django.apps import AppConfig

class MessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Mess'
    
    def ready(self):
        # scheduling emailing
        from . import update
        update.start()    
