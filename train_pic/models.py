from django.db import models
from django.shortcuts import render
from  django.conf import settings

# Create your models here.
class Web_text(models.Model):
    Wid = models.AutoField(primary_key=True)
    Wtext = models.TextField(default="cong's forum")
    WFloorCount = models.CharField(max_length=1000,default='null')

    class Meta:
        app_label = 'train_pic'

def  individualPath(instance,filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.WpicName), filename])

class Web_pic(models.Model):
    Wid = models.AutoField(primary_key=True)
    Wpic = models.ImageField(upload_to=individualPath,default='null')
    WpicRange = models.ForeignKey('Web_Range',to_field='WRanName',on_delete=models.CASCADE)
    WpicName = models.CharField(max_length=100,default='none')
    class Meta:
        app_label = 'train_pic'


class Web_Range(models.Model):
    Wid = models.AutoField(primary_key=True)
    WRanName = models.CharField(max_length=100,default='null',unique=True)
    WRanNum = models.IntegerField(default=0)
    WRanPath = models.CharField(max_length=300,default='null')
    class Meta:
        app_label = 'train_pic'




