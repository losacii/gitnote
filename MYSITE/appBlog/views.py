from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostModelForm
import re
from django.utils import timezone


def list(request):
    now = timezone.now()
    qs = Post.objects.all().published()

    if request.user.is_authenticated:
        my_qs = Post.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct() # do not show duplicates
    # --> posts = Post.objects.filter(title_icontains='hello')
    context = {"posts":qs}
    template = 'appBlog/list.html'
    return render(request, template, context)


def detail(request, slug):
    obj = Post.objects.filter(slug=slug).first()
    context = {"post":obj}
    template = 'appBlog/detail.html'
    return render(request, template, context)


def create(request):
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.slug = '-'.join(re.split('\W+', form.cleaned_data.get("title").lower()))
        obj.save()
        print("\n\n===> valid form, saved.")
        print(form.cleaned_data)
        return redirect("/blog/")
    else:
        print("\n\n===> NOT valid form.")
    context = {"title":"Fill Form", "form": form}
    template = 'appBlog/create.html'
    return render(request, template, context)


def update(request, slug):

    obj = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        form.save()
        return redirect("/blog/")

    context = {'form':form, "title":"Update Post"}
    template = 'form.html'

    return render(request, template, context)


def delete(request, slug):

    obj = get_object_or_404(Post, slug=slug)
    
    if request.method == "POST":
        obj.delete()
        return redirect("/blog/")

    context = {'object':obj, "title":"Delete Post"}
    template = 'appBlog/delete.html'
    return render(request, template, context)

