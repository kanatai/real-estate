from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.user.models import User, UserImage


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions',),
        }),
        (_('PersonData'), {
            'fields': ('first_name', 'last_name', 'middle_name'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2'),
        }),
    )
    list_display = ('login',)
    list_filter = ('is_active',)
    search_fields = ('login',)
    ordering = ('login', 'created_at')
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserImage)