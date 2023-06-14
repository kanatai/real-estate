from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers


class SwaggerResponseSerializer(serializers.Serializer):
    serializer = None
    data = serializers.SerializerMethodField()
    error = serializers.BooleanField()
    message = serializers.CharField(allow_null=True)

    def __init__(self, serializer, **kwargs):
        super().__init__(**kwargs)
        self.serializer = serializer

    @swagger_serializer_method(serializer_or_field=serializer)
    def get_data(self, obj):
        return self.serializer(obj).data