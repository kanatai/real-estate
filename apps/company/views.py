from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, parsers
from rest_framework.viewsets import ModelViewSet

from apps.company.models import Company, CompanyImage
from apps.company.serializers import CompanyCreateSerializer, CompanySerializer, CompanyImageSerializer
from project import project_permissions


class CompanyImageViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]
    parser_classes = (parsers.MultiPartParser,)

    def get_queryset(self):
        return CompanyImage.objects.all()

    def get_serializer_class(self):
        return CompanyImageSerializer


class CompanyViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    def get_queryset(self):
        return Company.objects.all()

    def get_serializer_class(self):
        serializer_map = {
            "retrieve": CompanySerializer,
            "list": CompanySerializer,
            "create": CompanyCreateSerializer
        }
        return serializer_map.get(self.action, CompanySerializer)