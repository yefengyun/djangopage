from django.shortcuts import render, render_to_response, HttpResponse
from app1 import forms
import json


# Create your views here.
def index(request):
    ret = {'data': None, 'error': ""}
    obj = forms.ALogin()
    ret['data'] = obj
    if request.method == 'POST':
        checkForm = forms.ALogin(request.POST)
        checkResult = checkForm.is_valid()

        if checkResult:
            pass
        else:
            # firstErrorMsg = checkForm.errors.as_()
            # print(firstErrorMsg)
            # ret['error'] = firstErrorMsg
            ret['data'] = checkForm

    return render(request, 'app1/index.html', ret)


def ajaxview(request):
    return render(request, 'app1/testajax.html', {})


def ajaxresp(request):
    if request.method == "POST":
        print(request.POST)
        msg = {'id': 80, 'status': 404, 'msg': '你好'}
        return HttpResponse(json.dumps(msg))
    else:
        return HttpResponse('not ojbk')
