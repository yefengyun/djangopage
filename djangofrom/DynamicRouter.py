# coding=utf-8
from django.shortcuts import HttpResponse, redirect


def matchURL(request, **kwargs):
    appandfun = ['app', 'function']
    app = kwargs[appandfun[0]]
    func = kwargs[appandfun[1]]

    newkwargs = {}

    for key, value in kwargs.items():
        if key not in appandfun:
            newkwargs[key] = value

    try:
        appObj = __import__('{}.views'.format(app))
        viewObj = getattr(appObj, 'views')
        funcObj = getattr(viewObj, func)
        result = funcObj(request, **newkwargs)
    except (ImportError, AttributeError) as e:
        print(e)
        # 导入失败时，自定义404错误
        return HttpResponse('404 Not Found')
    except Exception as e:
        print(e)
        return HttpResponse('404 Error')
    return result
