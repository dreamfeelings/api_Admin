# Author ：梦情
# Time ：2023-10-07 14:12
# File : ChatGPT.py
import requests
from django.shortcuts import HttpResponse

from api_app1.models import api_call, api


def ChatGPT(request):
    question = request.GET.get('question')
    sequence = request.GET.get('sequence')
    # 将第sequence个ChatGPT的count加一
    url = api.objects.filter(api_name="ChatGPT").values('api_url')[int(sequence) - 1]['api_url']
    api.objects.filter(api_url=url).update(
        api_count=api.objects.filter(api_url=url).values('api_count')[0]['api_count'] + 1)

    # 将调用情况存放到api_call
    api_call.objects.create(api_name="ChatGPT", api_url=url, api_method=request.method,
                            api_protocol=request.META.get('SERVER_PROTOCOL', ''),
                            api_ip=request.META['REMOTE_ADDR'], api_user_id="1", api_question=question,
                            api_UA=request.META['HTTP_USER_AGENT'])

    # 调用openai接口
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    }
    data = {"model": {"id": "gpt-3.5-turbo", "name": "GPT-3.5", "maxLength": 12000, "tokenLimit": 4000},
            "messages": [{"role": "user", "content": question}], "key": "",
            "prompt": "You are ChatGPT, a large language model trained by OpenAI. Follow the user\'s instructions carefully. Respond using markdown.",
            "temperature": 1}
    requests.packages.urllib3.disable_warnings()

    response = requests.post(url, headers=headers, json=data, verify=False).text

    return HttpResponse(response)
