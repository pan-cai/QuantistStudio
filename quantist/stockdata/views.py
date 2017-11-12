from django.shortcuts import render
from django.http import HttpResponse


from django.http import JsonResponse
import tushare as ts
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')  #quantist/static/template/index.html

def test_jquery(request):
    return render(request, 'test_jquery.html')

def test_table(request):
    t_sh = ts.get_hist_data('sh')[:5]
    print("success..")
    hello = t_sh['open']
    sh_open = t_sh['open']
    sh_high = t_sh['high']
    sh_close = t_sh['close']
    sh_low = t_sh['low']
    sh_p_change = t_sh['p_change']
    sh_volume = t_sh['volume']

    List = {'open':t_sh['open'],'high':t_sh['high'],'low':t_sh['low']}

    return render(request, 'test_table.html',{
                                              'sh_p_change': sh_p_change,
                                              'sh_volume': sh_volume,
                                                't_sh':t_sh,
                                                #'List':json.dumps(List)
                                              })
def test_table2(request):
    t_sh = ts.get_hist_data('sh')[:5]
    d1 = {'n1':100, 'n2':200, 'n3':300}
    j1 = json.dumps(d1)
    d2 = {'open':list(t_sh['open']), 'low':list(t_sh['low']), 'high':list(t_sh['high'])}
    j2 = json.dumps(d2)
    j3 = d2
    j4 = [list(t_sh['open']),list(t_sh['low'])]
    return render(request,'test_table2.html',{'j1':j1,'j2':j2, 'j3':j3,'j4':j4,})

def test_json_ajax(request):
    t_sh = ts.get_hist_data('sh')[:5]
    d2 = {'open':list(t_sh['open']), 'low':list(t_sh['low']), 'high':list(t_sh['high'])}
    j2 = json.dumps(d2)
    return render(request,'test_json_ajax.html',{'j2':j2})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return render(str(a+b))

def ajax_list(request):
    a = list(range(100))
    return JsonResponse(json.dumps(a), safe=False)

def ajax_dict(request):
    name_dict = {'twz':'love','zqxt':'best'}
    #return JsonResponse(name_dict)
    return render(request,'test_json_ajax.html',{'name_dict':name_dict})


def indicator(request):
    #callback = request.GET['callback']
    t_sh = ts.get_hist_data('sh')[:5]
    d2 = {'open': list(t_sh['open']), 'low': list(t_sh['low']), 'high': list(t_sh['high'])}
    j2 = json.dumps(d2,ensure_ascii=False)
    return HttpResponse(j2)
    #return render(request,"indicator.html",{"ret":j2})

"""
t_sh = ts.get_hist_data('sh')[:5]
List = {'open':str(t_sh['open']),'high':str(t_sh['high']),'low':str(t_sh['low'])}
list = json.dumps(List)
print(list)
"""


