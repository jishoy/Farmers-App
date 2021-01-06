from rest_framework import serializers

from .models import Crop


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
