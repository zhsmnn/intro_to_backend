"""
URL configuration for hw_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from todos import views
from django.contrib import admin 


urlpatterns = [
    path('', views.index, name='index'),  
    path('admin/', admin.site.urls),
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/create/', views.create_todo, name='create_todo'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
    path('api/todos/', views.api_todo_list, name='api_todo_list'),
    path('api/todos/<int:id>/', views.api_todo_detail, name='api_todo_detail'),
    path('delete/<int:id>/', views.api_todo_delete, name='todo_delete'),
    path('todos/', include('todos.urls')),
]


