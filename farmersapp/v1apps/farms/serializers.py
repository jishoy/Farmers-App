from rest_framework import serializers

from .models import Farm, GeoTag


class FarmSerializer(serializers.ModelSerializer):

    geo = serializers.ReadOnlyField(source='geo.loc_lat_long')

    class Meta:
        fields = ('id', 'name', 'village', 'district', 'acres',
                  'soil_health', 'geo')
        model = Farm


class GeoTagSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user.name')
    farm_name = serializers.ReadOnlyField(source='farm.area')

    class Meta:
        fields = ('id', 'user', 'user_name', 'farm', 'farm_name', 'loc_lat_long')
        model = GeoTag
