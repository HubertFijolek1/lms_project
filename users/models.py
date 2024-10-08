from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(
        max_length=20, choices=USER_ROLES, default='student'
    )

    def is_student(self):
        return self.role == 'student'

    def is_teacher(self):
        return self.role == 'teacher'

    def is_admin(self):
        return self.role == 'admin'


User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username