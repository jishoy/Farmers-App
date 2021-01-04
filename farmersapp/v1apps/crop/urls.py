from django.urls import path

from .views import (
    CropAddAPIView, CropListView, CropUpdateView, CropDeleteView, GetCropView, CropSellView
)

app_name = 'v1apps.crop'

urlpatterns = [
    path('crop/add/', CropAddAPIView.as_view(), name="crop-add"),
    path('crop/list/', CropListView.as_view(), name="crop-list"),
    path('crop/crop-update/<int:pk>', CropUpdateView.as_view(), name="crop-update"),
    path('crop/crop-sell/<int:pk>', CropSellView.as_view(), name="crop-sell"),
    path('crop/delete/<int:pk>/', CropDeleteView.as_view(), name="crop-delete"),
    path('crop/crop-view/<int:pk>/', GetCropView.as_view(), name="crop-view"),
]
