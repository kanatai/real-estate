from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet

from apps.banner.models import Banner
from apps.banner.serializers import BannerSerializer


class BannerViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    def get_queryset(self):
        return Banner.objects.all()

    def get_serializer_class(self):
        return BannerSerializer