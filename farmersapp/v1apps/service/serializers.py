from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'services', 'remark', 'date', 'status')
        model = Service
