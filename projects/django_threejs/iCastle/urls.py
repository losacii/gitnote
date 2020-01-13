from django.contrib import admin
from django.urls import path, include
from . import views as mainViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainViews.home, name='main-home'),
    path('about/', mainViews.about),
    path('threejs/<str:jsname>/', mainViews.threejs),
]
