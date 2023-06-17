from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework.viewsets import ModelViewSet

from apps.review.models import Review
from apps.review.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {
        'created_at': ['gte', 'lte'],
    }
    search_fields = ['fullname']

    def list(self, request, *args, **kwargs):
        """
        Это отзывы
        """
        super().list(self, request, *args, **kwargs)

    def get_queryset(self):
        return Review.objects.all()

    def get_serializer_class(self):
        return ReviewSerializer