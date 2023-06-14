from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from project import project_permissions
from apps.services.models import Service
from apps.services.serializers import ServiceSerializer


class ServiceViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    def get_queryset(self):
        return Service.objects.all()

    def get_serializer_class(self):
        return ServiceSerializer
