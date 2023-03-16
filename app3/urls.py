from django.urls import path
from app3.views import *

app_name ='app3'

urlpatterns =[
    path('app3/',app3,name='app3'),
]