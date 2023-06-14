from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet

from apps.region.models import Region
from apps.region.serializers import RegionSerializer


class RegionViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

    def get_queryset(self):
        return Region.objects.all()

    def get_serializer_class(self):
        return RegionSerializer
