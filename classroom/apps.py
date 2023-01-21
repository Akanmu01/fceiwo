from django.apps import AppConfig


class ClassroomConfig(AppConfig):
    name = 'classroom'
    
    def ready(self):
        import classroom.signals
        
    default_auto_field = 'django.db.models.BigAutoField'

