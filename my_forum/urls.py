"""my_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from train_pic import views
from django.conf import settings
from django.conf.urls.static import static
from . import main_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cong/',include('train_pic.urls')),
    path('cong1/',include('mix_forum.urls')),
    path('',main_views.main_page),
    #(d+)作为参数可传到views函数上
    path('map/',main_views.BaiduMapRaw),
    re_path('map/(\d+)$',main_views.BaiduMap),
    path('img/',main_views.upLoadImg),
]
#必须设置media文件夹的静态路径才能访问其下的图片
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
