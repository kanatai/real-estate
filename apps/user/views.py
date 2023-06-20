from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet
from rest_framework import response, status

from apps.user.models import User
from apps.user.serializers import UserSerializer, UserCreateSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    filterset_fields = {
        'login': ['exact'],
        'is_superuser': ['exact']
    }
    search_fields = ['login']

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        serializer_map = {
            "retrieve": UserSerializer,
            "list": UserSerializer,
            "create": UserCreateSerializer
        }
        return serializer_map.get(self.action)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(is_superuser=False)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)