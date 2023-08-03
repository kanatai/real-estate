from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    fullname = models.CharField(max_length=250)
    stars = models.IntegerField(max_length=1)
    review_text = models.TextField(max_length=1000, help_text="Enter a review text for company")
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        ordering = ['-created_at']
