from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import WorkerSerializer
from .models import Worker


# Create your views here.
class WorkerList(generics.ListCreateAPIView):
    queryset = Worker.objects.all().order_by('id')
    serializer_class = WorkerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('query', None)

        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all().order_by('id')
    serializer_class = WorkerSerializer
