from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

FIELDSETS = UserAdmin.fieldsets + (
    (None, {'fields': ('role', 'completed_courses')}),
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    LIST_DISPLAY = ['username', 'email', 'role', 'is_staff', 'is_active']
    LIST_FILTER = ['is_staff', 'is_active', 'is_superuser', 'role']
    SEARCH_FIELDS = ['username', 'email']

    list_display = LIST_DISPLAY
    list_filter = LIST_FILTER
    search_fields = SEARCH_FIELDS
    fieldsets = FIELDSETS


class UserProfileAdmin(admin.ModelAdmin):
    LIST_DISPLAY = ('user', 'bio')
    LIST_FILTER = ('user__is_active', 'user__date_joined')
    SEARCH_FIELDS = ('user__username', 'user__email', 'bio')

    list_display = LIST_DISPLAY
    list_filter = LIST_FILTER
    search_fields = SEARCH_FIELDS


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)