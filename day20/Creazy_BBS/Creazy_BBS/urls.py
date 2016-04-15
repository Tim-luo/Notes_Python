#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""Creazy_BBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from web import views
from web import urls as web_urls
from web_chat import urls as chat_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #include-app web
    url(r'^web/', include(web_urls)),
    #include-app  web_chat
    url(r'^chat/', include(chat_urls)),
    #指定默认的URL,
    url(r'',views.index,name='index'),
]