from django.shortcuts import get_object_or_404
from rest_framework import permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from apps.apartments.models import Apartment
from apps.favorite.models import Favorite
from apps.favorite.serializers import FavoriteSerializer, FavoriteCreateSerializer
from rest_framework.response import Response


class FavoriteViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {
        'user__id': ['exact'],
        'apartment__title': ['exact'],
        'apartment__type__id': ['exact'],
    }

    search_fields = ['apartment.title']

    def get_queryset(self):
        if self.request.POST:
            user = self.request.user
            apartment = self.request.data['apartment']
            return Favorite.objects.filter(user=user, apartment=apartment)
        else:
            return Favorite.objects.all()

    def post(self, request, *args, **kwargs):
        item_id = request.data.get('apartment')
        apartment = Apartment.objects.get('apartment')
        if not item_id:
            return Response({'item_id': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        exists = Favorite.objects.filter(user=user, apartment__id=item_id).exists()

        if exists:
            return Response({'error': 'Item is already in favorites.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, apartment=apartment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        serializer_map = {
            "list": FavoriteSerializer,
            "create": FavoriteCreateSerializer
        }
        return serializer_map.get(self.action)


    # def perform_create(self, serializer):
    #     if self.get_queryset().exists():
    #         raise ValidationError('You have already saved this apartment!')
    #     serializer.save(user=self.request.user,
    #                     apartment=Apartment.objects.get(pk=self.kwargs['pk']))
    # def favorites_apartment_api(self, request, **kwargs):
    #     where_conditions = kwargs
    #     favorites = Favorite.objects.filter(**where_conditions)
    #     if favorites:
    #         favorites.delete()
    #         for item in favorites:
    #             if item.apartment.author.id == request.user.id and item.apartment.id == request.data['apartment_id']:
    #                 return None
    #             else:
    #                 return None