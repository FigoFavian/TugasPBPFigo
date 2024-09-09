# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # bisa menambahkan URL utk views
    path('', views.app_info, name='home'),
    path('app-info/', views.app_info, name='app_info'),
]