from django.urls import path

from . import views

app_name = 'myApp'

urlpatterns = [
    path('', views.index, name='index'),
]
