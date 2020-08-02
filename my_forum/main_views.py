from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from train_pic.models import Web_text,Web_pic,Web_Range
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.paginator import Paginator
from django.conf import settings

import json
import datetime
def main_page(request):
    return render(request,'main_page.html')

#首页重定向
def BaiduMapRaw(request):
    return HttpResponseRedirect(request.path + '1')

def BaiduMap(request,pageId):
    WtList = Web_text.objects.all()
    #一共要创建多少个div/内容
    WtListCount = len(WtList)
    Wjson = serializers.serialize("json", WtList)
    load = request.POST.get('load')
    #直接通过ajax post的 abc=aaa & bs = bbb 的方式获得键值
    #t = request.POST.get('text')
    #id = request.POST.get('id')

    #每页显示多少个div
    divP = 5

    #获取post发出的load初始化字符串
    if load == 'yes':
        #return HttpResponse(Wjson)
        pg = Paginator(WtList,divP)
        #返回一个Page对象
        pgObj = pg.page(pageId)
        pgContent = pgObj.object_list
        pCJSON = serializers.serialize('json',pgContent)
        return HttpResponse(pCJSON)
    else:
        raw_data = request.body
        if raw_data:
            try:
                #从request.body得到的数据为byte型，必须先解码成utf-8
                raw_dataStr = raw_data.decode('utf-8')
                j = json.loads(raw_dataStr)
                #获取数据库表单
                Wt = Web_text()
                Wt.Wtext=j['text']
                Wt.WFloorCount = str(j['id'])
                Wt.save()
                #return HttpResponse(j['id'])
                return HttpResponse(raw_dataStr)
            except Exception as e:
                return  HttpResponse(e)
            #objData = json.loads(raw_data)
            #s2 = objData['text']
            return HttpResponse(str(objData))
        else:
            pg = Paginator(WtList,divP)
            pgObj = pg.page(pageId)
            #获取页码范围
            num = pgObj.paginator.page_range
            return render(request, 'Baidumap.html',{'page':num})
    #return HttpResponse('aa')

def upLoadImg(request):
    #查看img 的类型，显示为class 'django.core.files.uploadedfile.InMemoryUploadedFile'
    #上传多个文件用getlist()
    imgs = request.FILES.getlist('imgs')
    count = len(imgs)
    data = []
    for img in imgs:
        Wp = Web_pic()
        #默认数据库的upload_to会将图片存储在/media/下
        fkey = Web_Range.objects.get(Wid=1);
        Wp.WpicRange = fkey
        Wp.WpicName = 'df4b'
        Wp.Wpic = img
        data.append('/'.join(['/media', Wp.WpicName, img.name]))
        Wp.save()
    list = [('errno',0),('data',data)]
    list = dict(list)
    list = json.dumps(list)
    return  HttpResponse(list)
