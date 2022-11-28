import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from .models import Post, Category, Comment
from users.models import BlogUser
from .forms import CommentForm
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response


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
        'image',
        'category',
        'author',
    )
    template_name = 'create_post.html'

    def get_initial(self):
        self.initial.update({'author': self.request.user})
        return self.initial


class UpdatePost(UpdateView):
    model = Post
    fields = (
        'title',
        'image',
        'body',
        'category',
    )
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
            'posts': Post.objects.filter(category__id=self.kwargs['cpk'])[:4],
            'author': Post.objects.filter(author__id=self.kwargs['apk'])[:4],
            'most_read': Post.objects.all().order_by('-views')[:4],
            'comments': Comment.objects.filter(post=self.get_object()),
            'form': CommentForm(),
        }
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            body=request.POST.get('body'),
            author=self.request.user,
            post=self.get_object()             
        )
        new_comment.save()
        pk = self.kwargs['pk']
        cpk = self.kwargs['cpk']
        apk = self.kwargs['apk']
        return HttpResponseRedirect(reverse('post_view', kwargs={'pk': pk, 'cpk': cpk, 'apk': apk}))


def likes_view(request, pk, cpk, apk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_view', kwargs={'pk': pk, 'cpk': cpk, 'apk': apk}))


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

##################SERIALIZER##################

@api_view(['GET'])
def posts_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def post_list(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return JsonResponse(serializer.data, safe=False)