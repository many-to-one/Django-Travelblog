from django.shortcuts import render
from django.views.generic import CreateView
from .models import *


class CreateUser(CreateView):
    model = BlogUser
    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        # 'password2',
        'photo',
    )

    template_name = 'create_user.html'