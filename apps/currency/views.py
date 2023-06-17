from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from apps.currency.models import Currency
from apps.currency.serializers import CurrencySerializer
from project import project_permissions


class CurrencyViewSet(ModelViewSet):
    permission_classes = [project_permissions.IsAdmin]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {'created_at': ['gte', 'lte'],}
    search_fields = ['name', 'symbol']

    def get_queryset(self):
        return Currency.objects.all()

    def get_serializer_class(self):
        return CurrencySerializer