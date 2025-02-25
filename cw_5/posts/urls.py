from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('login/auth/', login_user, name='login_auth'),
    path('logout/', logout_user, name='logout'),
    path('posts/', posts_list, name='posts'),
    path('posts/my/', my_posts, name='my_posts'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:id>/delete/', delete_post, name='delete_post'),
]
