""" admin side acces will give permisions to save data """
from django.contrib import admin
from djangoapp.models import Post
from secondapp.models import SecondPost


""" admin models register here and you can get in admin console. 
"""
admin.site.register(Post)
admin.site.register(SecondPost)
