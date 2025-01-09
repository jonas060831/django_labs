from rest_framework import serializers
from .models import Company
from address_api.models import Location
from address_api.serializers import LocationSerializer

class CompanySerializer(serializers.ModelSerializer):

    #include address as a computed field
    address = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'industry', 'address')

    def get_address(self, obj):
        # Retrieve all Location objects where entity_id matches the company ID and entity_type='company'
        locations = Location.objects.filter(entity_id=obj.id, entity_type='company')
        return LocationSerializer(locations, many=True).data if locations.exists() else []
