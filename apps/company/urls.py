from rest_framework.routers import DefaultRouter

from apps.company.models import Company, CompanyImage
from apps.company.views import CompanyViewSet, CompanyImageViewSet

company_router = DefaultRouter()
company_router.register(r'company', CompanyViewSet, basename=Company.__name__)
company_router.register(r'img/company', CompanyImageViewSet, basename=CompanyImage.__name__)