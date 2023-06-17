from rest_framework import routers

from apps.review import views
from apps.review.models import Review

review_router = routers.DefaultRouter()
review_router.register(r'review', views.ReviewViewSet, basename=Review.__name__)