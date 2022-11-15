from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('update_post/<pk>/', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<pk>/', DeletePost.as_view(), name='delete_post'),
    path('post_view/<pk>/', PostView.as_view(), name='post_view'),
    path('posts_by_author/<pk>/', PostsByAuthor.as_view(), name='posts_by_author'),
    path('all_posts/', AllPosts.as_view(), name='all_posts'),
    path('posts_by_category/<pk>/', PostsByCategory.as_view(), name='posts_by_category'),
]