from django.shortcuts import render
from .models import Electric
from django.core.paginator import Paginator
# Create your views here.
def show_Elect(request,num):

#using 指定要使用的数据库
    train_list = Electric.objects.using('train_database').all()
    elect_paginator = Paginator(train_list,3)
    current_elect_page = elect_paginator.page(num)
    path = 'train_data/electric_ss'+'.html'
    total_pages = range(1,elect_paginator.num_pages+1,1)
    for t in total_pages:
        str(t)
    return  render(request,path,{'electrics':current_elect_page,'pages_num':total_pages})