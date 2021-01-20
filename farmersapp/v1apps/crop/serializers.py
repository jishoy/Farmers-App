from rest_framework import serializers
from rest_framework.response import Response

from .models import Crop, Seed, Machinery, Others, PesticidesAndFertilizers, BuyRequest, CropImage, CropSell
from v1apps.user.serializers import UserSerializer


class CropSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user.name')
    farm_name = serializers.ReadOnlyField(source='farm.area')

    class Meta:
        fields = ('id', 'crop_name', 'exp_price', 'exp_yield', 'exp_harvest_date',
                  'user', 'farm', 'user_name', 'farm_name', 'activity')
        model = Crop


class CropImageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'crops', 'images')
        model = CropImage


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
