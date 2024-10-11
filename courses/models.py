from django.db import models
from django.contrib.auth import get_user_model

MAX_NAME_LENGTH = 255


class Course(models.Model):
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    description = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CourseSchedule(models.Model):
    User = get_user_model()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.course.name} - {self.start_time} to {self.end_time}"