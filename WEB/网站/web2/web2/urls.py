"""web2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from hope.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schedule', schedule),
    path('api/book', book),
    path('api/signin', signin),
    path('api/docx',docx1),  #文章内容详情
    path('api/sort',sort1),  #文章目录
    path('api/excerpt',excerpt), #摘录
    path('api/web', webmark) #网站
]
