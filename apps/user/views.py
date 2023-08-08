from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, parsers, mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import response, status
from project import project_permissions
from apps.user.models import User, UserImage
from apps.user.serializers import UserSerializer, UserCreateSerializer, UserImageSerializer, UserUpdateSerializer, UserCreateSuperSerializer


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
            "post": UserCreateSerializer,
            "create_super_user": UserCreateSuperSerializer
        }
        return serializer_map.get(self.action, UserSerializer)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(is_superuser=False)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def get_me(self, request):
        user = request.user
        if not user:
            return response.Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], permission_classes=[project_permissions.IsAdmin,])
    def create_super_user(self, request):
        serializer = UserCreateSuperSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
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
            "update": UserImageSerializer,
            "partial_update": UserImageSerializer,
            "create": UserImageSerializer
        }
        return serializer_map.get(self.action, UserImageSerializer)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)