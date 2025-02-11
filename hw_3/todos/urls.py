from django.urls import path, include
from todos import views
from .forms import TodoForm


urlpatterns = [
    path('',views.todo_list, name='todo_list'),
    path('<int:id>/',views.todo_detail, name='todo_detail'),
    path('create/',.create_detail, name='todo_create'),
    path('delete/<int:id>/'views.delete_todo, name='todo_delete'),
]
