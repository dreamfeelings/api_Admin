from django.db import models

# Create your models here.


"""
创建数据表 class
"""


class root(models.Model):
    user = models.CharField(max_length=16)
    password = models.CharField(max_length=32)


# api 调用情况
class api_call(models.Model):
    id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=200)
    api_url = models.CharField(max_length=200)
    api_method = models.CharField(max_length=200)
    api_create_time = models.DateTimeField(auto_now_add=True)
    # api_status = models.CharField(max_length=200)
    api_UA = models.CharField(max_length=200, default="NONE")
    api_protocol = models.CharField(max_length=200)
    api_ip = models.CharField(max_length=200)
    api_user_id = models.CharField(max_length=200)
    api_question = models.CharField(max_length=200)


# api 存放
class api(models.Model):
    id = models.AutoField(primary_key=True)
    api_class = models.CharField(max_length=200, default="ChatGPT")
    api_name = models.CharField(max_length=200)
    api_en_name = models.CharField(max_length=200, default="NONE")
    api_url = models.CharField(max_length=200)
    api_method = models.CharField(max_length=200)
    api_params = models.CharField(max_length=200, default='NONE')
    api_count = models.IntegerField(default=0)
    api_create_time = models.DateTimeField(auto_now_add=True)
    api_detail = models.CharField(max_length=200, default='NONE')
