"""django app urls file
"""
from django.conf.urls import url
from secondapp import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
]
