from rest_framework import serializers
from apps.banner.models import Banner, BannerImage


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = "__all__"


class BannerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class BannerCreateSerializer(BannerBaseSerializer):
    pass


class BannerSerializer(BannerBaseSerializer):
    banner_images = BannerImageSerializer(many=True)