# main/urls.py
from django.urls import path
from main.views import ingfo 

app_name = 'main'

urlpatterns = [
    # bisa menambahkan URL utk views
    path('', ingfo, name='main')
]