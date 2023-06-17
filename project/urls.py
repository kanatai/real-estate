import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.banner.urls import banner_router
from apps.favorite.urls import favorite_router
from apps.user.urls import user_router
from apps.apartments.urls import apartment_router
from apps.region.urls import region_router
from apps.services.urls import service_router
from apps.ads.urls import ads_router
from apps.currency.urls import currency_router
from apps.review.urls import review_router

from project import settings

router = routers.DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(apartment_router.registry)
router.registry.extend(favorite_router.registry)
router.registry.extend(region_router.registry)
router.registry.extend(service_router.registry)
router.registry.extend(banner_router.registry)
router.registry.extend(ads_router.registry)
router.registry.extend(currency_router.registry)
router.registry.extend(review_router.registry)

urlpatterns = [
    path('dashboard/', admin.site.urls),
    # custom_jwt auth
    path('api/token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]

# swagger and redoc
if os.environ.get('env') != 'prod':
    schema_view = get_schema_view(
        openapi.Info(
            title="Real-Estate API",
            default_version='v1',
            description="Real-Estate Python API",
            terms_of_service="",
            contact=openapi.Contact(email="123kanatai@gmail.com"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )
    urlpatterns = urlpatterns + [
        path(r'api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path(r'api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
