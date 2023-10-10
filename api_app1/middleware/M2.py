# Author ：梦情
# Time ：2023-10-10 20:30
# File : M2.py
import re

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class Md1(MiddlewareMixin):
    EXCLUDE_URLS = [
        r'^/api/.*',  # 匹配以/api/开头的所有URL
    ]

    def process_request(self, request):
        print("M1校验")
        # 获取当前请求的URL
        current_url = request.path_info

        # 检查当前URL是否需要校验
        for pattern in self.EXCLUDE_URLS:
            if re.match(pattern, current_url):
                # 如果当前URL匹配排除列表中的任何模式，不执行校验
                return None

        # 获取cookies信息
        info = request.session.get("info")
        # 防止多次重定向
        if request.path_info == '/login/':
            return

        if info:
            return
        return redirect('/login/')

    def process_response(self, request, response):
        print('走了')
        return response

#
# class Md2(MiddlewareMixin):
#     def process_request(self, request):
#         print("M2效验")
#         # return HttpResponse("Md2中断")
#
#     def process_response(self, request, response):
#         print("M2返回")
#         return response
