from django.db import models
import mongoengine
# Create your models here.

class userInfo(mongoengine.Document):
    username = mongoengine.StringField(max_length=20,verbose_name='用户名')
    nickname = mongoengine.StringField(max_length=20, verbose_name='昵称')
    password = mongoengine.StringField(max_length=20, verbose_name='密码')

class article(mongoengine.Document):
    aid = mongoengine.StringField(max_length=20,verbose_name='编号')
    title = mongoengine.StringField(max_length=20,verbose_name='标题')
    content = mongoengine.StringField(verbose_name='内容')
    img_url = mongoengine.StringField(max_length=50,verbose_name='图片')
    time = mongoengine.DateTimeField(verbose_name='发表日期')

class dynamic(mongoengine.Document):
    aid = mongoengine.IntField(max_length=20,verbose_name='编号')
    content = mongoengine.StringField(verbose_name='内容')
    time = mongoengine.DateTimeField(verbose_name='发表日期')





