# Generated by Django 4.2.16 on 2024-10-14 12:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_alter_course_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='course',
            name='maximum_capacity',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, related_name='required_for', to='courses.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='enrolled_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
