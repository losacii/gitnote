from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .forms import BlogPostForm
from .models import BlogPost

#def blog_post_detail_page(request):
#    posts = BlogPost.objects.all()
#    context = {"posts": posts}
#    template = 'blog/blog_post_detail.html'
#    return render(request, template, context)

def blog_post_list_view(request):
    # list out objects
    # Search objects
    # posts = BlogPost.objects.filter(title__icontains="First")
    posts = BlogPost.objects.all()
    template = 'blog/blog_post_list.html'
    context = {"posts": posts}
    return render(request, template, context)

def blog_post_create_view(request):
    # create objects
    # ? use a form
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        post = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()
    template = 'blog/blog_post_create.html'
    context = {"form": form}
    return render(request, template, context)

def blog_post_detail_view(request, slug):
    # Detail view
    post = get_object_or_404(BlogPost, slug=slug)
    template = 'blog/blog_post_detail.html'
    context = {"post": post}
    return render(request, template, context)

def blog_post_update_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    template = 'blog/blog_post_update.html'
    context = {"post": post, 'form': None}
    return render(request, template, context)

def blog_post_delete_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    template = 'blog/blog_post_delete.html'
    context = {"post": post}
    return render(request, template, context)
