from django.contrib import admin
from django.urls import path
from . import views
from django.urls import re_path #若要在url用正则，则需此包
urlpatterns = [
    re_path(r'train_data/电力机车/(\d+)',views.show_Elect),
    #re_path(r'train_data/内燃机车/(\d+)',views.show_Elect),
    #re_path(r'train_data/蒸汽机车/(\d+)',views.show_Elect),
]