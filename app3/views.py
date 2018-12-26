from django.shortcuts import render


# Create your views here.
def login(request):
    context = {'title': "生鲜蔬果-登录"}
    return render(request, "app3/login.html", context)


def register(request):
    context = {'title': "生鲜蔬果-注册"}
    return render(request, "app3/register.html",context)


def info(request):
    context = {'title': "生鲜蔬果-个人信息", 'page': 1}
    return render(request, "app3/user_center_info.html", context)


def order(request):
    context = {'title': "生鲜蔬果-全部订单", 'page': 2}
    return render(request, "app3/user_center_order.html", context)


def site(request):
    context = {'title': "生鲜蔬果-收货地址", 'page': 3}
    return render(request, "app3/user_center_site.html", context)
