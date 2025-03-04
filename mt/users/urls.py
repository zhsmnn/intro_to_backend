from django.urls import path
from . import views
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('', views.home, name='home'),
]
