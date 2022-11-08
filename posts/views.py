from django.shortcuts import render
from django.views.generic import ListView, CreateView

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


class PostsByAuthor(ListView):
    model = Post
    template_name = 'posts_by_author.html'

    def get_queryset(self):
        return Post.objects.filter(
            slug=self.kwargs['slug']
        )
