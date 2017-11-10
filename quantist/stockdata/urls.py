from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^test_jquery/', views.test_jquery),
    url(r'^test_table/',views.test_table),
    url(r'^test_table2/',views.test_table2),
    url(r'^test_json_ajax/',views.test_json_ajax),
    url(r'^ajax_list/',views.ajax_list),
    url(r'^ajax_dict/',views.ajax_dict),
    url(r'^indicator/',views.indicator),


]
