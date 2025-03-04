from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login/auth/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('todos/', todos_list, name='todos_list'),
    path('todos/<int:id>/', todo_detail, name='todo_detail'),
    path('todos/add/', add_todo, name='add_todo'),
    path('todos/<int:id>/delete/', delete_todo, name='delete_todo'),
]
