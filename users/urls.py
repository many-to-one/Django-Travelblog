from django.urls import path
from .views import *

urlpatterns = [
    path('create_user/', CreateUser.as_view(), name='create_user'),
]