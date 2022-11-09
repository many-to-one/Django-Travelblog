from django.urls import path
from .views import *

urlpatterns = [
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('post_by_author/<pk>/', PostByAuthor.as_view(), name='post_by_author'),
]