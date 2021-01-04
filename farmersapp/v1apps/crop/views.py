from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView,\
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Crop
from .serializers import CropSerializer, CropSellSerializer


class CropAddAPIView(CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = CropSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance
        user.save()
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class CropListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CropSerializer

    def get_queryset(self):
        queryset = Crop.objects.all()
        return queryset


class CropUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CropSerializer

    def get_object(self):
        queryset = Crop.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class CropSellView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CropSellSerializer

    def get_object(self):
        queryset = Crop.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class CropDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CropSerializer

    def get_object(self):
        queryset = Crop.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        self.destroy(serializer)
        return Response("Deleted", status=status.HTTP_200_OK)


class GetCropView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = CropSerializer

    def get_object(self):
        queryset = Crop.objects.get(pk=self.kwargs.get('pk'))
        return queryset
