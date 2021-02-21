from django.urls import include, path
from django.contrib import admin
from v1apps.user.admin import base_admin_site

admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "farmers app"

api_urls = [

    path('', include('v1apps.user.urls')),
    path('', include('v1apps.farms.urls')),
    path('', include('v1apps.crop.urls')),
    path('', include('v1apps.service.urls')),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base-admin/', base_admin_site.urls),
    path('api/', include(api_urls)),
]
