from PIL import Image
from io import BytesIO
from rest_framework import serializers


class CompressImageField(serializers.ImageField):
    def to_internal_value(self, data):
        # Открываем изображение с помощью Pillow
        image = Image.open(data)

        # Сжимаем изображение до желаемого размера
        image = self.compress_image(image)

        # Конвертируем изображение обратно в BytesIO объект
        buffer = BytesIO()
        image.save(buffer, format='JPEG')
        return buffer

    def compress_image(self, image):
        # Ваши логика сжатия здесь.
        # Например, можно изменить размер изображения или изменить его качество.
        # В этом примере просто уменьшим размер вдвое.
        new_width = image.width // 2
        new_height = image.height // 2
        return image.resize((new_width, new_height))