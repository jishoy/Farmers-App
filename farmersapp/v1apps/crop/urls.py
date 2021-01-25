from django.urls import path

from .views import (
    CropAddAPIView, CropListView, CropUpdateView, CropDeleteView, GetCropView, CropSellView,
    SeedListView, MachineListView, OtherListView, PesticideAndFertilizerListView, BuyAPIView,
    RequestHistoryListView, CropSellAPIView, CropActivityAddAPIView
)

app_name = 'v1apps.crop'

urlpatterns = [
    path('crop/add/', CropAddAPIView.as_view(), name="crop-add"),
    path('crop/activity-add/', CropActivityAddAPIView.as_view(), name="crop-add-activity"),
    path('crop/list/<int:pk>/', CropListView.as_view(), name="crop-list"),
    path('crop/crop-update/<int:pk>', CropUpdateView.as_view(), name="crop-update"),
    path('crop/crop-sell/', CropSellAPIView.as_view(), name="crop-sell"),
    path('crop/delete/<int:pk>/', CropDeleteView.as_view(), name="crop-delete"),
    path('crop/crop-view/<int:pk>/', GetCropView.as_view(), name="crop-view"),
    path('seed/list/', SeedListView.as_view(), name="seed-list"),
    path('machine/list/', MachineListView.as_view(), name="machine-list"),
    path('others/list/', OtherListView.as_view(), name="others-list"),
    path('pesticides-fertilizers/list/', PesticideAndFertilizerListView.as_view(), name="pesticides-fertilizers-list"),
    path('buy/request/', BuyAPIView.as_view(), name="buy-request"),
    path('buy/request-history/<int:user_id>/', RequestHistoryListView.as_view(), name="buy-request-histry"),
]
