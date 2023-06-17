from django.db import models
from django.utils.translation import gettext_lazy as _


class Ads(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Ads')
        verbose_name_plural = _('Ads')
        ordering = ['-created_at']