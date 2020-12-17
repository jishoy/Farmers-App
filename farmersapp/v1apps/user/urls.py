from django.urls import path
from .views import (
    UserLoginAPIView, UserRegistrationAPIView
)

app_name = 'v1apps.user'

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('users/user-creation/', UserRegistrationAPIView.as_view(), name="user-creation"),
]
