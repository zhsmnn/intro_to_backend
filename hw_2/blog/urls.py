from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.article_detail, name='article_detail'),
    path('<int:id>/', views.article_list, name='article_list'),
]
