from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import *
from .forms import BlogUserCreationForm, BlogUserChangeForm
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')


class CreateUser(CreateView):
    # model = BlogUser
    # fields = (
    #     'username',
    #     'first_name',
    #     'last_name',
    #     'email',
    #     'password1',
    #     'password_confirm',
    #     'photo',
    # )
    form_class = BlogUserCreationForm
    success_url = reverse_lazy('success')

    template_name = 'create_user.html'


class UpdateUser(CreateView):
    form_class = BlogUserChangeForm
    success_url = reverse_lazy('updated')

    template_name = 'update_user.html'


class ProfileView(DetailView):
    model = BlogUser
    context_object_name = 'profile_view' 
    queryset = BlogUser.objects.all()
    template_name = 'profile_view.html'

