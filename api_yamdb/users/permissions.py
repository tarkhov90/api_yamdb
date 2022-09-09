from rest_framework import permissions


class IsAuthorOrStaffOrReadOnly(permissions.BasePermission):
    """Пермишен для автора, админа и модератора или только чтение"""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author
                or request.user == request.user.is_admin
                or request.user == request.user.is_moderator)
