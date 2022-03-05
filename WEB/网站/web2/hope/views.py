
# -*- coding: utf-8 -*-
from distutils.log import error
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from hope.models import Excerpt, Schedule
from hope.models import Book
from django.contrib.auth import authenticate, login, logout
import os
import mammoth
# Create your views here.

"""def schedule(request):
    qs = Schedule.objects.values()
    retStr = ''
    for schedule in  qs:
        for name,value in schedule.items():
            retStr += f'{name} : {value} | '
        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)
    """
""""""


def schedule(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_schedule':
        return listschedule(request)
    elif action == 'add_schedule':
        return addschedule(request)
    elif action == 'check_schedule':
        return checkschedule(request)
    elif action == 'del_schedule':
        return delschedule(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listschedule(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Schedule.objects.values()
    ph = request.params['time']
    print(ph)
    if ph:
        qs = qs.filter(scheduledata=ph)

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addschedule(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['data']
    record = Schedule.objects.create(
        scheduledata=info['time'], content=info['content'], finish=False)
    return JsonResponse({'ret': 0, 'id': record.id})


def checkschedule(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    info = request.params['data']

    try:
        todo = Schedule.objects.get(id=info["id"])
    except Schedule.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })

    todo.finish = bool(1-todo.finish)

    # 注意，一定要执行save才能将修改信息保存到数据库
    todo.save()

    return JsonResponse({'ret': 0})


def delschedule(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    info = request.params['data']

    try:
        todo = Schedule.objects.get(id=info["id"])
    except Schedule.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })
    todo.delete()
    return JsonResponse({'ret': 0})


def book(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET
    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_book':
        return listbook(request)
    elif action == 'add_book':
        return addbook(request)
    elif action == 'modify_book':
        return modifybook(request)
    elif action == 'del_book':
        return delbook(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listbook(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Book.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addbook(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Book.objects.create(bookname=info['bookname'],
                                 author=info['author'],
                                 readdata=info['readdata'],
                                 wordCount=info['wordcount'],
                                 remark=info['remark'])

    return JsonResponse({'ret': 0, 'id': record.id})


def modifybook(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    bookid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        book = Book.objects.get(id=bookid)
    except Book.DoesNotExist:
        return {
            'ret': 1,
        }
    if 'bookname' in newdata:
        book.bookname = newdata['bookname']
    if 'author' in newdata:
        book.author = newdata['author']
    if 'readdata' in newdata:
        book.readdata = newdata['readdata']
    if 'wordcount' in newdata:
        book.wordCount = newdata['wordcount']
    if 'remark' in newdata:
        book.remark = newdata['remark']

    # 注意，一定要执行save才能将修改信息保存到数据库
    book.save()

    return JsonResponse({'ret': 0})


def delbook(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    customerid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        book = Book.objects.get(id=customerid)
    except Book.DoesNotExist:
        return {
                'ret': 1,
        }

    # delete 方法就将该记录从数据库中删除了
    book.delete()

    return JsonResponse({'ret': 0})


def signin(request):
    userName = request.POST.get('name')
    passWord = request.POST.get('password')
    user = authenticate(username=userName, password=passWord)
    if user is not None:
        request.session['usertype'] = 'hope'
        login(request, user)
        return JsonResponse({'ret': 0})
    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})

#文章内容详情
def docx1(request):
    sort11=request.GET['sort'] #要显示文件的目录
    name1=request.GET['name']  #要显示文件的名字
    
    if(sort11=="cv"): #判断文章类别
        with open("/home/hope/web2/file/cv/"+name1, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)  #将文章转换为html格式
            html = result.value # The generated HTML
        return JsonResponse({'ret': 0, 'retlist': html})
    elif(sort11=="Python"):
        with open("/home/hope/web2/file/Python/"+name1, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value # The generated HTML
        return JsonResponse({'ret': 0, 'retlist': html})
    elif(sort11=="hardware"):
        with open("/home/hope/web2/file/hardware/"+name1, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value # The generated HTML
        return JsonResponse({'ret': 0, 'retlist': html})
    elif(sort11=="web"):
        with open("/home/hope/web2/file/web/"+name1, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value # The generated HTML
        return JsonResponse({'ret': 0, 'retlist': html})
    elif(sort11=="writing"):
        with open("/home/hope/web2/file/writing/"+name1, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value # The generated HTML
        return JsonResponse({'ret': 0, 'retlist': html})
    else:
        return JsonResponse({'ret': 1})


#文章目录
def sort1(request):


    sort11=request.GET['sort'] #要显示的目录
    if(sort11=='cv'):  #判断类别
        for x in os.walk("/home/hope/web2/file/cv"):  #获取文件夹中的文件目录
            list=x[2]
        for id,value in enumerate(list): #文件目录为列表，将目录加上序号。
            list[id]={"id":id,"name":value}  
    elif(sort11=="Python"):
        for x in os.walk("/home/hope/web2/file/Python"):
            list=x[2]
        for id,value in enumerate(list):
            list[id]={"id":id,"name":value} 
    elif(sort11=="hardware"):
        for x in os.walk("/home/hope/web2/file/hardware"):
            list=x[2]
        for id,value in enumerate(list):
            list[id]={"id":id,"name":value} 
    elif(sort11=="web"):
        for x in os.walk("/home/hope/web2/file/web"):
            list=x[2]
        for id,value in enumerate(list):
            list[id]={"id":id,"name":value} 
    elif(sort11=="writing"):
        for x in os.walk("/home/hope/web2/file/writing"):
            list=x[2]
        for id,value in enumerate(list):
            list[id]={"id":id,"name":value} 
    else:
        list="error"

    return JsonResponse({'ret': 0,'retlist': list})

def excerpt(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET
    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_excerpt':
        return listexcerpt(request)
    elif action == 'add_excerpt':
        return addexcerpt(request)
    elif action == 'modify_excerpt':
        return modifyexcerpt(request)
    elif action == 'del_excerpt':
        return delexcerpt(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listexcerpt(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Excerpt.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addexcerpt(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Excerpt.objects.create(content=info['content'])

    return JsonResponse({'ret': 0, 'id': record.id})


def modifyexcerpt(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    excerptid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        excerpt = Excerpt.objects.get(id=excerptid)
    except Excerpt.DoesNotExist:
        return {
            'ret': 1,
        }
    if 'content' in newdata:
        excerpt.content = newdata['content']

    # 注意，一定要执行save才能将修改信息保存到数据库
    book.save()
    return JsonResponse({'ret': 0})


def delexcerpt(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    info = request.params['data']

    try:
        excerpt = Excerpt.objects.get(id=info["id"])
    except Excerpt.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })
    excerpt.delete()
    return JsonResponse({'ret': 0})

