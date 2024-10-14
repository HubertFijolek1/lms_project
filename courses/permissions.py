from rest_framework import permissions

class IsTeacherOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow only teachers or admins to create, update, or delete courses.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.role in ['TEACHER', 'ADMIN']
        return False