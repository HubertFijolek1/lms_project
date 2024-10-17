from django.apps import AppConfig

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

class CourseManagementConfig(AppConfig):
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'courses'