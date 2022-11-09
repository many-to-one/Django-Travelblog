from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, \
    DeleteView, ListView

from posts.models import Post
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['post_list'] = Post.objects.bloguser_set.all()
        return context


class DeleteUser(DeleteView):
    model = BlogUser
    success_url = reverse_lazy('success')
    template_name = 'delete_profile.html'
