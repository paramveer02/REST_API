from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .mixins.views import ActionBasedSerializerModelViewSetMixin
from .models import Tenant
from .serializers import TenantMeModelSerializer, TenantModelSerializer


class TenantModelViewSet(ActionBasedSerializerModelViewSetMixin, ModelViewSet):
    """
    Returns all the available tenants by their number and id's, ordered ascending by their tenant number.
    """

    http_method_names = ["get", "head", "options", "delete"]
    lookup_field = "tenant_id"  # Model field used for performing object lookup
    # Serializer and Data Management
    serializer_class = TenantModelSerializer  # Default serializer class
    action_serializer_class = {
        "list": TenantModelSerializer,
        "retrieve": TenantMeModelSerializer,
    }
    filter_backends = [SearchFilter, OrderingFilter]
    # Searching, Ordering and Pagination
    search_fields = ["tenant_id"]
    ordering_fields = ["tenant_number"]
    pagination_class = PageNumberPagination  # Set to Page_Size=4, defined globally in the settings.py file

    def get_queryset(self):
        tenants = Tenant.objects.all()
        return tenants
