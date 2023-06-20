from rest_framework import serializers

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            # 'password',
            'groups',
            'user_permissions'
            # 'is_superuser',
        ]
        # fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'password')  # '__all__'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
