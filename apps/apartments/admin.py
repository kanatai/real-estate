from django.contrib import admin

from apps.apartments.models import Apartment, ApartmentType, Floor, Document, ApartmentImage


# Register your models here.
admin.site.register(Apartment)
admin.site.register(ApartmentType)
admin.site.register(Floor)
admin.site.register(Document)
admin.site.register(ApartmentImage)
