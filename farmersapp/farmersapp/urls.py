from django.urls import include, path
from django.contrib import admin


api_urls = [

    path('', include('v1apps.user.urls')),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
