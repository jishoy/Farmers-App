from rest_framework.generics import (
    GenericAPIView, CreateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (
    UserLoginSerializer, TokenSerializer, UserRegistrationSerializer
)
from rest_framework import status
from .models import ExpiringToken


class UserRegistrationAPIView(CreateAPIView):

    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance
        user.set_password(request.data['password'])
        user.save()
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = ExpiringToken.objects.get_or_create(user=user)
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
