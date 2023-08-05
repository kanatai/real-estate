import uuid

from rest_framework import serializers
from apps.user.models import User, UserImage
from apps.utils import CompressImageField


class UserImageSerializer(serializers.ModelSerializer):
    image = CompressImageField()

    class Meta:
        model = UserImage
        fields = '__all__'

    def create(self, validated_data):
        # При создании экземпляра BannerImage мы должны удалить изображение из validated_data,
        # так как это не является допустимым аргументом для метода create().
        image = validated_data.pop('image')

        # Создаем экземпляр BannerImage без изображения
        banner_image = UserImage.objects.create(**validated_data)

        # Затем сохраняем сжатое изображение, уже после создания экземпляра
        compressed_image = CompressImageField().to_internal_value(image)
        filename = f'{uuid.uuid4()}.jpg'
        banner_image.image.save(filename, compressed_image)

        return banner_image


class UserSerializer(serializers.ModelSerializer):
    user_images = UserImageSerializer(many=True)

    class Meta:
        model = User
        exclude = [
            'password',
            'groups',
            'user_permissions'
            # 'is_superuser',
        ]


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('login', 'password')  # '__all__'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'login',
            'first_name',
            'last_name',
            'middle_name',
            'created_at',
            'is_active',
            'is_superuser'
        )
