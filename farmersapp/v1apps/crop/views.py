from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView,\
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Crop, Seed, Machinery, PesticidesAndFertilizers, Others, BuyRequest, CropImage
from v1apps.user.models import Transaction
from .serializers import CropSerializer, CropSellSerializer, CropImageSerializer, SeedSerializer, MachineSerializer, BuyListSerializer, BuySerializer


class CropAddAPIView(CreateAPIView):

    permission_classes = ()
    serializer_class = CropSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class CropImageAddAPIView(CreateAPIView):

    permission_classes = ()
    serializer_class = CropImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class CropListView(ListAPIView):
    permission_classes = ()
    serializer_class = CropSerializer

    def get_queryset(self):
        queryset = Crop.objects.all()
        return queryset


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
        seed = buy_obj.seed.all()
        machine = buy_obj.machine.all()
        pest_fer = buy_obj.pest_fer.all()
        others = buy_obj.others.all()
        seed_amt = 0
        seed_name = ""
        machine_amt = 0
        machine_name = ""
        pest_fer_amt = 0
        pest_fer_name = ""
        others_amt = 0
        others_name = ""
        for seed in seed:
            seed_amt += seed.price
            seed_name += "," + seed.name

        for machine in machine:
            machine_amt += machine.price
            machine_name += "," + machine.name

        for pest_fer in pest_fer:
            pest_fer_amt += pest_fer.price
            pest_fer_name += "," + pest_fer.name

        for others in others:
            others_amt += others.price
            others_name += "," + others.name

        total_amt = seed_amt + machine_amt + pest_fer_amt + others_amt

        Transaction.objects.create(
                                    user=buy_obj.user,
                                    amount=total_amt,
                                    status="debit",
                                    purpose="Buy " + seed_name + " " + machine_name +
                                            " " + pest_fer_name + " " + others_name
                                  )
        return Response({"data":data, "total amount": total_amt}, status=status.HTTP_201_CREATED)


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