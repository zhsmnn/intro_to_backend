from django.urls import path
from . import views
from .forms import TodoForm

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('create/', views.create_todo, name='todo_create'),
    path('<int:id>/delete/', views.delete_todo, name='todo_delete'),
    
    path('api/', views.api_todo_list, name='api_todo_list'),
    path('api/<int:id>/', views.api_todo_detail, name='api_todo_detail'),
    path('api/create/', views.api_todo_create, name='api_todo_create'),
    path('api/<int:id>/delete/', views.api_todo_delete, name='api_todo_delete'),
]

