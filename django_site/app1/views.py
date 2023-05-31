from django.shortcuts import render

'''
I`ve already create file named as jinja2_tutorial.txt by path test_Django_site/django_site/app1/jinja2_tutorial.txt
In this file i wrote about how may use jinja2 in project
'''

def index(request):
    return render(request, 'app1/index.html')

def about_site(request):
    return render(request, 'app1/about_site.html')

def learning(request):
    return render(request, 'app1/learning.html')

def community(request):
    return render(request, 'app1/community.html')