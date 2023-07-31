from rest_framework import serializers

from apps.apartments.models import Apartment, ApartmentType, ApartmentImage, Floor, Series, Document
from apps.currency.serializers import CurrencySerializer
from apps.region.serializers import RegionSerializer
from apps.user.serializers import UserSerializer
from apps.utils import CompressImageField


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
    image = CompressImageField()

    class Meta:
        model = ApartmentImage
        fields = "__all__"

    def create(self, validated_data):
        # При создании экземпляра BannerImage мы должны удалить изображение из validated_data,
        # так как это не является допустимым аргументом для метода create().
        image = validated_data.pop('image')

        # Создаем экземпляр BannerImage без изображения
        banner_image = ApartmentImage.objects.create(**validated_data)

        # Затем сохраняем сжатое изображение, уже после создания экземпляра
        compressed_image = CompressImageField().to_internal_value(image)
        banner_image.image.save('compressed_image.jpg', compressed_image)

        return banner_image


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
