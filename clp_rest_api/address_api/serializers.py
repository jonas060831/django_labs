from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('entity_id', 'street', 'city', 'state', 'longitude', 'latitude', 'entity_type',)
