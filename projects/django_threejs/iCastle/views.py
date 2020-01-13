from django.shortcuts import render
import os

def home(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    jsfiles = os.listdir(BASE_DIR + '/static/myjs/')
    jsfiles.sort()
    context = {"jsfiles": jsfiles}
    template = 'main/home.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = 'main/about.html'
    return render(request, template, context)

def threejs(request, jsname):
    jsurl = 'myjs/{}'.format(jsname,)
    context = {"jsurl":jsurl, "title":jsname}
    template = 'threejs/view.html'
    return render(request, template, context)
