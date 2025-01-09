from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import CompanySerializer
from .models import Company
# Create your views here.



#/companies POST,GET,
#/companies?query=company_name OR industry WHERE company name & industry is case insensitive
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('query', None)

        if query:
            queryset = queryset.filter(name__icontains=query) | queryset.filter(industry__icontains=query) #query values of name or industry
        return queryset

#/companies/:id
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer
