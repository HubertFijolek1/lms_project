from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile
# from rest_framework_simplejwt.token_blacklist import models as blacklist_models
# from rest_framework_simplejwt.token_blacklist import admin as blacklist_admin
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2', 'role'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        # Add other fieldsets as needed
    )
    list_display = ('email', 'role', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)


FIELDSETS = UserAdmin.fieldsets + (
    (None, {'fields': ('role', 'completed_courses')}),
)

class UserProfileAdmin(admin.ModelAdmin):
    LIST_DISPLAY = ('user', 'bio')
    LIST_FILTER = ('user__is_active', 'user__date_joined')
    SEARCH_FIELDS = ('user__username', 'user__email', 'bio')

    list_display = LIST_DISPLAY
    list_filter = LIST_FILTER
    search_fields = SEARCH_FIELDS


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(blacklist_models.BlacklistedToken, blacklist_admin.BlacklistedTokenAdmin)
# admin.site.register(blacklist_models.OutstandingToken, blacklist_admin.OutstandingTokenAdmin)