from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def index(request):
    return render(request,'train_pic/index.html')

def tielusheying(request):
    return render(request,'train_pic/main_src/tielusheying.html')
    #return  HttpResponse('haha')

def fengjingsheying(request):
    return  render(request,'train_pic/main_src/fengjingsheying.html')

def sanmenxiafenglingdu(request,num):
    path = 'train_pic/main_src/huoche/sanmenxia_fenglingdu/sanmenxia_fenglingdu' + str(num) + '.html'
    return render(request, path)