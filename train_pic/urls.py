from django.contrib import admin
from django.urls import path
from . import views
from django.urls import re_path #若要在url用正则，则需此包
urlpatterns = [
    path(r'',views.index),
    path(r'tielusheying',views.tielusheying),
    path(r'fengjingsheying',views.fengjingsheying),
    re_path(r'tielusheying/sanmenxiafenglingdu(\d+)',views.sanmenxiafenglingdu),
]