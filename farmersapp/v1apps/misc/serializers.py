from rest_framework import serializers

from v1apps.user.models import Transaction, User
from v1apps.crop.models import Crop
from v1apps.farms.models import Farm


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'crop_name', 'harvest_days', 'acres', 'crop_image')
        model = Crop


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('trans_id', "date_of_transaction", "amount", 'title')


class FarmSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'soil_health')
        model = Farm

