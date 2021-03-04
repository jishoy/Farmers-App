from django.urls import path
from django.conf.urls import url, include

from .views import (
    FarmAddAPIView, FarmListView, FarmUpdateView, FarmDeleteView, GetFarmView, GeoTagAddAPIView
)

app_name = 'v1apps.farms'

urlpatterns = [
    path('farm/add/', FarmAddAPIView.as_view(), name="farm-add"),
    path('farm/list/<int:pk>/', FarmListView.as_view(), name="farm-list"),
    path('farm/farm-update/<int:pk>/', FarmUpdateView.as_view(), name="farm-update"),
    path('farm/delete/<int:pk>/', FarmDeleteView.as_view(), name="farm-delete"),
    path('farm/farm-view/<int:pk>/', GetFarmView.as_view(), name="farm-view"),
    path('farm/geo-tag/add/', GeoTagAddAPIView.as_view(), name="geo-tag-add")

]
