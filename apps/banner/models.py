from django.db import models
from django.utils.translation import gettext_lazy as _


class Banner(models.Model):
    title = models.CharField(max_length=250)
    url = models.TextField(max_length=1000, help_text="Enter a url of the banner")
    description = models.TextField(max_length=1000, help_text="Enter a description of the banner")
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')
        ordering = ['-created_at']