# Author ：梦情
# Time ：2023-10-07 0:38
# File : login.py
from django.shortcuts import render, redirect


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "mqmrx" and password == "mq123456789":
            print("登录成功")
            request.session["info"] = {"username": username}
            return redirect("/")
        else:
            print("登录失败")
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})
