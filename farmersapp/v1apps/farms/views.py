from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView,\
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Farm, District, Vilage
from .serializers import FarmSerializer, DistrictSerializer, VillageSerializer


class FarmAddAPIView(CreateAPIView):

    permission_classes = ()
    serializer_class = FarmSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class FarmListView(ListAPIView):
    permission_classes = ()
    serializer_class = FarmSerializer

    def get_queryset(self):
        queryset = Farm.objects.filter(user_id=self.kwargs.get('pk'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response({"status": "false"}, status=status.HTTP_204_NO_CONTENT)
        else:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response({"data": serializer.data, "status": "true"}, status=status.HTTP_200_OK)


class FarmUpdateView(RetrieveUpdateAPIView):
    permission_classes = ()
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
    permission_classes = ()
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

    permission_classes = ()
    serializer_class = FarmSerializer

    def get_object(self):
        queryset = Farm.objects.get(pk=self.kwargs.get('pk'))
        return queryset


class DistrictListView(ListAPIView):
    permission_classes = ()
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response({"status": "false"}, status=status.HTTP_204_NO_CONTENT)
        else:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response({"data": serializer.data, "status": "true"}, status=status.HTTP_200_OK)


class VillageListView(ListAPIView):
    permission_classes = ()
    serializer_class = VillageSerializer

    def get_queryset(self):
        queryset = Vilage.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response({"status": "false"}, status=status.HTTP_204_NO_CONTENT)
        else:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response({"data": serializer.data, "status": "true"}, status=status.HTTP_200_OK)

# class GeoTagAddAPIView(CreateAPIView):
#
#     permission_classes = ()
#     serializer_class = GeoTagSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         data = serializer.data
#         return Response(data, status=status.HTTP_201_CREATED)
