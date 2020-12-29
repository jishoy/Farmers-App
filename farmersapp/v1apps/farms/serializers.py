from rest_framework import serializers

from .models import Farm


class FarmSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user_id.name')

    class Meta:
        fields = ('id', 'area', 'village', 'district', 'whether',
                  'user_id', 'user_name')

        model = Farm
