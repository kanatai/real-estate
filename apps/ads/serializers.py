from rest_framework import serializers
from apps.ads.models import Ads


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'