# Author ：梦情
# Time ：2023-10-07 15:48
# File : add_api.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from api_app1.models import api


@csrf_protect
def add_api(request):
    if request.method == "GET":
        return render(request, "add_api.html")

    api_class = request.POST.get("api_class")
    api_name = request.POST.get("api_name")
    api_en_name = request.POST.get("api_en_name")
    api_url = request.POST.get("api_url")
    api_method = request.POST.get("api_method")
    api_params = request.POST.get("api_params")
    api_detail = request.POST.get("api_detail")
    # print(api_name, api_url, api_method, api_params, api_detail,sep="\n")
    api.objects.create(api_class=api_class, api_name=api_name, api_en_name=api_en_name, api_url=api_url,
                       api_method=api_method, api_params=api_params,
                       api_detail=api_detail)

    return JsonResponse({"status": 200, "message": "添加成功"})
