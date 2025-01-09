from django.urls import path
from . import views

urlpatterns = [
    path('api/workers', views.WorkerList.as_view(), name='worker_list'),
    path('api/workers/<uuid:pk>', views.WorkerDetail.as_view(), name='worker_detail')
]
