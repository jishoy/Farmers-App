from rest_framework import serializers
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Crop, Seed, Machinery, Others, PesticidesAndFertilizers, BuyRequest, CropSell, CropActivity
from v1apps.user.serializers import UserSerializer


class CropActivitySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'crops', 'activity', 'images')
        model = CropActivity


class CropSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user.name')
    farm_name = serializers.ReadOnlyField(source='farm.area')
    activities = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'crop_name', 'exp_price', 'exp_yield', 'exp_harvest_date',
                  'user', 'farm', 'user_name', 'farm_name', 'crop_image', 'activities')
        model = Crop

    def get_activities(self, obj):
        activities_queryset = CropActivity.objects.filter(crops=obj)
        return CropActivitySerializer(activities_queryset, many=True).data


class CropSellSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'crops', 'user')
        model = CropSell


class SeedSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'brand', 'name', 'category', 'variety',
                  'price')

        model = Seed


class MachineSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'brand', 'name', 'category', 'price')
        model = Machinery


class OtherSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'brand', 'name', 'category', 'price')
        model = Others


class PesticideAndFertilizerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'brand', 'name', 'category', 'price')
        model = PesticidesAndFertilizers


class BuyListSerializer(serializers.ModelSerializer):
    pest_fer = PesticideAndFertilizerSerializer(read_only=True, many=True)
    seed = SeedSerializer(read_only=True, many=True)
    machine = MachineSerializer(read_only=True, many=True)
    others = OtherSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        fields = ('id', 'user', 'seed', 'machine', 'pest_fer', 'others')
        model = BuyRequest


class BuySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user', 'seed', 'machine', 'pest_fer', 'others')
        model = BuyRequest
