from rest_framework import routers

from apps.favorite.models import Favorite
from apps.favorite.views import FavoriteViewSet

favorite_router = routers.DefaultRouter()

favorite_router.register(r'favorite', viewset=FavoriteViewSet, basename=Favorite.__name__)