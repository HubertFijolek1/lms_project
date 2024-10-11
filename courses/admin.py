### courses/admin.py

from django.contrib import admin
from .models import Course, Schedule


class BaseAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_filter = ('availability',)


@admin.register(Course)
class CourseAdmin(BaseAdmin):
    list_display = ('name', 'description', 'availability')


@admin.register(Schedule)
class ScheduleAdmin(BaseAdmin):
    list_display = ('course', 'user', 'start_time', 'end_time')
    search_fields = ('course__name', 'user__username')
    list_filter = ('course', 'start_time', 'end_time')