from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import pandas as pd
#from bokeh.plotting import figure
#from bokeh.io import output_file,show
import pymysql as mysql
import json
import requests

# Create your views here.
tmp_time = 0
con = mysql.connect(user='root',passwd='caicai520',host='localhost',db='quantist')
con.autocommit(True)
cur = con.cursor()

user_list = [
    {"user":"jack", "pwd":"abc"},
    {"user":"toms", "pwd":"abc"},
]


def index(request):

    return render(request, 'index.html',)


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        temp = {"user":username, "pwd":password}
        user_list.append(temp)
    return render(request, 'login.html',{'data':user_list})


def bootstraps(request):
    return render(request, 'bootstraps.html', )

def bs2(request):
    return render(request, 'bs2.html', )

def co(request):
    return render(request, 'co.html',)

def contral(request):
    return render(request, 'contral.html',)

def face(request):
    return render(request, 'face.html',)



def test(request):
    render(request, 'test.html')

def highchartsTry(request):
    if request.method == 'GET':
        topMusics = [
            ["晴天",1329.656],
            ["告白气球",248.533],
            ["演员",175.353],
            ["Five Hundred Miles",121.012],
            ["Booty Music",111.814],
            ["超越无限",105.345],
            ["刚刚好",104.539],
            ["你还要我怎样",102.994],
            ["夜空中最亮的星",84.444],
            ["全世界谁倾听你 ",64.522],
        ]

        lists = []
        for music_info in topMusics:
            lists.append(music_info)

        return render_to_response('highcharts.html', RequestContext(request,{'lists':lists}))


"""
# bokeh
def waveform(request):
    csv_file = 'your file'
    data = pd.read_csv(csv_file)
    TOOLS = "hover,crosshair,pan,wheel_zoom,box_zoom,reset,save,box_select"
    picture = figure(width=1200, height=400, tools=TOOLS)
    picture.line(data['order'], data['value'], color='blue', alpha=0.5)
    script, div = components(picture, CDN)
    return render(request, 'waveform.html', {'script': script, 'div': div})
"""

"""
def datas(request):
    global tmp_time
    if tmp_time>0:
        sql = 'select * from memory where time>%s' %(tmp_time/1000)
    else:
        sql = 'select * from memory'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time = arr[-1][0]
    return HttpResponse(json.dumps(arr))

def demo(request):
    return render(request, 'datas.html')
"""



