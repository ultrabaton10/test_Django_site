from django.urls import path, re_path
from app1.views import *


'''
URL configuration for app1
In this urlpatterns list satisfied url`s of main page 
'''

urlpatterns = [
    path('', index, name='main'),
    path('about_site', about_site, name='about_site'),
    path('learning', learning, name='learning'),
    path('community', community, name='community')
]