from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    url = models.TextField(max_length=1000, help_text="Enter a url of the social app")
    contacts = models.TextField(max_length=1000, help_text="Enter a phone namber of the banner")
    description = models.TextField(max_length=1000, help_text="Enter a description of the banner")
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
        ordering = ['-created_at']


class CompanyImage(models.Model):
    image = models.ImageField(upload_to='banner/')
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_images")

    class Meta:
        verbose_name = _('CompanyImage')
        verbose_name_plural = _('CompanyImages')
        ordering = ['-created_at']