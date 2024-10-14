from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('enroll/<int:course_id>/', views.enroll_in_course, name='enroll'),
]