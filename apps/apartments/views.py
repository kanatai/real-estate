from rest_framework import filters, parsers, mixins
from project import project_permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from apps.apartments.models import ApartmentType, Apartment, ApartmentImage, Floor, Series, Document
from apps.apartments.serializers import ApartmentSerializer, ApartmentTypeSerializer, ApartmentCreateSerializer, \
    ApartmentImageSerializer, FloorSerializer, SeriesSerializer, DocumentSerializer, ApartmentBaseSerializer


# Create your views here.
class ApartmentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    permission_classes = [project_permissions.IsAdmin]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {
        'title': ['exact'],
        'type': ['exact'],
        'series': ['exact'],
        'region': ['exact'],
        'room_count': ['exact'],
        'floor__title': ['exact'],
        'square': ['gte', 'lte'],
        'price': ['gte', 'lte'],
        'created_at': ['gte', 'lte'],
        'best': ['exact']

    }
    search_fields = ['title']

    def get_queryset(self):
        return Apartment.objects.all()

    def get_serializer_class(self):
        serializer_map = {
            "retrieve": ApartmentSerializer,
            "list": ApartmentSerializer,
            "update": ApartmentBaseSerializer,
            "partial_update": ApartmentBaseSerializer,
            "create": ApartmentCreateSerializer
        }
        return serializer_map.get(self.action, ApartmentSerializer)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class ApartmentTypeViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]

    def get_queryset(self):
        return ApartmentType.objects.all()

    def get_serializer_class(self):
        return ApartmentTypeSerializer


class ApartmentImageViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]
    parser_classes = (parsers.MultiPartParser,)

    def get_queryset(self):
        return ApartmentImage.objects.all()

    def get_serializer_class(self):
        return ApartmentImageSerializer


class FloorViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]

    def get_queryset(self):
        return Floor.objects.all()

    def get_serializer_class(self):
        return FloorSerializer


class SeriesViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]

    def get_queryset(self):
        return Series.objects.all()

    def get_serializer_class(self):
        return SeriesSerializer


class DocumentViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]

    def get_queryset(self):
        return Document.objects.all()

    def get_serializer_class(self):
        return DocumentSerializer
