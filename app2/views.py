from django.shortcuts import render, HttpResponse

from app2.models import *
from app2 import common
from app2 import htmlgen


def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, *args, **kwargs):

            before_result = before_func(request, *args, **kwargs)
            if (before_result != None):
                return before_result

            main_result = main_func(request, *args, **kwargs)
            if main_result != None:
                return main_result

            after_result = after_func(request, *args, **kwargs)
            if after_result != None:
                return after_result

        return wrapper

    return outer


def after_index(request, *args, **kwargs):
    print("after")


def before_index(request, *args, **kwargs):
    print("before")


# Create your views here.
@Filter(before_index, after_index)
def index(request, *args, **kwargs):
    page = common.string_int(kwargs['page'], 1)

    cookies = request.COOKIES
    per_item = common.string_int(cookies['page_num'], 5)
    datas = Host.objects.all()
    count = datas.count()

    start, end, allpage = htmlgen.culpage(page, count, per_item)

    data = datas[start:end]

    htmlstr = htmlgen.gen_html(page, allpage, '/app2/index', 5)

    ret = {'data': data, 'count': count, 'htmllist': htmlstr}
    return render(request, 'index2.html', ret)
