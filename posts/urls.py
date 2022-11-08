from django.urls import path
from .views import *

urlpatterns = [
    path('create_post/', CreatePost.as_view(), name='create_post'),
]