""" import basic thing for views"""
from django.shortcuts import render

from django.http import HttpResponse

"""first view"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
