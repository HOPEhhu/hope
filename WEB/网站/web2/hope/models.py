from pyexpat import model
from django.db import models

# Create your models here.
#书
class Book(models.Model):
    # 书名称
    bookname = models.CharField(max_length=200)

    # 作者
    author = models.CharField(max_length=200)

    wordCount = models.CharField(max_length=200,null=True)

    # 日期
    readdata = models.CharField(max_length=200)

    #备注
    remark = models.TextField(null=True)


#日程
class Schedule(models.Model):
    #日期
    scheduledata = models.CharField(max_length=200)

    #内容
    content = models.TextField(null=True)

    #是否完成
    finish = models.BooleanField(null=True)

    #备注
    remark = models.TextField(null=True)



#摘录
class Excerpt(models.Model):
    #内容
    content = models.TextField(null=True)


class Webmark(models.Model):
    #网站名
    webname = models.CharField(max_length=200,null=True)
    weburl = models.CharField(max_length=200,null=True)

