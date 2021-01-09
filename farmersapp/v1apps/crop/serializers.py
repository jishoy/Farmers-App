from rest_framework import serializers

from .models import Crop, Seed, Machinery, Others, PesticidesAndFertilizers, BuyRequest
from v1apps.user.serializers import UserSerializer


class CropSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user.name')
    farm_name = serializers.ReadOnlyField(source='farm.area')

    class Meta:
        fields = ('id', 'crop_name', 'exp_price', 'exp_yield', 'exp_harvest_date',
                  'crop_images', 'user', 'farm', 'user_name', 'farm_name')
        model = Crop


class CropSellSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'sell_flag')
        model = Crop


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


class BuySerializer(serializers.ModelSerializer):
    pest_fer = PesticideAndFertilizerSerializer(read_only=True, many=True)
    seed = SeedSerializer(read_only=True, many=True)
    machine = MachineSerializer(read_only=True, many=True)
    others = OtherSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        fields = ('id', 'user', 'seed', 'machine', 'pest_fer', 'others')
        model = BuyRequest
