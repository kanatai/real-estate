from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework.viewsets import ModelViewSet

from apps.ads.models import Ads
from apps.ads.serializers import AdsSerializer


class AdsViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {'created_at': ['gte', 'lte'],}
    search_fields = ['name']

    def list(self, request, *args, **kwargs):
        """
        Данный Endpoint предназначен для подачи обьявления со стороны клиентов
        """
        super().list(self, request, *args, **kwargs)

    def get_queryset(self):
        return Ads.objects.all()

    def get_serializer_class(self):
        return AdsSerializer