from django.urls import path
from .views import login_view, logout_view, todos_list, todo_detail, todo_create, todo_delete

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("todos/", todos_list, name="todos_list"),
    path("todos/<int:id>/", todo_detail, name="todo_detail"),
    path("todos/new/", todo_create, name="todo_create"),
    path("todos/<int:id>/delete/", todo_delete, name="todo_delete"),
]
