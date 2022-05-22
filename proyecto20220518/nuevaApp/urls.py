from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('proyecto20220518/', include('proyecto20220518.urls')),
  

]


