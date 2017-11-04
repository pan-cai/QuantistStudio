from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^bootstraps/', views.bootstraps),
    url(r'^bs2/', views.bs2),
    url(r'^co/', views.co),
    url(r'^contral/', views.contral),
    url(r'^face/', views.face),
    url(r'^test/', views.test),
    url(r'^highchartsTry/', views.highchartsTry),

]
