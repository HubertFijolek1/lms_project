from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    availability = models.CharField(max_length=50)
    credits = models.IntegerField(default=3)  # New field for course credits
    maximum_capacity = models.IntegerField(default=30)  # New field for max capacity
    prerequisites = models.ManyToManyField(
        'self', symmetrical=False, blank=True, related_name='required_for'
    )

    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='enrolled_courses',
        blank=True,
    )

    def __str__(self):
        return self.name

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.course.name} - {self.user}"