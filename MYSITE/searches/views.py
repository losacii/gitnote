from django.shortcuts import render

# Create your views here.

from appBlog.models import Post
from .models import SearchQuery

def search(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {'query':query}
    if query is not None:
        blog_list = Post.objects.all().search(query)
    context['blog_list'] = blog_list
    template = 'searches/view.html'
    return render(request, template, context)
