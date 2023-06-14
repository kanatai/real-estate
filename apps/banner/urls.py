from rest_framework.routers import DefaultRouter

from apps.banner.models import Banner
from apps.banner.views import BannerViewSet

banner_router = DefaultRouter()
banner_router.register(r'banner', BannerViewSet, basename=Banner.__name__)