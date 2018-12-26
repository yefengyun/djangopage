"""djangofrom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from djangofrom import DynamicRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'favicon.ico', RedirectView.as_view(url=r'/static/favicon.ico')),
    re_path(r'^(?P<app>(\w+))/$', DynamicRouter.matchURL, {'function': 'index'}),
    re_path(r'^(?P<app>(\w+))/(?P<function>(\w+))/$', DynamicRouter.matchURL),
    re_path(r'^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\d*))/', DynamicRouter.matchURL),
    re_path('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\d+))/(?P<id>(\d+))/$', DynamicRouter.matchURL),
]
