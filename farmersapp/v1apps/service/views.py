from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView,\
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Service
from .serializers import ServiceSerializer


class ServiceAddAPIView(CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class ServiceHistoryListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.filter(user=self.kwargs.get('user_id'))
        return queryset
