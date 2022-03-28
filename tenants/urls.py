from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TenantModelViewSet

router = DefaultRouter()
router.register("tenants", TenantModelViewSet, basename="tenant-users")

urlpatterns = [
    path("", include(router.urls)),
]
