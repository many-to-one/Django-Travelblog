import json

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from .models import Post, Category
from users.models import BlogUser


class Home(ListView):
    model = Post
    template_name = 'home.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'categories': Category.objects.all(),
            'posts': Post.objects.all(),
            'users': BlogUser.objects.all(),
            'post_json': json.dumps(list(Post.objects.values()))
        }
        return context


class CreatePost(CreateView):
    model = Post
    fields = (
        'title',
        'body',
        # 'image',
        'category',
        'author',
    )
    template_name = 'create_post.html'

    def get_initial(self):
        self.initial.update({'author': self.request.user})
        return self.initial


class UpdatePost(UpdateView):
    model = Post
    fields = [
        'title',
        'image',
        'body',
        'category',
    ]
    template_name = 'update_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = 'create_post'


class PostView(DetailView):
    model = Post
    template_name = 'post_view.html'

    def get_context_data(self, **kwargs):
        context = {
            'post': Post.objects.filter(id=self.kwargs['pk']),
            'posts': Post.objects.filter(category__id=self.kwargs['cpk'])[:3],
            'author': Post.objects.filter(author__id=self.kwargs['apk'])[:3],
        }
        return context


class PostsByAuthor(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts_by_author.html'

    def get_queryset(self):
        return Post.objects.filter(
            author__id=self.kwargs['pk']
        )


class PostsByCategory(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts_by_category.html'

    def get_context_data(self, **kwargs):
        context = {
            'posts': Post.objects.filter(category__id=self.kwargs['pk']),
            'categories': Category.objects.filter(id=self.kwargs['pk']),
        }
        return context

class AllPosts(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all()
    template_name = 'all_posts.html'