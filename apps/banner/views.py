from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, parsers, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from project import project_permissions
from apps.banner.models import Banner, BannerImage
from apps.banner.serializers import BannerSerializer, BannerImageSerializer, BannerCreateSerializer


class BannerImageViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    permission_classes = [project_permissions.IsAdmin]
    parser_classes = (parsers.MultiPartParser,)

    def get_queryset(self):
        return BannerImage.objects.all()

    def get_serializer_class(self):
        return BannerImageSerializer


class BannerViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    def get_queryset(self):
        return Banner.objects.all()

    def get_serializer_class(self):
        serializer_map = {
            "retrieve": BannerSerializer,
            "list": BannerSerializer,
            "create": BannerCreateSerializer
        }
        return serializer_map.get(self.action, BannerSerializer)
