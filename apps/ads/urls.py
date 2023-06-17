from rest_framework import routers

from apps.ads import views
from apps.ads.models import Ads

ads_router = routers.DefaultRouter()
ads_router.register(r'ads', views.AdsViewSet, basename=Ads.__name__)