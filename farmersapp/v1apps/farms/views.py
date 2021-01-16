from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView,\
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Farm
from .serializers import FarmSerializer, GeoTagSerializer


class FarmAddAPIView(CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = FarmSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class FarmListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FarmSerializer

    def get_queryset(self):
        queryset = Farm.objects.all()
        return queryset


class FarmUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FarmSerializer

    def get_object(self):
        queryset = Farm.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class FarmDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FarmSerializer

    def get_object(self):
        queryset = Farm.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        self.destroy(serializer)
        return Response("Deleted", status=status.HTTP_200_OK)


class GetFarmView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = FarmSerializer

    def get_object(self):
        queryset = Farm.objects.get(pk=self.kwargs.get('pk'))
        return queryset


class GeoTagAddAPIView(CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = GeoTagSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)
