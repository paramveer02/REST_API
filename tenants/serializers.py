from rest_framework import serializers

from .models import Tenant


class TenantModelSerializer(serializers.ModelSerializer):
    """
    A serializer for the :py:class:`tenants.Tenant` model. Used whenever the tenant number and id is needed.
    """

    class Meta:
        model = Tenant
        fields = ("tenant_number", "tenant_id")


class TenantMeModelSerializer(serializers.ModelSerializer):
    """
    A serializer for the :py:class:tenants.Tenant` model. Used whenever the information of a tenant is required,
    accessible via it's tenant_id.
    """

    class Meta:
        model = Tenant
        fields = ("address", "description")
