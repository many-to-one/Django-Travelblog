from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('update_post/<pk>/', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<pk>/', DeletePost.as_view(), name='delete_post'),
    path('post_view/<pk>/<cpk>/<apk>/', PostView.as_view(), name='post_view'),
    path('likes_view/<pk>/<cpk>/<apk>/', likes_view, name='likes_view'),
    path('posts_by_author/<pk>/', PostsByAuthor.as_view(), name='posts_by_author'),
    path('all_posts/', AllPosts.as_view(), name='all_posts'),
    path('posts_by_category/<pk>/', PostsByCategory.as_view(), name='posts_by_category'),
    path('posts_list/', posts_list, name='posts_list'),
    path('post_list/<str:pk>/', post_list, name='post_list'),
]