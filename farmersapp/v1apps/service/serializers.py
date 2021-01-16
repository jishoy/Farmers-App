from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.name')

    class Meta:
        fields = ('id', 'services', 'remark', 'user',)
        model = Service
