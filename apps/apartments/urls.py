from rest_framework import routers

from apps.apartments import views
from apps.apartments.models import Apartment, ApartmentType, ApartmentImage, Floor, Series, Document

apartment_router = routers.DefaultRouter()
apartment_router.register(r'apartment', views.ApartmentViewSet, basename=Apartment.__name__)
apartment_router.register(r'types/apartments', views.ApartmentTypeViewSet, basename=ApartmentType.__name__)
apartment_router.register(r'image/apartments', views.ApartmentImageViewSet, basename=ApartmentImage.__name__)
apartment_router.register(r'floor/apartment', views.FloorViewSet, basename=Floor.__name__)
apartment_router.register(r'document/apartment', views.DocumentViewSet, basename=Document.__name__)
apartment_router.register(r'series/apartment', views.SeriesViewSet, basename=Series.__name__)
