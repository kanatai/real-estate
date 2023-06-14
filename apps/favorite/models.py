from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.apartments.models import Apartment


class Favorite(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')
        ordering = ['-created_at']