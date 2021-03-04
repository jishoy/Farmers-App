from django.http import JsonResponse
from django.db.models import Sum
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, \
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Crop, Seed, Machinery, PesticidesAndFertilizers, Others, BuyRequest
from v1apps.user.models import Transaction
from .serializers import CropListSerializer, CropSerializer, CropSellSerializer, CropActivitySerializer, SeedSerializer, MachineSerializer, \
    BuyListSerializer, BuySerializer


class CropAddAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CropSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class CropActivityAddAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CropActivitySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class CropListActivityView(ListAPIView):
    permission_classes = ()
    serializer_class = CropSerializer

    def get_queryset(self):
        queryset = Crop.objects.filter(user=self.kwargs.get('pk'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data, "status": "200"}, status=status.HTTP_200_OK)


class CropListView(ListAPIView):
    permission_classes = ()
    serializer_class = CropListSerializer

    def get_queryset(self):
        queryset = Crop.objects.filter(user=self.kwargs.get('pk'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data, "status": "true"}, status=status.HTTP_200_OK)


class CropUpdateView(RetrieveUpdateAPIView):
    permission_classes = ()
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
    permission_classes = ()
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
    permission_classes = ()
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
    permission_classes = ()
    serializer_class = CropSerializer

    def get_object(self):
        queryset = Crop.objects.get(pk=self.kwargs.get('pk'))
        return queryset


class SeedListView(ListAPIView):
    permission_classes = ()
    serializer_class = SeedSerializer

    def get_queryset(self):
        queryset = Seed.objects.all()
        return queryset


class MachineListView(ListAPIView):
    permission_classes = ()
    serializer_class = MachineSerializer

    def get_queryset(self):
        queryset = Machinery.objects.all()
        return queryset


class OtherListView(ListAPIView):
    permission_classes = ()
    serializer_class = MachineSerializer

    def get_queryset(self):
        queryset = Others.objects.all()
        return queryset


class PesticideAndFertilizerListView(ListAPIView):
    permission_classes = ()
    serializer_class = PesticidesAndFertilizers

    def get_queryset(self):
        queryset = PesticidesAndFertilizers.objects.all()
        return queryset


class BuyAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = BuySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        buy_id = serializer.data['id']
        buy_obj = BuyRequest.objects.get(id=buy_id)

        seed_name = [name for name in buy_obj.seed.values_list('name', flat=True)]
        machine_name = [name for name in buy_obj.machine.values_list('name', flat=True)]
        pest_fer_name = [name for name in buy_obj.pest_fer.values_list('name', flat=True)]
        others_name = [name for name in buy_obj.others.values_list('name', flat=True)]
        seed_amt = buy_obj.seed.aggregate(Sum('price'))['price__sum']
        machine_amt = buy_obj.machine.aggregate(Sum('price'))['price__sum']
        pest_fer_amt = buy_obj.pest_fer.aggregate(Sum('price'))['price__sum']
        others_amt = buy_obj.others.aggregate(Sum('price'))['price__sum']

        total_amt = seed_amt + machine_amt + pest_fer_amt + others_amt
        purpose = ','.join(seed_name + machine_name + pest_fer_name + others_name)

        Transaction.objects.create(
            user=buy_obj.user,
            amount=total_amt,
            status="debit",
            purpose="Buy " + purpose
        )
        return Response({"data": data, "total amount": total_amt}, status=status.HTTP_201_CREATED)


class RequestHistoryListView(ListAPIView):
    permission_classes = ()
    serializer_class = BuyListSerializer

    def get_queryset(self):
        queryset = BuyRequest.objects.filter(user=self.kwargs.get('user_id'))
        return queryset


class CropSellAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = CropSellSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)
