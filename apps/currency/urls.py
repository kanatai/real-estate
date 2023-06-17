from rest_framework import routers

from apps.currency import views
from apps.currency.models import Currency

currency_router = routers.DefaultRouter()
currency_router.register(r'currency', views.CurrencyViewSet, basename=Currency.__name__)