from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(_('login'), unique=True, max_length=13)
    first_name = models.CharField(_('first name'), max_length=155)
    last_name = models.CharField(_('last name'), max_length=155)
    middle_name = models.CharField(_('middle name'), max_length=155, null=True, blank=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    objects = UserManager()
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['-created_at']

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.get_short_name()

    def create_user(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.objects._create_user(self, login=login, password=password, **extra_fields)
