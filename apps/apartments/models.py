from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.currency.models import Currency
from apps.region.models import Region
from apps.user.models import User


class ApartmentType(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('ApartmentType')
        verbose_name_plural = _('ApartmentTypes')
        ordering = ['-created_at']


class Floor(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Floor')
        verbose_name_plural = _('Floors')
        ordering = ['-created_at']


class Document(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        ordering = ['-created_at']


class Series(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Series')
        verbose_name_plural = _('Series')
        ordering = ['-created_at']


class Apartment(models.Model):
    title = models.CharField(max_length=256)
    square = models.CharField(max_length=50)
    address = models.CharField(max_length=256)

    communications = models.TextField(max_length=1000, help_text="Enter a description of the apartment")
    description = models.TextField(max_length=1000, help_text="Enter a description of the apartment")

    best = models.BooleanField(False)

    price = models.DecimalField(max_digits=50, decimal_places=2)
    room_count = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=50, decimal_places=6)
    lng = models.DecimalField(max_digits=50, decimal_places=6)

    type = models.ForeignKey(ApartmentType, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Apartment')
        verbose_name_plural = _('Apartments')
        ordering = ['-created_at']


class ApartmentImage(models.Model):
    image = models.ImageField(upload_to='apartment/')
    created_at = models.DateTimeField(_('Created date'), auto_now_add=True)

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="apartment_images")

    class Meta:
        verbose_name = _('ApartmentImage')
        verbose_name_plural = _('ApartmentImages')
        ordering = ['-created_at']

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     compressed_image = compressImage(self)
    #     compressed_image.save(self.image.path, quality=80) # Перезаписываем оригинальное изображение сжатым