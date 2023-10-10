# Author ：梦情
# Time ：2023-10-08 16:33
# File : test_api.py
from django.shortcuts import render


def test_api(request):
    return render(request, 'test_api.html')
