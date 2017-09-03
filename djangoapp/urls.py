"""django app urls file
"""
from django.conf.urls import url
from djangoapp import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
]
