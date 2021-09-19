from xml.etree.ElementInclude import include

from django.urls import path

from . import views, admin

urlpatterns = [
    path('', views.index, name='index'),
]