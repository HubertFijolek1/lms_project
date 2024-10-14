from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    availability = models.CharField(max_length=50)
    credits = models.IntegerField(default=3)
    maximum_capacity = models.IntegerField(default=30)
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

    def enroll_student(self, student):
        if self.students.count() >= self.maximum_capacity:
            raise ValidationError("Maximum capacity reached.")
        if not self.check_prerequisites(student):
            raise ValidationError("Prerequisites not met.")
        self.students.add(student)

    def check_prerequisites(self, student):
        completed_courses = student.completed_courses.all()
        return all(prereq in completed_courses for prereq in self.prerequisites.all())

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.course.name} - {self.user}"