from rest_framework import routers

from apps.user import views
from apps.user.models import User

user_router = routers.DefaultRouter()
user_router.register(r'users', views.UserViewSet, basename=User.__name__)