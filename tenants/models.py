from django.db import models
from django.utils.translation import gettext_lazy as _


class Tenant(models.Model):
    """
    Tenant model defines the various attributes of a Tenant entity.
    """

    tenant_number = models.AutoField(verbose_name=_("tenant number"), primary_key=True)
    tenant_id = models.CharField(verbose_name=_("tenant id"), max_length=100)
    address = models.CharField(verbose_name=_("tenant address"), max_length=100)
    description = models.CharField(verbose_name=_("tenant description"), max_length=100)

    class Meta:
        verbose_name = _("tenant")
        verbose_name_plural = _("tenants")

    def __str__(self):
        return f"ID: {self.tenant_id}"
