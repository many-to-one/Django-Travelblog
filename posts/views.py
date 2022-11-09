from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from posts.models import Post


class CreatePost(CreateView):
    model = Post
    fields = (
        'title',
        'body',
        'image',
        'category',
    )
    template_name = 'create_post.html'


class PostByAuthor(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_by_author.html'

    def get_queryset(self):
        return Post.objects.filter(
            id=self.kwargs['pk']
        )
