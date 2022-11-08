from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from .models import *
from .forms import BlogUserCreationForm, BlogUserChangeForm, BlogPhotoChangeForm
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')


class CreateUser(CreateView):
    form_class = BlogUserCreationForm
    success_url = reverse_lazy('success')
    template_name = 'create_user.html'


class UpdateUser(UpdateView):
    model = BlogUser
    form_class = BlogUserChangeForm
    success_url = reverse_lazy('success')
    template_name = 'create_user.html'


class UpdatePhoto(UpdateView):
    model = BlogUser
    form_class = BlogPhotoChangeForm
    success_url = reverse_lazy('success')
    template_name = 'create_user.html'


class ProfileView(DetailView):
    model = BlogUser
    context_object_name = 'user'
    queryset = BlogUser.objects.all()
    template_name = 'profile_view.html'

