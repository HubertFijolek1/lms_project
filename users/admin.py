from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'is_superuser', 'role']
    search_fields = ['username', 'email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'user__email', 'bio')
    list_filter = ('user__is_active', 'user__date_joined')
