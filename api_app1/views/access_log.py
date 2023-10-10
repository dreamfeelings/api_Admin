# Author ：梦情
# Time ：2023-10-08 16:00
# File : access_log.py
from django.shortcuts import render

from api_app1.models import api_call


def access_log(request):
    # 获取所有的api调用情况
    api_call_list = api_call.objects.all().order_by('-api_create_time')
    return render(request, 'access_log.html', {'api_call_list': api_call_list})
