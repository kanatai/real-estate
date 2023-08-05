import uuid

from PIL import Image
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

    def update(self, instance, validated_data):
        # Обновление атрибутов экземпляра UserImage, кроме изображения
        instance.is_main = validated_data.get('is_main', instance.is_main)
        instance.save()

        # Если есть новое изображение в данных, то обновляем изображение
        new_image = validated_data.get('image', None)
        if new_image:
            compressed_image = CompressImageField().to_internal_value(new_image)
            filename = f'{uuid.uuid4()}.jpg'
            instance.image.delete()  # Удаляем старое изображение
            instance.image.save(filename, compressed_image)

        return instance

# class UserUpdateImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserImage
#         exclude = ('created_at')
#
#     def validate_image(self, user_img):
#         img = Image.open(user_img)
#
#         # override old TemporaryFile image with edited image
#         path_to_tmp = user_img.file.name
#         new_filename = "%s.jpeg" % user_img.name.split('.')[0]
#
#         # set new image name
#         img.save(path_to_tmp, format='JPEG', quality=100)
#         user_img.name = new_filename
#         ...
#         return user_img  # no errors more :)

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
