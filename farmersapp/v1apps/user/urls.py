from django.urls import path
from .views import (
    UserLoginAPIView, getPhoneNumberRegistered, UserUpdateView, CreditListView, UsageListView
)

app_name = 'v1apps.user'

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('users/user-update/<int:pk>', UserUpdateView.as_view(), name="user-update"),
    path('users/credit-history/<int:user>', CreditListView.as_view(), name="user-credit-history"),
    path('users/usage-history/<int:user>', UsageListView.as_view(), name="user-usage-history"),
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
]
