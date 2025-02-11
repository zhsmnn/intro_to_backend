from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('create/', views.create_todo, name='todo_create'),
    path('delete/<int:id>/', views.delete_todo, name='todo_delete'),
]

