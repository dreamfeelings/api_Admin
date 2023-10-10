# Author ：梦情
# Time ：2023-10-07 1:03
# File : index.py
from django.shortcuts import render

from api_app1.models import api


def index(request):
    # urls = requests.get("http://gptjk.mqmrx.cn/api/get_gpt").json()['data']
    # # 插入数据到api
    # for url in urls:
    #     api.objects.create(api_name="ChatGPT", api_en_name="ChatGPT", api_params="question=(str)&sequence=(int)",
    #                        api_url=url, api_method="GET",
    #                        api_detail="调用openai接口")
    api_data = api.objects.all()

    # 使用 .values() 和 .distinct() 获取唯一的 api_name
    unique_api_names = api.objects.values('api_class').distinct()
    api_class_list = [item['api_class'] for item in unique_api_names]
    host = request.get_host()
    return render(request, "index.html",
                  {"api_data": api_data, "api_class_list": api_class_list, "host": host})
