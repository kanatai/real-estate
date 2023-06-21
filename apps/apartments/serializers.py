from rest_framework import serializers

from apps.apartments.models import Apartment, ApartmentType, ApartmentImage, Floor, Series, Document
from apps.currency.serializers import CurrencySerializer
from apps.region.serializers import RegionSerializer
from apps.user.serializers import UserSerializer


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"#("title",)


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = "__all__"#("title",)


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"#("title",)


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = "__all__"#("title",)


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = "__all__"


class ApartmentBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = "__all__"


class ApartmentCreateSerializer(ApartmentBaseSerializer):
    pass


class ApartmentSerializer(ApartmentBaseSerializer):
    type = ApartmentTypeSerializer()
    floor = FloorSerializer()
    document = DocumentSerializer()
    series = SeriesSerializer()
    region = RegionSerializer()
    currency = CurrencySerializer()
    apartment_images = ApartmentImageSerializer(many=True)
    author = UserSerializer()
