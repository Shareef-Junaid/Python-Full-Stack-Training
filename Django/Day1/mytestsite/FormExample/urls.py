
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index),

    # path('addme', views.add_numbers),
    path('getData', views.index),
    # url('getData', views.index),
    url('addnum', views.add_numbers),
]




