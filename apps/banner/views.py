from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from project import project_permissions
from apps.banner.models import Banner
from apps.banner.serializers import BannerSerializer


class BannerViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    def list(self, request, *args, **kwargs):
        """
        hello
        """
        super().list(self, request, *args, **kwargs)

    def get_queryset(self):
        return Banner.objects.all()

    def get_serializer_class(self):
        return BannerSerializer
