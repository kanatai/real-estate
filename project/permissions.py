from rest_framework import permissions


def has_permission(request, view):
    # allow all POST requests
    if request.method == 'POST':
        return True

    # Otherwise, only allow authenticated requests
    # Post Django 1.10, 'is_authenticated' is a read-only attribute
    return request.user and request.user.is_authenticated


class IsPostOrIsAuthenticated(permissions.BasePermission):
    pass


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return request.user.is_superuser
        # Otherwise, only allow authenticated requests
        return True
