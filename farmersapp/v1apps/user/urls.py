from django.urls import path
from .views import (
    UserLoginAPIView, getPhoneNumberRegistered, UserUpdateView
)

app_name = 'v1apps.user'

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('users/user-update/<int:pk>', UserUpdateView.as_view(), name="user-update"),
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
]
