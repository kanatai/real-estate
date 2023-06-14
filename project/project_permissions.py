from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'PATCH', 'HEAD', 'OPTIONS')


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_superuser
        )
