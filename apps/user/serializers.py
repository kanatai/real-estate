from rest_framework import serializers

from apps.user.models import User, UserImage


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_images = UserImageSerializer(many=True)

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
