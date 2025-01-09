from django.urls import path
from . import views

urlpatterns = [
    path('api/addresses', views.LocationList.as_view(), name='location_list'),
    path('api/addresses/<int:pk>', views.LocationDetail.as_view(), name='location_detail')
]
