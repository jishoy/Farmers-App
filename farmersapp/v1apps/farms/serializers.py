from rest_framework import serializers

from .models import Farm, District, Vilage


class FarmSerializer(serializers.ModelSerializer):

    # geo = serializers.ReadOnlyField(source='geo.loc_lat_long')

    class Meta:
        fields = ('id', 'name', 'village', 'district', 'acres',
                  'soil_health', 'geo')
        model = Farm


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'code')
        model = District


class VillageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name')
        model = Vilage


# class GeoTagSerializer(serializers.ModelSerializer):
#
#     user_name = serializers.ReadOnlyField(source='user.name')
#     farm_name = serializers.ReadOnlyField(source='farm.area')
#
#     class Meta:
#         fields = ('id', 'user', 'user_name', 'farm', 'farm_name', 'loc_lat_long')
#         model = GeoTag
