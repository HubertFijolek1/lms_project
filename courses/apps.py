from django.apps import AppConfig

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Extracted constant


class CourseManagementConfig(AppConfig):  # Renamed class
    default_auto_field = DEFAULT_AUTO_FIELD  # Used extracted constant
    name = 'courses'