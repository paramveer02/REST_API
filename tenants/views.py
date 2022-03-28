from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .mixins.views import ActionBasedSerializerModelViewSetMixin
from .models import Tenant
from .serializers import TenantMeModelSerializer, TenantModelSerializer


class TenantModelViewSet(ActionBasedSerializerModelViewSetMixin, ModelViewSet):
    """
    A list/retrieve endpoint that returns all the available tenants by their tenant number and id's,
    rendered in ascending order by their tenant number.
    """

    http_method_names = ["get", "head", "options"]
    lookup_field = "tenant_id"  # Model field used for performing object lookup
    # Serializer and Data Management
    serializer_class = TenantModelSerializer  # Default serializer class
    action_serializer_class = {
        "list": TenantModelSerializer,
        "retrieve": TenantMeModelSerializer,
    }
    # Searching, Ordering and Pagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["tenant_id"]
    ordering_fields = ["tenant_number"]
    pagination_class = PageNumberPagination  # Set to Page_Size=6, defined globally in the settings.py file

    def get_queryset(self):
        tenants = Tenant.objects.all()
        return tenants
