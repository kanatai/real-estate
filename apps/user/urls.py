from rest_framework import routers

from apps.user import views
from apps.user.models import User, UserImage

user_router = routers.DefaultRouter()
user_router.register(r'users', views.UserViewSet, basename=User.__name__)
user_router.register(r'img/users', views.UserImageViewSet, basename=UserImage.__name__)