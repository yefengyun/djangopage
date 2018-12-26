from django.shortcuts import render, HttpResponse

from app2.models import *
from app2 import common
from app2 import htmlgen


# Create your views here.
def index(request, page):
    page = common.string_int(page, 1)

    cookies = request.COOKIES
    per_item = common.string_int(cookies['page_num'], 5)
    datas = Host.objects.all()
    count = datas.count()

    start, end, allpage = htmlgen.culpage(page, count, per_item)

    data = datas[start:end]

    htmlstr = htmlgen.gen_html(page, allpage, '/app2/index', 5)

    ret = {'data': data, 'count': count, 'htmllist': htmlstr}
    return render(request, 'index2.html', ret)
