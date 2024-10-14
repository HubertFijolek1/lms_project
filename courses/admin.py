from django.contrib import admin
from .models import Course, Schedule

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'credits', 'maximum_capacity', 'availability')
    search_fields = ('name', 'description')
    list_filter = ('availability',)
    filter_horizontal = ('prerequisites', 'students')  # For better UI in admin

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'start_time', 'end_time')
    search_fields = ('course__name', 'user__username')
    list_filter = ('course', 'start_time', 'end_time')