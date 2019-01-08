from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from djangofrom import settings


# Create your views here.
def login(request):
    context = {'title': "生鲜蔬果-登录"}
    return render(request, "app3/login.html", context)


def register(request):
    context = {'title': "生鲜蔬果-注册"}
    return render(request, "app3/register.html", context)


def register_handle(request):
    email = 'yefengyun241@foxmail.com'
    res = send_mail('论坛激活邮件', '', settings.EMAIL_FROM, [email],
                    html_message='欢迎注册论坛, 点击链接激活你的账户:<a href="127.0.0.1:8000/app3/login/">127.0.0.1:8000/app3/login/</a>')
    print(res)
    return HttpResponse('ok')


def info(request):
    context = {'title': "生鲜蔬果-个人信息", 'page': 1}
    return render(request, "app3/user_center_info.html", context)


def order(request):
    context = {'title': "生鲜蔬果-全部订单", 'page': 2}
    return render(request, "app3/user_center_order.html", context)


def site(request):
    context = {'title': "生鲜蔬果-收货地址", 'page': 3}
    return render(request, "app3/user_center_site.html", context)
