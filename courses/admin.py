from django.contrib import admin
from .models import Course, Schedule

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('availability',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'start_time', 'end_time')
    search_fields = ('course__name', 'user__username')
    list_filter = ('course', 'start_time', 'end_time')
