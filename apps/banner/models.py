from PIL import Image
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


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner/')
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name="banner_images")

    class Meta:
        verbose_name = _('ApartmentImage')
        verbose_name_plural = _('ApartmentImages')
        ordering = ['-created_at']

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     compressed_image = compressImage(self)
    #     compressed_image.save(self.image.path, quality=80) # Перезаписываем оригинальное изображение сжатым

