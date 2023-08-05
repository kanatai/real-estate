from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, parsers, mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import response, status

from apps.user.models import User, UserImage
from apps.user.serializers import UserSerializer, UserCreateSerializer, UserImageSerializer, UserUpdateSerializer, \
    UserUpdateImageSerializer
from project import project_permissions


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
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
            "update": UserUpdateSerializer,
            "partial_update": UserUpdateSerializer,
            "create": UserCreateSerializer
        }
        return serializer_map.get(self.action, UserSerializer)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(is_superuser=False)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def get_me(self, request):
        user = request.user
        if not user:
            return response.Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class UserImageViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)

    def get_queryset(self):
        return UserImage.objects.all()

    def get_serializer_class(self):
        serializer_map = {
            "retrieve": UserImageSerializer,
            "list": UserImageSerializer,
            "update": UserUpdateImageSerializer,
            "partial_update": UserUpdateImageSerializer,
            "create": UserImageSerializer
        }
        return serializer_map.get(self.action, UserImageSerializer)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)