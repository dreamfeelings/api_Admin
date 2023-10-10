"""
URL configuration for API_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from api_app1.api_views import ChatGPT, tk
from api_app1.views import login, index, add_api, access_log, test_api

urlpatterns = [
    path("login/", login.login),
    path("", index.index),
    path("api/ChatGPT/", ChatGPT.ChatGPT),
    path("add_api/", add_api.add_api),
    path("api/tk/", tk.tk),
    path("access_log/", access_log.access_log),
    path("test_api/", test_api.test_api),
]
