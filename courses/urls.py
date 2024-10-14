from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CourseViewSet

app_name = 'courses'

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
urlpatterns = [
    path('enroll/<int:course_id>/', views.enroll_in_course, name='enroll'),
    path('api/', include(router.urls)),
]

