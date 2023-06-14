from rest_framework import serializers

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'groups',
            'user_permissions',
            'is_superuser',
            'is_staff'
            ]
        # fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"