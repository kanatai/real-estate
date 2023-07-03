from rest_framework.routers import DefaultRouter

from apps.banner.models import Banner, BannerImage
from apps.banner.views import BannerViewSet, BannerImageViewSet

banner_router = DefaultRouter()
banner_router.register(r'banner', BannerViewSet, basename=Banner.__name__)
banner_router.register(r'img/banner', BannerImageViewSet, basename=BannerImage.__name__)