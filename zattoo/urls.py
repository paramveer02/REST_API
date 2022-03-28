from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Zattoo Admin View"
admin.site.index_title = "Admin"
admin.site.site_title = "Zattoo"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tenants.urls")),
]
