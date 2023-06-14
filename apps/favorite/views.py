from rest_framework import permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from apps.apartments.models import Apartment
from apps.favorite.models import Favorite
from apps.favorite.serializers import FavoriteSerializer, FavoriteCreateSerializer


class FavoriteViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {
        'apartment__title': ['exact'],
        'apartment__type.id': ['exact'],
    }
    search_fields = ['apartment.title']

    def get_queryset(self):
        apartment = Apartment.objects.get(pk=self.kwargs['pk'])
        user = self.request.user
        return Favorite.objects.filter(user=user,
                                       apartment=apartment)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already saved this apartment!')
        serializer.save(user=self.request.user,
                        apartment=Apartment.objects.get(pk=self.kwargs['pk']))

    # def get_queryset(self):
    #     return Favorite.objects.all()

    def get_serializer_class(self):
        serializer_map = {
            "list": FavoriteSerializer,
            "create": FavoriteCreateSerializer
        }
        return serializer_map.get(self.action)
