from django.urls import path
from corona.views import *

urlpatterns = [
    path('', index, name='index'),
]
