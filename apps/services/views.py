from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet

from apps.services.models import Service
from apps.services.serializers import ServiceSerializer


class ServiceViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    def get_queryset(self):
        return Service.objects.all()

    def get_serializer_class(self):
        return ServiceSerializer
