from struct import pack
from django import views
from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('',views.home, name ="home"),
    path('users/', views.getData, name="users"),
    path('posts/', views.getPost, name="getPost"),
    path('post/<int:post_id>/', views.getPostById, name="getPostById"),
    path('updatePost/<int:post_id>/', views.updatePost, name="updatePost"),
    path('getPostByUsedId/<int:user_id>/', views.getPostByUsedId, name="getPostByUsedId"),
    path('createPost/', views.createPost, name="createPost"),
    path('deletePost/<int:post_id>/', views.deletePost, name="deletePost"),

]
