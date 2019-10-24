from django.contrib import admin
from django.urls import path, re_path, include

from . import views as mainViews
import blog.views as blogViews

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Main Dir
    path('', mainViews.home, name='main-home'),
    path('about/', mainViews.about, name='main-about'),
    re_path(r'^abou/$', mainViews.about),   # re_path

    # App: blog
    path('blog/', blogViews.blog_post_list_view),
    path('blog/<str:slug>', blogViews.blog_post_detail_view),
    path('blog/<str:slug>/edit/', blogViews.blog_post_update_view),
    path('blog/<str:slug>/delete/', blogViews.blog_post_delete_view),
    path('blog-new/', blogViews.blog_post_create_view),

]

from django.conf import settings