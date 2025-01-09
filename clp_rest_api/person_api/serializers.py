from rest_framework import serializers
from .models import Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('id', 'name', 'age', 'company', 'registered_date',)
