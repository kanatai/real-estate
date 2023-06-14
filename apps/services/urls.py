from rest_framework import routers

from apps.services.models import Service
from apps.services.views import ServiceViewSet

service_router = routers.DefaultRouter()

service_router.register(r'service', viewset=ServiceViewSet, basename=Service.__name__)