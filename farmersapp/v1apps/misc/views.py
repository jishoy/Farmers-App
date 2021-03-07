from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, \
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

from .serializers import FarmSerializer, CropSerializer, TransactionSerializer
from v1apps.user.models import Transaction, User
from v1apps.crop.models import Crop
from v1apps.farms.models import Farm
from rest_framework import viewsets
import requests


class HomeView(ListAPIView):
    permission_classes = ()
    serializer_class_Farm = FarmSerializer
    serializer_class_Crop = CropSerializer
    serializer_class_Transaction = TransactionSerializer

    def get_queryset_Farm(self):
        return Farm.objects.filter(user_id=self.kwargs.get('pk'))

    def get_queryset_Crop(self):
        return Crop.objects.filter(user=self.kwargs.get('pk'))

    def get_queryset_Transaction(self):
        return Transaction.objects.filter(user=self.kwargs.get('pk'))

    def total(self):
        return Transaction.objects.filter(user=self.kwargs.get('pk'), status='credit').aggregate(Sum('amount'))['amount__sum']

    def weather_details(self):
        city = self.request.GET.get('city')
        api_token = self.request.GET.get('api_token')
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_token}")
        return r.json()

    def list(self, request, *args, **kwargs):
        farm_queryset = self.get_queryset_Crop()
        crop_queryset = self.get_queryset_Farm()
        transaction_queryset = self.get_queryset_Transaction()
        farm = self.serializer_class_Crop(farm_queryset, many=True)
        crop = self.serializer_class_Farm(crop_queryset, many=True)
        transaction = self.serializer_class_Transaction(transaction_queryset, many=True)

        if farm_queryset or crop_queryset or transaction_queryset:
            return Response({
                "status": "true",
                "weather_details": self.weather_details(),
                "farms": crop.data,
                "crops": farm.data,
                "transactions": transaction.data,
                "total_amount_received": self.total()
            })
        else:
            return Response({
                "status": "false"
            })
