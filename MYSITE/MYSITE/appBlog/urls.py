from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='blog-list'),
    path('<str:slug>', views.detail),
    path('<str:slug>/update/', views.update),
    path('<str:slug>/delete/', views.delete),
    path('/create/', views.create, name='blog-create'),
]
