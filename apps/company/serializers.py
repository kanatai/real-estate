from rest_framework import serializers
from apps.company.models import Company, CompanyImage


class CompanyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImage
        fields = "__all__"


class CompanyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanyCreateSerializer(CompanyBaseSerializer):
    pass


class CompanySerializer(CompanyBaseSerializer):
    company_images = CompanyImageSerializer(many=True)