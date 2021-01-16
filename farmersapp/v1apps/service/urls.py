from django.urls import path
from django.conf.urls import url, include

from .views import ServiceAddAPIView, ServiceHistoryListView

app_name = 'v1apps.service'

urlpatterns = [
    path('service/request/', ServiceAddAPIView.as_view(), name="service-request"),
    path('service/service-history/<int:user_id>/', ServiceHistoryListView.as_view(), name="service-histry"),
]
