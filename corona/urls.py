from django.urls import path

from corona import views

urlpatterns = [
    path('', views.index, name='index'),
]
