from django.urls import path

from .views import HomeView

app_name = 'v1apps.misc'

urlpatterns = [
    path('misc/home/<int:pk>/', HomeView.as_view(), name="farm-list"),
]
