from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.course.name} - {self.start_time} to {self.end_time}"
