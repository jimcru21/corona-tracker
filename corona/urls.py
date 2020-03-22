from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('country_stat/<str:pk>', country_stat, name='country_stat'),
]