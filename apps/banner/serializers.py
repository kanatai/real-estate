from rest_framework import serializers
from apps.banner.models import Banner, BannerImage
from apps.utils import CompressImageField


class BannerImageSerializer(serializers.ModelSerializer):
    image = CompressImageField()
    class Meta:
        model = BannerImage
        fields = "__all__"

    def create(self, validated_data):
        # При создании экземпляра BannerImage мы должны удалить изображение из validated_data,
        # так как это не является допустимым аргументом для метода create().
        image = validated_data.pop('image')

        # Создаем экземпляр BannerImage без изображения
        banner_image = BannerImage.objects.create(**validated_data)

        # Затем сохраняем сжатое изображение, уже после создания экземпляра
        compressed_image = CompressImageField().to_internal_value(image)
        banner_image.image.save('compressed_image.jpg', compressed_image)

        return banner_image


class BannerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class BannerCreateSerializer(BannerBaseSerializer):
    pass


class BannerSerializer(BannerBaseSerializer):
    banner_images = BannerImageSerializer(many=True)