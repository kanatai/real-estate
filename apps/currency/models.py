from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    symbol = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
        ordering = ['-created_at']