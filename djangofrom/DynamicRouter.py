# coding=utf-8
from django.shortcuts import HttpResponse, redirect


def matchURL(request, **kwargs):
    app = kwargs['app']
    func = kwargs['function']
    print(app,func)
    try:
        page = kwargs['page']
    except Exception as e:
        print("not page")

    try:
        appObj = __import__('{}.views'.format(app))
        viewObj = getattr(appObj, 'views')
        funcObj = getattr(viewObj, func)
        try:
            if page:
                result = funcObj(request, page)
        except Exception as e:
            print(e)
            result = funcObj(request)

    except (ImportError, AttributeError) as e:
        print(e)
        # 导入失败时，自定义404错误
        return HttpResponse('404 Not Found')
    except Exception as e:
        print(e)
        return redirect('/{}/index/1/'.format(app))
    return result
