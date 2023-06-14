from rest_framework import serializers

from apps.apartments.serializers import ApartmentSerializer
from apps.favorite.models import Favorite
# from apps.apartments.serializers import ApartmentSerializer


class FavoriteBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


class FavoriteCreateSerializer(FavoriteBaseSerializer):
    pass


class FavoriteSerializer(FavoriteBaseSerializer):
    apartment = ApartmentSerializer()