from rest_framework.generics import (
    GenericAPIView, CreateAPIView, RetrieveUpdateAPIView, ListAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (
    UserLoginSerializer, TokenSerializer, UserSerializer, TransactionSerializer
)
from rest_framework import status
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
import base64
from .models import ExpiringToken, UserOtp, User, Transaction


# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


class getPhoneNumberRegistered(APIView):
    permission_classes = ()
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            phone = UserOtp.objects.get(phone=phone) #if phone already exists the take this else create New One
        except ObjectDoesNotExist:
            UserOtp.objects.create(
                phone=phone,
            )
            phone = UserOtp.objects.get(phone=phone)  # user Newly created Model
        if phone.isVerified:
            return Response({"response": "Already Registered!"}, status=200)
        else:
            phone.counter += 1  # Update Counter At every Call
            phone.save()  # Save the data
            keygen = generateKey()
            key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
            OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
            print(OTP.at(phone.counter))
            return Response({"OTP": OTP.at(phone.counter)}, status=200)  # Just for now

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            phone = UserOtp.objects.get(phone=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.GET.get('otp'), phone.counter):  # Verifying the OTP
            # phone.isVerified = True
            User.objects.get_or_create(phone=phone.phone)
            user = User.objects.get(phone=phone)
            token, _ = ExpiringToken.objects.get_or_create(user=user)
            phone.save()
            return Response(str(token), status=200)
        return Response("OTP is wrong", status=400)


class UserLoginAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = ExpiringToken.objects.get_or_create(user=user)
            print(type(user))
            if user:
                if token.expired():
                    token.delete()
                    return Response(data="Token expired, Login again",
                                    status=status.HTTP_401_UNAUTHORIZED
                                    )
                else:
                    return Response(
                        data=TokenSerializer(token).data,
                        status=status.HTTP_200_OK,
                    )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_401_UNAUTHORIZED,
            )


class UserUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        queryset = User.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        phone = serializer.data['phone']
        phone = UserOtp.objects.get(phone=phone)
        phone.isVerified = True
        phone.save()
        user = serializer.instance
        user.set_password(request.data['password'])
        user.save()
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class CreditListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.kwargs.get('user'), status="credit")
        return queryset

    def list(self, request, *args, **kwargs):
        total_amt = 0
        queryset = self.filter_queryset(self.get_queryset())
        for query in queryset:
            total_amt += query.amount
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"data":serializer.data, "total_amount": total_amt})


class UsageListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.kwargs.get('user'), status="debit")
        return queryset

    def list(self, request, *args, **kwargs):
        total_amt = 0
        queryset = self.filter_queryset(self.get_queryset())
        for query in queryset:
            total_amt += query.amount
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"data":serializer.data, "total_amount": total_amt})


