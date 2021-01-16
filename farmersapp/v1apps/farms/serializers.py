from rest_framework import serializers

from .models import Farm, GeoTag


class FarmSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user_id.name')

    class Meta:
        fields = ('id', 'area', 'village', 'district', 'whether',
                  'user_id', 'user_name')
        model = Farm


class GeoTagSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user.name')
    farm_name = serializers.ReadOnlyField(source='farm.area')

    class Meta:
        fields = ('id', 'user', 'user_name', 'farm', 'farm_name', 'loc_lat_long')
        model = GeoTag
