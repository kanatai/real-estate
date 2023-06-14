from rest_framework import routers

from apps.region.models import Region
from apps.region.views import RegionViewSet

region_router = routers.DefaultRouter()

region_router.register(r'region', viewset=RegionViewSet, basename=Region.__name__)