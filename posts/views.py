from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from posts.models import Post


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
    context_object_name = 'post'
    template_name = 'post_view.html'

    def get_queryset(self):
        return Post.objects.filter(
            id=self.kwargs['pk']
        )


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

    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs['slug']
        )


class AllPosts(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all()
    template_name = 'all_posts.html'