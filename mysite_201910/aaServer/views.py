from django.shortcuts import render

def home(request):
    context = {}
    template = 'home/home.html'
    return render(request, template, context)

def about(request):
    context = {"title": "My Title", "my_list": [1, 2, 3, 5, 9]}
    template = 'home/about.html'
    return render(request, template, context)