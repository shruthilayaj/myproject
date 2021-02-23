from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.blog_post_list, name='posts'),
    path('posts/<int:pk>', views.blog_detail, name='post'),
]
