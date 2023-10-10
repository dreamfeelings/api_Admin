# Author ：梦情
# Time ：2023-10-07 19:10
# File : tk.py
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api_app1.models import api_call, api


@csrf_exempt
def tk(request):
    question = request.GET.get('question')
    type = request.GET.get('type')
    url = api.objects.filter(api_en_name=type).values('api_url')[0]['api_url']
    name = api.objects.filter(api_en_name=type).values('api_name')[0]['api_name']
    api.objects.filter(api_url=url).update(
        api_count=api.objects.filter(api_url=url).values('api_count')[0]['api_count'] + 1)
    api_call.objects.create(api_name=name, api_url=url, api_method=request.method,
                            api_protocol=request.META.get('SERVER_PROTOCOL', ''),
                            api_ip=request.META['REMOTE_ADDR'], api_user_id="1", api_question=question,
                            api_UA=request.META['HTTP_USER_AGENT'])

    answer = requests.post(url, json={"question": question}).json()
    print(answer)

    return JsonResponse(answer)
