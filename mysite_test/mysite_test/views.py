from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def runoob(request):
    context = {}
    context['hello'] = '天街月色凉如水'
    context['views_str'] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    context['num'] = 88
    return render(request, 'runoob.html', context)
