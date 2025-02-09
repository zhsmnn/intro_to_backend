from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list_create, name='post_list_create'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('todos/', views.todos, name='todos'),
]
