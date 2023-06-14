from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet

from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {
        'login': ['exact'],
        'is_staff': ['exact']
    }
    search_fields = ['login']

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer
